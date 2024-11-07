cmake_minimum_required(VERSION 3.21)
include(${CMAKE_ROOT}/Modules/ExternalProject.cmake)
project(PyG2O)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

# Specify build type
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE "Debug")
endif()
set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "RelWithDebInfo" "MinSizeRel")

if (CMAKE_BUILD_TYPE MATCHES "Debug")
  set(CPYTHON_BUILD_TYPE Debug)
else ()
  set(CPYTHON_BUILD_TYPE Release)
endif()

# Add the cpython as an external project that will be included in the build
if(MSVC)
  if(CMAKE_CL_64)
    set(CPYTHON_PLATFORM x64)
    set(CPYTHON_BUILD_DIR amd64)
  else()
    set(CPYTHON_PLATFORM x86)
    set(CPYTHON_BUILD_DIR win32)
  endif()
  ExternalProject_Add(CPYTHON
    DOWNLOAD_COMMAND ""
    SOURCE_DIR ${CMAKE_SOURCE_DIR}/dependencies/cpython
    CONFIGURE_COMMAND ""
    BUILD_COMMAND cd ${CMAKE_SOURCE_DIR}/dependencies/cpython && MSBuild.exe /p:Configuration=${CPYTHON_BUILD_TYPE} /property:Platform=${CPYTHON_PLATFORM} "PCBuild/python.vcxproj" /nologo /verbosity:minimal /consoleloggerparameters:summar
    INSTALL_COMMAND ""
    TEST_COMMAND ""
  )
else()
  ExternalProject_Add(CPYTHON
    DOWNLOAD_COMMAND ""
    SOURCE_DIR ${CMAKE_SOURCE_DIR}/dependencies/cpython
    CONFIGURE_COMMAND cd ${CMAKE_SOURCE_DIR}/dependencies/cpython && ./configure --disable-static --enable-shared 
    BUILD_COMMAND cd ${CMAKE_SOURCE_DIR}/dependencies/cpython && make
    INSTALL_COMMAND ""
    TEST_COMMAND ""
  )
endif()

set(CPYTHON_STDLIB_DIR ${CMAKE_SOURCE_DIR}/dependencies/cpython/Lib)
if(MSVC)
  set(CPYTHON_INCLUDE_DIR ${CMAKE_SOURCE_DIR}/dependencies/cpython/Include ${CMAKE_SOURCE_DIR}/dependencies/cpython/PC)
  set(CPYTHON_LIBRARY_DIR ${CMAKE_SOURCE_DIR}/dependencies/cpython/PCBuild/${CPYTHON_BUILD_DIR})
  if(CMAKE_BUILD_TYPE MATCHES "Debug")
    set(CPYTHON_BIN ${CMAKE_SOURCE_DIR}/dependencies/cpython/PCBuild/${CPYTHON_BUILD_DIR}/python312_d.dll)
  else()
    set(CPYTHON_BIN ${CMAKE_SOURCE_DIR}/dependencies/cpython/PCBuild/${CPYTHON_BUILD_DIR}/python312.dll)
  endif()
else()
  set(CPYTHON_INCLUDE_DIR ${CMAKE_SOURCE_DIR}/dependencies/cpython/Include ${CMAKE_SOURCE_DIR}/dependencies/cpython)
  set(CPYTHON_LIBRARY_DIR ${CMAKE_SOURCE_DIR}/dependencies/cpython)
  set(CPYTHON_LIBRARY python3.12m)
  set(CPYTHON_BIN ${CMAKE_SOURCE_DIR}/dependencies/dependencies/libpython3.12m.so)
endif()

file(GLOB_RECURSE SOURCE
	"include/*.h"
  
  "src/NoNut/core/*.h"
  "src/NoNut/core/*.cpp"
  "src/classes/*.h"
  "src/classes/*.cpp"
  "src/classes/sq/*.h"
  "src/classes/sq/*.cpp"
  "src/classes/py/*.h"
  "src/classes/py/*.cpp"
  "src/constants/*.h"
  "src/constants/*.cpp"
	"src/*.h"
	"src/*.cpp"
  "src/events/*.h"
  "src/events/*.cpp"
)

# Linking directories
link_directories(${CPYTHON_LIBRARY_DIR})

add_library(${PROJECT_NAME} SHARED ${SOURCE})

# Dependencies
add_dependencies(${PROJECT_NAME} CPYTHON)

target_compile_definitions(${PROJECT_NAME}
	PRIVATE
		SCRAT_EXPORT
)

target_include_directories(${PROJECT_NAME}
	INTERFACE
		"include/"
	PRIVATE
		"src/"
)

if(DEFINED OUT_FILE_SUFFIX)
	set_target_properties(${PROJECT_NAME}
			PROPERTIES 
				PREFIX ""
				SUFFIX ".${OUT_FILE_SUFFIX}${CMAKE_SHARED_LIBRARY_SUFFIX}"
	)
endif()

add_subdirectory(dependencies)
target_link_libraries(${PROJECT_NAME} ${CPYTHON_LIBRARY})
target_link_libraries(${PROJECT_NAME} PRIVATE pybind11::embed)

# Copy Python DLL to the build folder if different
add_custom_command(
  TARGET ${PROJECT_NAME}
  POST_BUILD
  COMMAND ${CMAKE_COMMAND}
  -E copy_if_different ${CPYTHON_BIN} $<TARGET_FILE_DIR:${PROJECT_NAME}>
)

# Copy the Python stdlib into the build folder (needed by the embedded python)
add_custom_command(
  TARGET ${PROJECT_NAME} 
  POST_BUILD
  COMMAND ${CMAKE_COMMAND} 
  -E copy_directory ${CPYTHON_STDLIB_DIR} $<TARGET_FILE_DIR:${PROJECT_NAME}>/lib
)

# Copy the PyG2O library into the build/lib folder
add_custom_command(
  TARGET ${PROJECT_NAME} 
  POST_BUILD
  COMMAND ${CMAKE_COMMAND} 
  -E copy_directory ${CMAKE_SOURCE_DIR}/g2o $<TARGET_FILE_DIR:${PROJECT_NAME}>/lib/g2o
)