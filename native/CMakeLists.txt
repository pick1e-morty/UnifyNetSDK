cmake_minimum_required(VERSION 3.27)
project(unify_native LANGUAGES CXX)

# ============================================================
# 构建哪些厂商
#
# 两个厂商是**彼此独立的 target**，无依赖关系，所以 ninja 会把所有 TU 混进
# 同一个 -j N 池子并行编译 —— 不是串行。分开构建的意义不是"避免等待两个"，
# 而是"日常只改一个厂商时不必让另一个也进依赖图"。
#
#   all     两个都建（默认）。ninja 会跳过内容未变的 TU，所以日常几乎不额外耗时，
#           且能避免"改了海康却只编了大华"这类静默漏编。
#   dahua   只建大华。
#   haikang 只建海康。
# ============================================================
set(UNIFY_SDK "all" CACHE STRING "构建哪些厂商: dahua / haikang / all")
set_property(CACHE UNIFY_SDK PROPERTY STRINGS dahua haikang all)
if(NOT UNIFY_SDK MATCHES "^(dahua|haikang|all)$")
    message(FATAL_ERROR "UNIFY_SDK must be dahua / haikang / all, got: ${UNIFY_SDK}")
endif()

# ============================================================
# 厂商 SDK 路径
#
# 两个厂商都指向 tools/sync_sdk.py 同步出来的副本 vendor/<厂商>/sdk_win64/{include,lib,bin}，
# 结构同构、全 ASCII 路径。vendor 原始包保持不动，只作为复制源。
#
# 为什么大华也要走副本：它的原始路径本来已是纯 ASCII，但海康的"头文件/库文件"
# 是中文 —— CMake 的 message() 会打印乱码、bat 里传中文路径会让 dumpbin 之类
# 工具直接失败。两边结构对不齐，后来的人就得猜哪个是有意的，索性一起统一。
#
# 换了 vendor SDK 后先跑：  python tools/sync_sdk.py
# 原始包与副本都不入库，见 .gitignore。
# ============================================================
set(DH_ROOT_DEFAULT "${CMAKE_CURRENT_SOURCE_DIR}/../vendor/dahua/sdk_win64")
# *_ROOT_DEFAULT 必须是**普通变量**，不能是 CACHE。踩过的坑：它原本写成
# CACHE PATH 且没有 FORCE，于是自己也被缓存进 CMakeCache.txt —— 源码里改了
# 默认值，已有 build/ 目录里存的仍是旧路径。后果是下面那段 stale 探测永远
# 失效（探测条件里的 DEFAULT 本身就是旧值），DH_ROOT 修不过来，configure
# 只会报"找不到 dhnetsdk.h"，完全看不出真因是 DEFAULT 自己被冻住了。
# 用户要覆盖路径用 -DDH_ROOT=...，那个入口仍然是 CACHE。
#
# DH_ROOT 作为 CACHE 有个固有陷阱：改了默认值，已有 build/CMakeCache.txt 里
# 的旧值**不会**跟着更新。所以先探测旧值是否还有效，无效则 FORCE 更新。
if(NOT EXISTS "${DH_ROOT}/include/dhnetsdk.h"
   AND EXISTS "${DH_ROOT_DEFAULT}/include/dhnetsdk.h")
    message(STATUS "DH_ROOT stale path, updating to ${DH_ROOT_DEFAULT}")
    set(DH_ROOT "${DH_ROOT_DEFAULT}" CACHE PATH "大华 SDK" FORCE)
endif()
set(DH_ROOT "${DH_ROOT_DEFAULT}" CACHE PATH "大华 SDK（sync_sdk.py 同步的副本）")
set(DH_INCLUDE "${DH_ROOT}/include")
set(DH_LIB "${DH_ROOT}/lib")
set(DH_BIN "${DH_ROOT}/bin")

set(HK_ROOT_DEFAULT "${CMAKE_CURRENT_SOURCE_DIR}/../vendor/haikang/sdk_win64")
# 同 DH_ROOT_DEFAULT：必须是普通变量，否则自身被 cache 冻住，stale 探测失效。
if(NOT EXISTS "${HK_ROOT}/include/HCNetSDK.h"
   AND EXISTS "${HK_ROOT_DEFAULT}/include/HCNetSDK.h")
    message(STATUS "HK_ROOT stale path, updating to ${HK_ROOT_DEFAULT}")
    set(HK_ROOT "${HK_ROOT_DEFAULT}" CACHE PATH "海康 SDK" FORCE)
endif()
set(HK_ROOT "${HK_ROOT_DEFAULT}" CACHE PATH "海康 SDK（sync_sdk.py 同步的副本）")
set(HK_INCLUDE "${HK_ROOT}/include")
set(HK_LIB "${HK_ROOT}/lib")
set(HK_BIN "${HK_ROOT}/bin")

if(UNIFY_SDK STREQUAL "all" OR UNIFY_SDK STREQUAL "dahua")
    if(NOT EXISTS "${DH_INCLUDE}/dhnetsdk.h")
        message(FATAL_ERROR "missing ${DH_INCLUDE}/dhnetsdk.h -- run: python tools/sync_sdk.py")
    endif()
endif()
if(UNIFY_SDK STREQUAL "all" OR UNIFY_SDK STREQUAL "haikang")
    if(NOT EXISTS "${HK_INCLUDE}/HCNetSDK.h")
        message(FATAL_ERROR "missing ${HK_INCLUDE}/HCNetSDK.h -- run: python tools/sync_sdk.py")
    endif()
endif()

# ============================================================
# nanobind / Python
# 必须指向本项目的 .venv，不要用系统 Python
# ============================================================
# 项目根的统一 .venv（native/../.venv）
set(NB_PYTHON "${CMAKE_CURRENT_SOURCE_DIR}/../.venv/Scripts/python.exe"
    CACHE FILEPATH "venv 中的 Python 解释器")

execute_process(
    COMMAND "${NB_PYTHON}" -m nanobind --cmake_dir
    OUTPUT_VARIABLE NB_CMAKE_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
    RESULT_VARIABLE NB_RESULT)
if(NOT NB_RESULT EQUAL 0)
    message(FATAL_ERROR "`${NB_PYTHON} -m nanobind --cmake_dir` failed. "
                        "Run: uv venv --python 3.13 && uv pip install nanobind ninja")
endif()
message(STATUS "nanobind cmake dir: ${NB_CMAKE_DIR}")
list(APPEND CMAKE_PREFIX_PATH "${NB_CMAKE_DIR}")

set(Python_FIND_VIRTUALENV FIRST)
find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)
message(STATUS "Python   : ${Python_EXECUTABLE}")
find_package(nanobind CONFIG REQUIRED)

# ============================================================
# 大华 NetSDK 绑定
# ============================================================
if(UNIFY_SDK STREQUAL "all" OR UNIFY_SDK STREQUAL "dahua")
    nanobind_add_module(unify_dh src/dh_netsdk.cpp)
    target_include_directories(unify_dh PRIVATE "${DH_INCLUDE}")
    target_link_libraries(unify_dh PRIVATE "${DH_LIB}/dhnetsdk.lib")

    message(STATUS "DH header: ${DH_INCLUDE}")
    message(STATUS "DH lib   : ${DH_LIB}/dhnetsdk.lib")
    message(STATUS "DH dll   : ${DH_BIN}  (runtime: smoke_test.py calls add_dll_directory)")
else()
    message(STATUS "unify_dh: skipped (UNIFY_SDK=${UNIFY_SDK})")
endif()

# ============================================================
# 全量生成绑定（由 native/codegen/gen_bind.py --sdk <sdk> 产出，不入库、可重建）
# 没有生成产物时自动跳过，不影响对应手写模块的编译。
#
# 大华与海康是两个独立 target：ninja 会把两边的 TU 混进同一个 -j N 池子
# 并行编译，不是串行。它们各自只链自己厂商的 .lib，互不依赖。
# ============================================================
function(add_gen_module target gen_dir include_dir lib_file)
    file(GLOB GEN_SOURCES CONFIGURE_DEPENDS "${gen_dir}/*.cpp")
    if(NOT GEN_SOURCES)
        message(STATUS "${target}: skipped (no generated sources in ${gen_dir})")
        return()
    endif()
    list(LENGTH GEN_SOURCES GEN_N)
    message(STATUS "${target}: ${GEN_N} generated source files")
    nanobind_add_module(${target} ${GEN_SOURCES})
    # 生成的绑定是纯模板胶水：注册类型、转发字段读写，运行时没有任何计算量。
    # -O 优化对产物毫无意义，却让 MSVC 在深层模板实例化上花费大量时间。
    # 必须写在 nanobind_add_module 之后，才排得进 nanobind 自带的 /Os 之后生效。
    if(MSVC)
        target_compile_options(${target} PRIVATE /Od)
    endif()
    target_include_directories(${target} PRIVATE "${include_dir}" "${gen_dir}")
    target_link_libraries(${target} PRIVATE "${lib_file}")
endfunction()

if(UNIFY_SDK STREQUAL "all" OR UNIFY_SDK STREQUAL "dahua")
    # 产物目录 gen_dh / gen_hk：与各 config 的 out_dir、file_prefix、module
    # 同一套命名。目录名只差两个字母，失败提示里务必写明归属（见 build.ps1）。
    add_gen_module(unify_dh_gen
                   "${CMAKE_CURRENT_SOURCE_DIR}/src/gen_dh"
                   "${DH_INCLUDE}" "${DH_LIB}/dhnetsdk.lib")
endif()

if(UNIFY_SDK STREQUAL "all" OR UNIFY_SDK STREQUAL "haikang")
    add_gen_module(unify_hk_gen
                   "${CMAKE_CURRENT_SOURCE_DIR}/src/gen_hk"
                   "${HK_INCLUDE}" "${HK_LIB}/HCNetSDK.lib")
    message(STATUS "HK header: ${HK_INCLUDE}")
    message(STATUS "HK lib   : ${HK_LIB}/HCNetSDK.lib")
    message(STATUS "HK dll   : ${HK_BIN}  (runtime: add_dll_directory)")
endif()
