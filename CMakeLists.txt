cmake_minimum_required(VERSION 3.17)

project(squirrel-template)

file(GLOB SRC
	"src/api/squirrel_api.h"

	"src/api/module_api.h"
	"src/api/module_api.cpp"

	"src/sqmain.cpp"
)

add_library(squirrel-template SHARED ${SRC})

target_compile_definitions(squirrel-template
	PRIVATE
		SCRAT_EXPORT
)

target_include_directories(squirrel-template
	INTERFACE
		"include/"
	PRIVATE
		"src/"
)

add_subdirectory(dependencies)

if(DEFINED OUT_FILE_SUFFIX)
	set_target_properties(squirrel-template
			PROPERTIES 
				PREFIX ""
				SUFFIX ".${OUT_FILE_SUFFIX}${CMAKE_SHARED_LIBRARY_SUFFIX}"
	)
endif()