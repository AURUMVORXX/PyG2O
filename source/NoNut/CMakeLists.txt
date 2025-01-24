
target_sources(${PYG2O_MODULE_NAME}
    PRIVATE
        source/Array.cpp
        source/Class.cpp
        source/Constant.cpp
        source/CustomTypes.cpp
        source/StaticClass.cpp
)
    
target_include_directories(${PYG2O_MODULE_NAME}
    PRIVATE
        "include/"
)