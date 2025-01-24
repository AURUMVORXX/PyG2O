
add_library(${PYG2O_MODULE_NAME} SHARED
        bind.cpp
)

add_subdirectory(dependencies)
add_subdirectory(NoNut)
add_subdirectory(classes)
add_subdirectory(constants)
add_subdirectory(events)
add_subdirectory(functions)
add_subdirectory(types)

# pybind11 requires to declare all modules before interpretor initializes, so we have to load main.cpp last
target_sources(${PYG2O_MODULE_NAME}
        PRIVATE
                main.cpp
)

if(DEFINED OUT_FILE_SUFFIX)
	set_target_properties(${PYG2O_MODULE_NAME} 
			PROPERTIES 
				PREFIX ""
				SUFFIX ".${OUT_FILE_SUFFIX}${CMAKE_SHARED_LIBRARY_SUFFIX}"
	)
endif()

# Use this code to auto copy module to your server folder for quick testing
# Change paths to your actual paths

# add_custom_command(TARGET ${PYG2O_MODULE_NAME} POST_BUILD
#    COMMAND ${CMAKE_COMMAND} -E copy
#            ${CMAKE_BINARY_DIR}/source/${PYG2O_MODULE_NAME}.${OUT_FILE_SUFFIX}${CMAKE_SHARED_LIBRARY_SUFFIX}
#            C:\\server-windows-x64
#     COMMAND ${CMAKE_COMMAND} -E copy_directory
#            ${CMAKE_SOURCE_DIR}/python/g2o
#            C:\\server-windows-x64\\g2o)