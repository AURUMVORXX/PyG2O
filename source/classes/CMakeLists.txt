
target_sources(${PYG2O_MODULE_NAME}
    PRIVATE
        squirrel/Daedalus.cpp
        squirrel/DamageDescription.cpp
        squirrel/ItemGround.cpp
        squirrel/ItemsGround.cpp
        squirrel/Mds.cpp
        squirrel/Packet.cpp
        squirrel/Sky.cpp
        squirrel/Way.cpp
)

target_include_directories(${PYG2O_MODULE_NAME}
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/
)