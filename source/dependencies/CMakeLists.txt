add_subdirectory(sqapi)
add_subdirectory(pybind11)

target_link_libraries(${PYG2O_MODULE_NAME}
	PRIVATE 
		sqapi
		pybind11::embed
)

target_compile_definitions(${PYG2O_MODULE_NAME}
	PRIVATE
		SCRAT_EXPORT
)