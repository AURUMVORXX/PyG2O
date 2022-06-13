# Simple toolchain file for compiling under windows
# Usage: cmake .. -DCMAKE_TOOLCHAIN_FILE=windows-x64.cmake

# specify the target system properties
set(CMAKE_SYSTEM_NAME Windows)
set(CMAKE_GENERATOR_PLATFORM x64 CACHE INTERNAL "")

# specify shared library suffix
set(SHARED_LIBRARY_SUFFIX ${CMAKE_GENERATOR_PLATFORM})
