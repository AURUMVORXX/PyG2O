

target_sources(${PYG2O_MODULE_NAME}
    PRIVATE
        sqevents.cpp
        sqevents_anticheat.cpp
        sqevents_general.cpp
        sqevents_network.cpp
        sqevents_npc.cpp
        sqevents_player.cpp
)

target_include_directories(${PYG2O_MODULE_NAME}
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/
)