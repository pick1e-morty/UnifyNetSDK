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
    message(FATAL_ERROR "UNIFY_SDK 只能是 dahua / haikang / all，收到: ${UNIFY_SDK}")
endif()

# ============================================================
# 厂商 SDK 路径（SDK 原始包不入库，见 .gitignore）
# ============================================================
set(DH_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/../dahua/C_Win64" CACHE PATH "大华 SDK 根目录")
set(DH_INCLUDE "${DH_ROOT}/Include/Common")
set(DH_LIB "${DH_ROOT}/Lib/Win64")
set(DH_BIN "${DH_ROOT}/Bin")

# 海康 SDK 的目录名是中文（"头文件" / "库文件"），且版本号带构建号，
# 所以整条路径只能用 CACHE 变量传进来，无法像大华那样拼相对路径。
set(HK_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/../haikang/HCNetSDK_Win64/HCNetSDKV6.1.11.30_build20260805_Win64_ZH"
    CACHE PATH "海康 SDK 根目录（含 头文件/ 与 库文件/）")
set(HK_INCLUDE "${HK_ROOT}/头文件")
set(HK_LIB "${HK_ROOT}/库文件")
set(HK_BIN "${HK_ROOT}/库文件")

if(UNIFY_SDK STREQUAL "all" OR UNIFY_SDK STREQUAL "dahua")
    if(NOT EXISTS "${DH_INCLUDE}/dhnetsdk.h")
        message(FATAL_ERROR "找不到 dhnetsdk.h，检查 DH_ROOT: ${DH_ROOT}")
    endif()
endif()
if(UNIFY_SDK STREQUAL "all" OR UNIFY_SDK STREQUAL "haikang")
    if(NOT EXISTS "${HK_INCLUDE}/HCNetSDK.h")
        message(FATAL_ERROR "找不到 HCNetSDK.h，检查 HK_ROOT: ${HK_ROOT}")
    endif()
endif()

# ============================================================
# nanobind / Python
# 必须指向本项目的 .venv，不要用系统 Python
# ============================================================
# 项目根的统一 .venv（native/../.venv），与 bench_nanobind 共用同一份
set(NB_PYTHON "${CMAKE_CURRENT_SOURCE_DIR}/../.venv/Scripts/python.exe"
    CACHE FILEPATH "venv 中的 Python 解释器")

execute_process(
    COMMAND "${NB_PYTHON}" -m nanobind --cmake_dir
    OUTPUT_VARIABLE NB_CMAKE_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
    RESULT_VARIABLE NB_RESULT)
if(NOT NB_RESULT EQUAL 0)
    message(FATAL_ERROR "`${NB_PYTHON} -m nanobind --cmake_dir` 失败。"
                        "请先: uv venv --python 3.13 && uv pip install nanobind ninja")
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
    message(STATUS "DH dll   : ${DH_BIN}  (运行时需要，smoke_test.py 会 add_dll_directory)")
else()
    message(STATUS "unify_dh: skipped (UNIFY_SDK=${UNIFY_SDK})")
endif()

# ============================================================
# 全量生成绑定（由 tools/gen_bind.py --sdk <sdk> 产出，不入库、可重建）
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
    add_gen_module(unify_dh_gen
                   "${CMAKE_CURRENT_SOURCE_DIR}/src/gen"
                   "${DH_INCLUDE}" "${DH_LIB}/dhnetsdk.lib")
endif()

if(UNIFY_SDK STREQUAL "all" OR UNIFY_SDK STREQUAL "haikang")
    add_gen_module(unify_hk_gen
                   "${CMAKE_CURRENT_SOURCE_DIR}/src/gen_hk"
                   "${HK_INCLUDE}" "${HK_LIB}/HCNetSDK.lib")
    message(STATUS "HK header: ${HK_INCLUDE}")
    message(STATUS "HK lib   : ${HK_LIB}/HCNetSDK.lib")
    message(STATUS "HK dll   : ${HK_BIN}  (运行时需要)")
endif()
