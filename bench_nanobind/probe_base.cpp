// 基准：只包含大华头文件，不做任何绑定。
// 用于分离「吃 dhnetsdk.h 的固定成本」与「每字段的边际成本」。
#include <nanobind/nanobind.h>
#include <dhnetsdk.h>

namespace nb = nanobind;

NB_MODULE(probe_base, m) {
    m.doc() = "baseline: only include dhnetsdk.h, bind nothing";
}
