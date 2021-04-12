cmake_minimum_required(VERSION 3.17)

project(SqModule)

file(GLOB_RECURSE SRC
	"dependencies/squirrel/include/*.h"
	"dependencies/sqrat/include/*.h"
	"src/sqmodule_api.h"
	"src/sqmodule_api.cpp"
	"src/pch.h"
	"src/sqmain.cpp"
)

add_library(SqModule SHARED ${SRC})
target_precompile_headers(SqModule PRIVATE "src/pch.h")

target_include_directories(SqModule
	INTERFACE
		"include/"
	PRIVATE
		"include/sqModule/"
		"dependencies/squirrel/include/"
		"dependencies/sqrat/include/"
)

if (EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/.game.dir.txt")
	file(READ ".game.dir.txt" GAME_DIR)

	add_custom_command(TARGET SqModule 
		POST_BUILD
			COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:SqModule> ${GAME_DIR}
			COMMAND ${CMAKE_COMMAND} -E echo "[Post Build] $<TARGET_FILE_NAME:SqModule> copied to: ${GAME_DIR}")
endif()

if (EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/.server.dir.txt")
	file(READ ".server.dir.txt" SERVER_DIR)

	add_custom_command(TARGET SqModule 
		POST_BUILD
			COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:SqModule> ${SERVER_DIR}
			COMMAND ${CMAKE_COMMAND} -E echo "[Post Build] $<TARGET_FILE_NAME:SqModule> copied to: ${SERVER_DIR}")
endif()
