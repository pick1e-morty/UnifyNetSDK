"""
从大华 dhnetsdk.h 提取具名结构体，生成 nanobind 绑定代码，用于测量编译耗时。

用法:
    python gen_probe.py <目标字段数> <输出cpp> [with_array]

分档生成（如 500 / 2000 / 5000 字段），分别编译计时后拟合:
    总耗时 = 固定成本(吃头文件) + 每字段成本 × 字段数

字段分两类，成本不同:
    - 标量字段: .def_rw("x", &S::x)                 —— 便宜
    - 数组字段: .def_prop_rw(...) + lambda 转换       —— 贵，且占 27%
"""
import re
import sys
import collections

try:
    from tqdm import tqdm
except ImportError:  # 没装 tqdm 也能正常生成，只是没有进度条
    def tqdm(it=None, **kw):
        return it

HEADER = r'c:\Users\Hast\Documents\CodeProjects\UnifyNetSDK\dahua\C_Win64\Include\Common\dhnetsdk.h'

STRUCT_RE = re.compile(r'typedef\s+struct\s*(?:\w+\s*)?\{([^{}]*)\}\s*(\w+)\s*;', re.S)

FIELD_RE = re.compile(
    r'^[ \t]*(?:(?:const|volatile|static)\s+)*'
    r'((?:unsigned\s+|signed\s+)*(?:long\s+)?(?:int|char|short|long|float|double)?'
    r'[A-Za-z_]\w*(?:\s*\*)*)'
    r'\s+([A-Za-z_]\w*)\s*(\[[^\]]*\])?\s*;',
    re.M)


# typedef int (CALLBACK *fOfflineCallBack)(...);  —— 这类函数指针类型
FP_RE = re.compile(r'typedef\s+[^(;]*\(\s*(?:CALLBACK|__stdcall|__cdecl|WINAPI)?\s*\*\s*(\w+)\s*\)\s*\(')


def extract():
    text = open(HEADER, encoding='latin-1', errors='replace').read()
    fp_types = set(FP_RE.findall(text))
    out, seen, fp_skip, ptr_skip = [], set(), 0, 0
    for m in tqdm(list(STRUCT_RE.finditer(text)), desc='  解析结构体',
                  unit=' struct', leave=False):
        body, name = m.group(1), m.group(2)
        if name in seen:
            continue
        fields = []
        for fm in FIELD_RE.finditer(body):
            ftype, fname, arr = fm.group(1).strip(), fm.group(2), fm.group(3)
            if fname in ('struct', 'union', 'enum'):
                continue
            # 函数指针字段：nanobind 无法把 C 函数指针映射为 Python
            if ftype in fp_types or '(' in ftype:
                fp_skip += 1
                continue
            # 裸指针字段（char* / void* 等）：def_rw 无法处理
            if '*' in ftype:
                ptr_skip += 1
                continue
            fields.append((ftype, fname, bool(arr)))
        if not fields:
            continue
        seen.add(name)
        out.append((name, fields))
    return out, fp_skip, ptr_skip, len(fp_types)


def gen_field(name, ftype, fname, is_arr, with_array):
    if not is_arr:
        return ['        .def_rw("%s", &%s::%s)' % (fname, name, fname)]
    if not with_array:
        return None
    # 只有纯 char[N] 才能构造 std::string；unsigned char[N] / BYTE[N] 走 bytes 分支
    if ftype.replace(' ', '') == 'char':
        # char[N] -> std::string
        # 注意: 不用 std::min —— windows.h 会把 min 定义成宏，展开后变成 std::( ... ) 报 C2589
        return [
            '        .def_prop_rw("%s",' % fname,
            '            [](const %s &s) { return std::string(s.%s); },' % (name, fname),
            '            [](%s &s, const std::string &v) {' % name,
            '                size_t n = v.size() < sizeof(s.%s) - 1 ? v.size() : sizeof(s.%s) - 1;' % (fname, fname),
            '                memcpy(s.%s, v.data(), n);' % fname,
            '                s.%s[n] = 0;' % fname,
            '            })',
        ]
    # 非 char 数组（BYTE[N] / DWORD[N] 等）：转成 bytes
    return [
        '        .def_prop_rw("%s",' % fname,
        '            [](const %s &s) {' % name,
        '                return nb::bytes(reinterpret_cast<const char *>(s.%s), sizeof(s.%s));' % (fname, fname),
        '            },',
        '            [](%s &s, const nb::bytes &v) {' % name,
        '                size_t n = (size_t)v.size() < sizeof(s.%s) ? (size_t)v.size() : sizeof(s.%s);' % (fname, fname),
        '                memcpy(s.%s, (const char *)v.data(), n);' % fname,
        '            })',
    ]


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    target = int(sys.argv[1])
    out_path = sys.argv[2]
    with_array = len(sys.argv) > 3 and sys.argv[3] == 'with_array'

    structs, fp_skip, ptr_skip, n_fp = extract()
    tf = sum(len(f) for _, f in structs)
    ta = sum(1 for _, f in structs for _, _, a in f if a)
    tc = collections.Counter(t.replace(' ', '') for _, f in structs for t, _, a in f if a)
    print('头文件: %d 结构体 / %d 字段 / 数组字段 %d (%.0f%%)'
          % (len(structs), tf, ta, 100.0 * ta / tf))
    print('  函数指针类型 %d / 跳过函数指针字段 %d / 跳过指针字段 %d' % (n_fp, fp_skip, ptr_skip))
    print('  数组字段类型 TOP:', tc.most_common(6))

    chosen, used = [], 0
    for name, fields in structs:
        if used >= target:
            break
        chosen.append((name, fields))
        used += len(fields)

    # NOMINMAX 必须在 dhnetsdk.h(内含 windows.h) 之前，否则 min/max 宏会污染后续代码
    L = ['#define NOMINMAX',
         '#include <nanobind/nanobind.h>',
         '#include <nanobind/stl/string.h>',
         '#include <string>',
         '#include <cstring>',
         '#include <dhnetsdk.h>',
         '',
         'namespace nb = nanobind;',
         '',
         'NB_MODULE(probe, m) {',
         '    m.doc() = "nanobind compile benchmark";']
    # 阶段1: 先注册所有类型，保证字段引用其它结构体时该类型已为 nanobind 所知
    for name, _ in chosen:
        L.append('    nb::class_<%s> c_%s(m, "%s");' % (name, name, name))
    L.append('')

    # 阶段2: 再逐个绑定字段
    n_scalar = n_arr = n_skip = 0
    for name, fields in chosen:
        body = ['        .def(nb::init<>())']
        for ftype, fname, is_arr in fields:
            g = gen_field(name, ftype, fname, is_arr, with_array)
            if g is None:
                n_skip += 1
                continue
            body += g
            if is_arr:
                n_arr += 1
            else:
                n_scalar += 1
        L.append('    c_%s' % name)
        L += body
        L.append('        ;')
    L.append('}')

    open(out_path, 'w', encoding='ascii', errors='replace').write('\n'.join(L) + '\n')
    print('生成 %s : 结构体 %d / 标量 %d / 数组 %d / 跳过 %d'
          % (out_path, len(chosen), n_scalar, n_arr, n_skip))


if __name__ == '__main__':
    main()
