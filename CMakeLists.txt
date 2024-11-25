cmake_minimum_required(VERSION 3.21)
include(${CMAKE_ROOT}/Modules/ExternalProject.cmake)
project(PyG2O)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

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
  "src/functions/*.h"
  "src/functions/*.cpp"
	"src/*.h"
	"src/*.cpp"
  "src/events/*.h"
  "src/events/*.cpp"
)

add_library(${PROJECT_NAME} SHARED ${SOURCE})

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
target_link_libraries(${PROJECT_NAME} PRIVATE pybind11::embed)