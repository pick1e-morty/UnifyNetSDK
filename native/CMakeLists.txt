cmake_minimum_required(VERSION 3.27)
project(unify_native LANGUAGES CXX)

# ============================================================
# 厂商 SDK 路径（SDK 原始包不入库，见 .gitignore）
# ============================================================
set(DH_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/../dahua/C_Win64" CACHE PATH "大华 SDK 根目录")
set(DH_INCLUDE "${DH_ROOT}/Include/Common")
set(DH_LIB "${DH_ROOT}/Lib/Win64")
set(DH_BIN "${DH_ROOT}/Bin")

if(NOT EXISTS "${DH_INCLUDE}/dhnetsdk.h")
    message(FATAL_ERROR "找不到 dhnetsdk.h，检查 DH_ROOT: ${DH_ROOT}")
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
nanobind_add_module(unify_dh src/dh_netsdk.cpp)
target_include_directories(unify_dh PRIVATE "${DH_INCLUDE}")
target_link_libraries(unify_dh PRIVATE "${DH_LIB}/dhnetsdk.lib")

message(STATUS "DH header: ${DH_INCLUDE}")
message(STATUS "DH lib   : ${DH_LIB}/dhnetsdk.lib")
message(STATUS "DH dll   : ${DH_BIN}  (运行时需要，smoke_test.py 会 add_dll_directory)")

# ============================================================
# 全量生成绑定（由 tools/gen_dh_bind.py 产出，不入库、可重建）
# 没有生成产物时自动跳过，不影响 unify_dh 的编译
# ============================================================
set(GEN_DIR "${CMAKE_CURRENT_SOURCE_DIR}/src/gen")
file(GLOB GEN_SOURCES CONFIGURE_DEPENDS "${GEN_DIR}/*.cpp")
if(GEN_SOURCES)
    list(LENGTH GEN_SOURCES GEN_N)
    message(STATUS "unify_dh_gen: ${GEN_N} generated source files")
    nanobind_add_module(unify_dh_gen ${GEN_SOURCES})
    # 生成的绑定是纯模板胶水：注册类型、转发字段读写，运行时没有任何计算量。
    # -O 优化对产物毫无意义，却让 MSVC 在深层模板实例化上花费大量时间。
    # 必须写在 nanobind_add_module 之后，才排得进 nanobind 自带的 /Os 之后生效。
    if(MSVC)
        target_compile_options(unify_dh_gen PRIVATE /Od)
    endif()
    target_include_directories(unify_dh_gen PRIVATE "${DH_INCLUDE}" "${GEN_DIR}")
    target_link_libraries(unify_dh_gen PRIVATE "${DH_LIB}/dhnetsdk.lib")
else()
    message(STATUS "unify_dh_gen: skipped (no generated sources in ${GEN_DIR})")
endif()
