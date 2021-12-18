cmake_minimum_required(VERSION 3.17)

project(SqModule)

option(INSTALL_AFTER_BUILD "Run cmake --install separately for every target after each build. By default this option is set to OFF" OFF)

set(GAME_PATH "" CACHE PATH "This option specifies the game location. It's only used for the installation step.")
set(SERVER_PATH "" CACHE PATH "This option specifies the server location. It's only used for the installation step.")

file(GLOB SRC
	"dependencies/squirrel/include/*.h"
	"dependencies/sqrat/include/*.h"
	"src/api/squirrel_api.h"
	"src/api/module_api.h"
	"src/api/module_api.cpp"
	"src/pch.h"
	"src/sqmain.cpp"
)

add_library(SqModule SHARED ${SRC})
target_precompile_headers(SqModule PRIVATE "src/pch.h")

target_include_directories(SqModule
	INTERFACE
		"include/"
	PRIVATE
		"src/"
		"dependencies/squirrel/include/"
		"dependencies/sqrat/include/"
)

if (NOT ${GAME_PATH} STREQUAL "")
	install(TARGETS SqModule
			RUNTIME
			  DESTINATION ${GAME_PATH}
			  COMPONENT "clientModule"
	)

	if(INSTALL_AFTER_BUILD)
		add_custom_command(TARGET SqModule 
			POST_BUILD
				COMMAND ${CMAKE_COMMAND} --install ${CMAKE_CURRENT_BINARY_DIR} --component "clientModule"
		)
	endif()
endif()

if (NOT ${SERVER_PATH} STREQUAL "")
	install(TARGETS SqModule
			RUNTIME
			  DESTINATION ${SERVER_PATH}
			  COMPONENT "serverModule"
	)

	if(INSTALL_AFTER_BUILD)
		add_custom_command(TARGET SqModule 
			POST_BUILD
				COMMAND ${CMAKE_COMMAND} --install ${CMAKE_CURRENT_BINARY_DIR} --component "serverModule"
		)
	endif()
endif()
