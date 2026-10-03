cmake_minimum_required(VERSION 3.27)
project(dh_probe LANGUAGES CXX)

set(DH_INCLUDE "c:/Users/Hast/Documents/CodeProjects/UnifyNetSDK/dahua/C_Win64/Include/Common"
    CACHE PATH "大华头文件目录")

# 用于查询 nanobind cmake_dir 的解释器。必须指向 bench_nanobind/.venv，
# 不要用系统 Python（本项目依赖用 uv 隔离）。
# 用法: cmake -DNB_PYTHON=<...>/.venv/Scripts/python.exe ...
set(NB_PYTHON "python" CACHE FILEPATH "venv 中的 Python 解释器")

execute_process(
    COMMAND "${NB_PYTHON}" -m nanobind --cmake_dir
    OUTPUT_VARIABLE NB_CMAKE_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
    RESULT_VARIABLE NB_RESULT)
if(NOT NB_RESULT EQUAL 0)
    message(FATAL_ERROR "`${NB_PYTHON} -m nanobind --cmake_dir` 失败。"
                        "请确认 NB_PYTHON 指向 .venv 且已 uv pip install nanobind")
endif()
message(STATUS "nanobind cmake dir: ${NB_CMAKE_DIR}")
list(APPEND CMAKE_PREFIX_PATH "${NB_CMAKE_DIR}")

# 禁止 CMake 自己去找系统 Python
set(Python_FIND_VIRTUALENV FIRST)
find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)
message(STATUS "Python: ${Python_EXECUTABLE}")
find_package(nanobind CONFIG REQUIRED)

# 基准 + 三档样本，用于拟合: 总耗时 = 固定成本 + 每字段成本 × 字段数
nanobind_add_module(probe_base probe_base.cpp)
target_include_directories(probe_base PRIVATE "${DH_INCLUDE}")

foreach(N 500 2000 5000)
    nanobind_add_module(probe_${N} probe_${N}.cpp)
    target_include_directories(probe_${N} PRIVATE "${DH_INCLUDE}")
endforeach()
