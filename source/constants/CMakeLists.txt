
target_sources(${PYG2O_MODULE_NAME}
    PRIVATE
        sqconstants.cpp
)

target_include_directories(${PYG2O_MODULE_NAME}
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/
)