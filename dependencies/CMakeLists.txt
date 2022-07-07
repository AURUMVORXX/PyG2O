add_subdirectory(squirrel)
add_subdirectory(sqrat)

target_link_libraries(SqModule PUBLIC Squirrel)
target_link_libraries(SqModule PUBLIC SqRat)