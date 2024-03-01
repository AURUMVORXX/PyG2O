cmake_minimum_required(VERSION 3.21)

project(squirrel-template)

file(GLOB_RECURSE SRC
	"include/*.h"

	"src/*.h"
	"src/*.cpp"
)

add_library(${PROJECT_NAME} SHARED ${SRC})

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

add_subdirectory(dependencies)

if(DEFINED OUT_FILE_SUFFIX)
	set_target_properties(${PROJECT_NAME}
			PROPERTIES 
				PREFIX ""
				SUFFIX ".${OUT_FILE_SUFFIX}${CMAKE_SHARED_LIBRARY_SUFFIX}"
	)
endif()