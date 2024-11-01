add_subdirectory(sqapi)
add_subdirectory(pybind11)

target_link_libraries(${PROJECT_NAME}
	PRIVATE 
		sqapi
)