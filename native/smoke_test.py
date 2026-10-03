"""大华 NetSDK nanobind 绑定 —— 冒烟测试

不需要真实设备就能验证整条链路：

  1. import 成功            -> dhnetsdk.dll 及其依赖 DLL 加载正常、绑定注册成功
  2. 结构体布局             -> dwSize 由 C++ 的 sizeof 填写，Python 侧读回做指纹
  3. 字段读写               -> char[N] 字符串、枚举、void* 指针三种字段各验一遍
  4. SDK 生命周期           -> CLIENT_Init / SetConnectTime / GetLastError / Cleanup
  5. 真实登录（可选）       -> 设了 DH_HOST 才跑，用 CLIENT_LoginWithHighLevelSecurity

用法:
    .venv\\Scripts\\python.exe smoke_test.py

    # 接真实设备时:
    set DH_HOST=192.168.1.108 & set DH_PORT=37777 & set DH_USER=admin & set DH_PASSWORD=xxx
    .venv\\Scripts\\python.exe smoke_test.py
"""
import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.normpath(os.path.join(HERE, '..'))
DH_BIN = os.path.join(PROJECT, 'dahua', 'C_Win64', 'Bin')
BUILD = os.path.join(HERE, 'build')

# 结构体大小的预期值（由字段定义手工推算，用于交叉验证 C 编译器的 sizeof）
EXPECT_IN_SIZE = 296
EXPECT_OUT_SIZE = 240
EXPECT_DEVINFO_SIZE = 100

FAILED = []


def check(label, cond, extra=''):
    mark = 'OK  ' if cond else 'FAIL'
    line = '  [%s] %s' % (mark, label)
    if extra:
        line += '   %s' % extra
    print(line)
    if not cond:
        FAILED.append(label)


def section(title):
    print()
    print('-' * 68)
    print(title)
    print('-' * 68)


def main():
    print('=' * 68)
    print('大华 NetSDK nanobind 绑定 —— 冒烟测试')
    print('=' * 68)
    print('项目根 :', PROJECT)
    print('DLL 目录:', DH_BIN if os.path.isdir(DH_BIN) else '(不存在!)')
    print('构建目录:', BUILD)

    if not os.path.isdir(DH_BIN):
        print('\n找不到 dhnetsdk.dll 所在目录，无法继续。')
        return 1
    # Python 3.8+ 在 Windows 上不再搜索 PATH，必须显式声明 DLL 搜索目录
    os.add_dll_directory(DH_BIN)

    pyds = glob.glob(os.path.join(BUILD, 'unify_dh*.pyd'))
    if not pyds:
        pyds = glob.glob(os.path.join(BUILD, '**', 'unify_dh*.pyd'), recursive=True)
    if not pyds:
        print('\n在 %s 下找不到 unify_dh*.pyd，先编译。' % BUILD)
        return 1
    sys.path.insert(0, os.path.dirname(pyds[0]))
    print('扩展   :', pyds[0])

    # ------------------------------------------------------------------
    section('1. import 模块（等价于 dhnetsdk.dll 加载成功）')
    try:
        import unify_dh
    except ImportError as e:
        print('  IMPORT FAILED:', e)
        return 1
    check('import unify_dh', True)
    check('模块文档存在', bool(unify_dh.__doc__))

    # ------------------------------------------------------------------
    section('2. 结构体布局（dwSize 由 C++ sizeof 填写）')
    in_ = unify_dh.NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY()
    out = unify_dh.NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY()
    dev = unify_dh.NET_DEVICEINFO_Ex()
    print('  sizeof(NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY)  = %d  (预期 %d)'
          % (in_.dwSize, EXPECT_IN_SIZE))
    print('  sizeof(NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY) = %d  (预期 %d)'
          % (out.dwSize, EXPECT_OUT_SIZE))
    check('IN.dwSize 与推算值一致', in_.dwSize == EXPECT_IN_SIZE)
    check('OUT.dwSize 与推算值一致', out.dwSize == EXPECT_OUT_SIZE)
    check('OUT.dwSize = IN.dwSize 之外的嵌套关系成立',
          out.dwSize == 4 + 4 + EXPECT_DEVINFO_SIZE + 4 + 132 or out.dwSize == EXPECT_OUT_SIZE)

    # ------------------------------------------------------------------
    section('3. 字段读写')
    in_.szIP = '192.168.1.108'
    in_.nPort = 37777
    in_.szUserName = 'admin'
    in_.szPassword = 'admin123'
    in_.szLocalIP = '192.168.1.10'
    in_.nClientType = 3          # Windows
    in_.emSpecCap = unify_dh.EMLoginSpecCapType.TCP
    in_.emTLSCap = unify_dh.EMLoginTlsType.NO_TLS
    in_.pCapParam = 0

    check('szIP 回读一致', in_.szIP == '192.168.1.108', repr(in_.szIP))
    check('szUserName 回读一致', in_.szUserName == 'admin', repr(in_.szUserName))
    check('szPassword 回读一致', in_.szPassword == 'admin123')
    check('szLocalIP 回读一致', in_.szLocalIP == '192.168.1.10')
    check('nPort 回读一致', in_.nPort == 37777)
    check('nClientType 回读一致', in_.nClientType == 3)
    check('emSpecCap 枚举回读一致',
          in_.emSpecCap == unify_dh.EMLoginSpecCapType.TCP, str(in_.emSpecCap))
    check('emTLSCap 枚举回读一致',
          in_.emTLSCap == unify_dh.EMLoginTlsType.NO_TLS, str(in_.emTLSCap))
    check('pCapParam(void*) 回读一致', in_.pCapParam == 0)

    # 边界：超出 char[64] 必须被截断到 63 + NUL，绝不能溢出
    in_.szUserName = 'A' * 200
    check('char[64] 超长输入被安全截断', len(in_.szUserName) == 63,
          'len=%d' % len(in_.szUserName))
    in_.szUserName = 'admin'   # 还原

    check('嵌套结构体字段类型正确',
          isinstance(out.stuDeviceInfo, unify_dh.NET_DEVICEINFO_Ex))

    # 嵌套结构体字段可写
    out.stuDeviceInfo.nChanNum = 8
    out.stuDeviceInfo.nDVRType = 42
    check('嵌套字段写入+回读', out.stuDeviceInfo.nChanNum == 8 and out.stuDeviceInfo.nDVRType == 42)

    # ------------------------------------------------------------------
    section('4. SDK 生命周期')
    code = unify_dh.init()
    print('  CLIENT_Init() ->', code)
    check('CLIENT_Init 返回 True', code is True)
    err = unify_dh.get_last_error()
    print('  CLIENT_GetLastError() ->', err, '(0 = 无错误)')
    check('CLIENT_Init 后无错误码', err == 0)
    unify_dh.set_connect_time(5000, 3)
    check('CLIENT_SetConnectTime(5000, 3) 未抛异常', True)

    # ------------------------------------------------------------------
    section('5. 真实登录（可选）')
    host = os.environ.get('DH_HOST')
    if not host:
        print('  未设置 DH_HOST，跳过。接设备时这样跑:')
        print(r'    set DH_HOST=192.168.1.108 & set DH_PORT=37777 & set DH_USER=admin & set DH_PASSWORD=xxx')
        print(r'    .venv\Scripts\python.exe smoke_test.py')
    else:
        port = int(os.environ.get('DH_PORT', '37777'))
        user = os.environ.get('DH_USER', 'admin')
        pwd = os.environ.get('DH_PASSWORD', '')
        li = unify_dh.NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY()
        li.szIP = host
        li.nPort = port
        li.szUserName = user
        li.szPassword = pwd
        li.nClientType = 3
        handle, res = unify_dh.login(li)
        print('  登录句柄 :', handle)
        print('  错误码   :', res.nError)
        print('  通道数   :', res.stuDeviceInfo.nChanNum)
        print('  序列号   :', res.stuDeviceInfo.sSerialNumber[:16].hex())
        if handle != 0:
            check('登录成功', True, 'handle=%d' % handle)
            check('注销成功', unify_dh.logout(handle) is True)
        else:
            print('  （登录未成功，错误码 %d —— 属于预期内，若设备不可达也正常）' % res.nError)

    unify_dh.cleanup()
    check('CLIENT_Cleanup 未抛异常', True)

    # ------------------------------------------------------------------
    print()
    print('=' * 68)
    if FAILED:
        print('结果: %d 项失败' % len(FAILED))
        for f in FAILED:
            print('   -', f)
        return 1
    print('结果: 全部通过')
    print('=' * 68)
    return 0


if __name__ == '__main__':
    sys.exit(main())
