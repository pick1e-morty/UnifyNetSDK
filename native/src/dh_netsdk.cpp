// Unified NetSDK -- Dahua NetSDK (dhnetsdk) minimal real-path binding.
//
// Goal: prove the end-to-end chain on REAL types (not synthetic slices):
//   1. dhnetsdk.h is consumed by MSVC as-is
//      (default args, __stdcall, enums, anonymous struct typedefs)
//   2. dhnetsdk.lib links
//   3. the nanobind module imports
//   4. real structs are readable from Python
//      (char[N] arrays, void* pointers, nested struct, enum fields)
//
// ENCODING NOTE: keep this file ASCII-only. dhnetsdk.h is GBK-encoded, so the
// compiler must NOT be given /utf-8, otherwise the header's Chinese comments
// get mis-decoded.

#define NOMINMAX
#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>

#include <cstddef>
#include <cstdint>
#include <cstring>
#include <string>

#include <dhnetsdk.h>

namespace nb = nanobind;

namespace {

template <std::size_t N>
std::string read_cstr(const char (&buf)[N]) {
    std::size_t n = 0;
    while (n < N && buf[n] != '\0') ++n;
    return std::string(buf, n);
}

template <std::size_t N>
void write_cstr(char (&buf)[N], const std::string &v) {
    std::size_t n = v.size() < N - 1 ? v.size() : N - 1;
    std::memcpy(buf, v.data(), n);
    std::memset(buf + n, 0, N - n);
}

}  // namespace

NB_MODULE(unify_dh, m) {
    m.doc() = "Dahua NetSDK minimal binding (nanobind) -- real end-to-end path";

    // ---------------------------------------------------------------- enums
    nb::enum_<EM_LOGIN_SPAC_CAP_TYPE>(m, "EMLoginSpecCapType", nb::is_arithmetic())
        .value("TCP", EM_LOGIN_SPEC_CAP_TCP)
        .value("ANY", EM_LOGIN_SPEC_CAP_ANY)
        .value("SERVER_CONN", EM_LOGIN_SPEC_CAP_SERVER_CONN)
        .value("MULTICAST", EM_LOGIN_SPEC_CAP_MULTICAST)
        .value("UDP", EM_LOGIN_SPEC_CAP_UDP)
        .value("MAIN_CONN_ONLY", EM_LOGIN_SPEC_CAP_MAIN_CONN_ONLY)
        .value("SSL", EM_LOGIN_SPEC_CAP_SSL);

    nb::enum_<EM_LOGIN_TLS_TYPE>(m, "EMLoginTlsType", nb::is_arithmetic())
        .value("NO_TLS", EM_LOGIN_TLS_TYPE_NO_TLS)
        .value("TLS_ADAPTER", EM_LOGIN_TLS_TYPE_TLS_ADAPTER)
        .value("TLS_COMPEL", EM_LOGIN_TLS_TYPE_TLS_COMPEL)
        .value("TLS_MAIN_ONLY", EM_LOGIN_TLS_TYPE_TLS_MAIN_ONLY)
        .value("TLS_GENERAL", EM_LOGIN_TLS_TYPE_TLS_GENERAL)
        .value("TLS_UPNP", EM_LOGIN_TLS_TYPE_TLS_UPNP);

    // ------------------------------------------------------ NET_DEVICEINFO_Ex
    // Nested inside NET_OUT_LOGIN_..., so it must be registered first.
    nb::class_<NET_DEVICEINFO_Ex>(m, "NET_DEVICEINFO_Ex")
        .def(nb::init<>())
        .def_prop_rw("sSerialNumber",
                     [](const NET_DEVICEINFO_Ex &s) {
                         return nb::bytes(reinterpret_cast<const char *>(s.sSerialNumber),
                                          sizeof(s.sSerialNumber));
                     },
                     [](NET_DEVICEINFO_Ex &s, const nb::bytes &v) {
                         std::size_t n = v.size() < sizeof(s.sSerialNumber)
                                             ? v.size()
                                             : sizeof(s.sSerialNumber);
                         std::memcpy(s.sSerialNumber, v.data(), n);
                     },
                     "unsigned char[DH_SERIALNO_LEN] <-> bytes")
        .def_rw("nAlarmInPortNum", &NET_DEVICEINFO_Ex::nAlarmInPortNum)
        .def_rw("nAlarmOutPortNum", &NET_DEVICEINFO_Ex::nAlarmOutPortNum)
        .def_rw("nDiskNum", &NET_DEVICEINFO_Ex::nDiskNum)
        .def_rw("nDVRType", &NET_DEVICEINFO_Ex::nDVRType)
        .def_rw("nChanNum", &NET_DEVICEINFO_Ex::nChanNum)
        .def_rw("byLimitLoginTime", &NET_DEVICEINFO_Ex::byLimitLoginTime)
        .def_rw("byLeftLogTimes", &NET_DEVICEINFO_Ex::byLeftLogTimes)
        .def_rw("nLockLeftTime", &NET_DEVICEINFO_Ex::nLockLeftTime)
        .def_rw("nNTlsPort", &NET_DEVICEINFO_Ex::nNTlsPort)
        .def_rw("nKeyFrameEncrypt", &NET_DEVICEINFO_Ex::nKeyFrameEncrypt)
        .def_prop_rw("emAlgorithm",
                     [](const NET_DEVICEINFO_Ex &s) {
                         return static_cast<int>(s.emAlgorithm);
                     },
                     [](NET_DEVICEINFO_Ex &s, int v) {
                         s.emAlgorithm = static_cast<EM_ALGORITHM_TYPE>(v);
                     },
                     "EM_ALGORITHM_TYPE exposed as int (enum not bound yet)");

    // --------------------------- NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY
    using InLogin = NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY;
    nb::class_<InLogin>(m, "NET_IN_LOGIN_WITH_HIGHLEVEL_SECURITY")
        .def("__init__",
             [](InLogin *self) {
                 std::memset(self, 0, sizeof(*self));
                 // dwSize is the classic source of silent failures -- fill it for the user.
                 self->dwSize = sizeof(*self);
                 self->emSpecCap = EM_LOGIN_SPEC_CAP_TCP;
             })
        .def_rw("dwSize", &InLogin::dwSize, "sizeof(struct), filled automatically")
        .def_prop_rw("szIP",
                     [](const InLogin &s) { return read_cstr(s.szIP); },
                     [](InLogin &s, const std::string &v) { write_cstr(s.szIP, v); })
        .def_rw("nPort", &InLogin::nPort)
        .def_prop_rw("szUserName",
                     [](const InLogin &s) { return read_cstr(s.szUserName); },
                     [](InLogin &s, const std::string &v) { write_cstr(s.szUserName, v); })
        .def_prop_rw("szPassword",
                     [](const InLogin &s) { return read_cstr(s.szPassword); },
                     [](InLogin &s, const std::string &v) { write_cstr(s.szPassword, v); })
        .def_rw("emSpecCap", &InLogin::emSpecCap)
        .def_rw("emTLSCap", &InLogin::emTLSCap)
        .def_prop_rw("szLocalIP",
                     [](const InLogin &s) { return read_cstr(s.szLocalIP); },
                     [](InLogin &s, const std::string &v) { write_cstr(s.szLocalIP, v); })
        .def_rw("nClientType", &InLogin::nClientType)
        .def_rw("nSpecEx", &InLogin::nSpecEx)
        .def_rw("nVendor", &InLogin::nVendor)
        .def_prop_rw("pCapParam",
                     [](const InLogin &s) {
                         return reinterpret_cast<std::uintptr_t>(s.pCapParam);
                     },
                     [](InLogin &s, std::uintptr_t v) {
                         s.pCapParam = reinterpret_cast<void *>(v);
                     },
                     "void* exposed as int; 0 = NULL");

    // -------------------------- NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY
    using OutLogin = NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY;
    nb::class_<OutLogin>(m, "NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY")
        .def("__init__",
             [](OutLogin *self) {
                 std::memset(self, 0, sizeof(*self));
                 self->dwSize = sizeof(*self);
             })
        .def_rw("dwSize", &OutLogin::dwSize)
        .def_rw("stuDeviceInfo", &OutLogin::stuDeviceInfo)
        .def_rw("nError", &OutLogin::nError);

    // ----------------------------------------------------------- functions
    m.def("init",
          [](std::uintptr_t cb, std::uintptr_t user) -> bool {
              return CLIENT_Init(reinterpret_cast<fDisConnect>(cb),
                                 static_cast<LDWORD>(user)) != FALSE;
          },
          nb::arg("cb") = 0, nb::arg("user") = 0,
          "CLIENT_Init; cb = address of an fDisConnect callback (0 = none)");

    m.def("cleanup", []() { CLIENT_Cleanup(); }, "CLIENT_Cleanup");

    m.def("get_last_error",
          []() -> unsigned int { return static_cast<unsigned int>(CLIENT_GetLastError()); },
          "CLIENT_GetLastError");

    m.def("set_connect_time",
          [](int wait_ms, int tries) { CLIENT_SetConnectTime(wait_ms, tries); },
          nb::arg("wait_ms"), nb::arg("tries"), "CLIENT_SetConnectTime");

    m.def("login",
          [](const InLogin &in_param) {
              LLONG handle;
              OutLogin out;
              {
                  nb::gil_scoped_release release;  // 阻塞期间释放 GIL，避免饿死同进程其他线程
                  InLogin in_copy = in_param;  // the API takes a non-const pointer
                  std::memset(&out, 0, sizeof(out));
                  out.dwSize = sizeof(out);
                  handle = CLIENT_LoginWithHighLevelSecurity(&in_copy, &out);
              }
              return nb::make_tuple(static_cast<long long>(handle), out);
          },
          nb::arg("in_param"),
          "returns (login_handle, NET_OUT_LOGIN_WITH_HIGHLEVEL_SECURITY)");

    m.def("logout",
          [](long long handle) -> bool {
              nb::gil_scoped_release release;  // 阻塞期间释放 GIL
              return CLIENT_Logout(static_cast<LLONG>(handle)) != FALSE;
          },
          nb::arg("handle"), "CLIENT_Logout");

    m.def("log_open",
          [](const std::string &path) -> bool {
              LOG_SET_PRINT_INFO info;
              std::memset(&info, 0, sizeof(info));
              info.dwSize = sizeof(info);
              info.bSetFilePath = TRUE;
              std::strncpy(info.szLogFilePath, path.c_str(),
                           sizeof(info.szLogFilePath) - 1);
              info.bSetPrintStrategy = TRUE;
              info.nPrintStrategy = 0;
              return CLIENT_LogOpen(&info) != FALSE;
          },
          nb::arg("path"), "CLIENT_LogOpen (SDK log to file)");

    m.def("log_close", []() { CLIENT_LogClose(); }, "CLIENT_LogClose");
}
