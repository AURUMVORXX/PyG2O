# Simple toolchain file for compiling under linux
# Usage: cmake .. -DCMAKE_TOOLCHAIN_FILE=linux-arm64.cmake

# specify the target system properties
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR aarch64)

# specify cross compiler
set(CMAKE_C_COMPILER aarch64-linux-gnu-gcc)
 set(CMAKE_CXX_COMPILER aarch64-linux-gnu-g++)

# specify the paths for find_(name), functions (target environment). 
set(CMAKE_FIND_ROOT_PATH
    /usr/lib
    /usr/aarch64-linux-gnu
    ${CMAKE_CURRENT_SOURCE_DIR}
)

# search only for programs in the build host directories (find_program)
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)

# use only CMAKE_FIND_ROOT_PATH for searching (find_library)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)

# use only CMAKE_FIND_ROOT_PATH for searching (find_file, find_path)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)

# use only CMAKE_FIND_ROOT_PATH for searching (find_package)
set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)