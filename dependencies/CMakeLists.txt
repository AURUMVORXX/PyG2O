add_subdirectory(sqapi)

target_link_libraries(${PROJECT_NAME}
	PRIVATE 
		sqapi
)