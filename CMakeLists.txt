cmake_minimum_required(VERSION 3.17)

project(sqModule)

file(GLOB_RECURSE SRC
	"dependencies/squirrel/include/*.h"
	"dependencies/sqrat/include/*.h"
	"src/sqmodule_api.h"
	"src/sqmodule_api.cpp"
	"src/pch.h"
	"src/sqmain.cpp"
)

add_library(sqModule SHARED ${SRC})
target_precompile_headers(sqModule PRIVATE "src/pch.h")

target_include_directories(sqModule
	INTERFACE
		"include/"
	PRIVATE
		"include/sqModule/"
		"dependencies/squirrel/include/"
		"dependencies/sqrat/include/"
)

if (EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/.game.dir.txt")
	file(READ ".game.dir.txt" GAME_DIR)

	add_custom_command(TARGET sqModule 
		POST_BUILD
			COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:sqModule> ${GAME_DIR}
			COMMAND ${CMAKE_COMMAND} -E echo "[Post Build] $<TARGET_FILE_NAME:sqModule> copied to: ${GAME_DIR}")
endif()

if (EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/.server.dir.txt")
	file(READ ".server.dir.txt" SERVER_DIR)

	add_custom_command(TARGET sqModule 
		POST_BUILD
			COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:sqModule> ${SERVER_DIR}
			COMMAND ${CMAKE_COMMAND} -E echo "[Post Build] $<TARGET_FILE_NAME:sqModule> copied to: ${SERVER_DIR}")
endif()
