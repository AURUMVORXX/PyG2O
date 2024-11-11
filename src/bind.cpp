#include <pybind11/embed.h>

#include "classes/py/Packet.h"
#include "classes/py/DamageDescription.h"
#include "classes/py/ItemGround.h"
#include "classes/py/Daedalus.h"
#include "classes/py/Sky.h"
#include "classes/py/ItemsGround.h"
#include "classes/py/Mds.h"
#include "classes/py/Way.h"

#include "functions/pyfunctions.h"

#include <NoNut/core/Constant.h>

namespace py = pybind11;

PYBIND11_EMBEDDED_MODULE(sqg2o, m) {
    
    py::class_<PyPacket>(m, "Packet")
        .def(py::init<>())
        .def("reset",                               &PyPacket::reset)
        .def("send",                                &PyPacket::send)
        .def("sendToAll",                           &PyPacket::sendToAll)
        .def("writeInt8",                           &PyPacket::writeInt8)
        .def("writeUInt8",                          &PyPacket::writeUInt8)
        .def("writeInt16",                          &PyPacket::writeInt16)
        .def("writeUInt16",                         &PyPacket::writeUInt16)
        .def("writeInt32",                          &PyPacket::writeInt32)
        .def("writeUInt32",                         &PyPacket::writeUInt32)
        .def("writeFloat",                          &PyPacket::writeFloat)
        .def("writeBool",                           &PyPacket::writeBool)
        .def("writeString",                         &PyPacket::writeString)
        .def("readInt8",                            &PyPacket::readInt8)
        .def("readUInt8",                           &PyPacket::readUInt8)
        .def("readInt16",                           &PyPacket::readInt16)
        .def("readUInt16",                          &PyPacket::readUInt16)
        .def("readInt32",                           &PyPacket::readInt32)
        .def("readUInt32",                          &PyPacket::readUInt32)
        .def("readFloat",                           &PyPacket::readFloat)
        .def("readBool",                            &PyPacket::readBool)
        .def("readString",                          &PyPacket::readString)
        .def("__del__",                             &PyPacket::del)
        
        .def_property_readonly("bitsUsed",          &PyPacket::getBitsUsed)
        .def_property_readonly("bytesUsed",         &PyPacket::getBytesUsed);
        
// -------------------------------------------------------------------------
        
    py::class_<PyDamageDescription>(m, "DamageDescription")
        
        .def_property_readonly("item_instance",     &PyDamageDescription::getItemInstance)
        
        .def_property("flags",                      &PyDamageDescription::getFlags,         &PyDamageDescription::setFlags, py::return_value_policy::reference_internal)
        .def_property("damage",                     &PyDamageDescription::getDamage,        &PyDamageDescription::setDamage, py::return_value_policy::reference_internal)
        .def_property("distance",                   &PyDamageDescription::getDistance,      &PyDamageDescription::setDistance, py::return_value_policy::reference_internal)
        .def_property("spell_id",                   &PyDamageDescription::getSpellId,       &PyDamageDescription::setSpellId, py::return_value_policy::reference_internal)
        .def_property("spell_level",                &PyDamageDescription::getSpellLevel,    &PyDamageDescription::setSpellLevel, py::return_value_policy::reference_internal)
        .def_property("node",                       &PyDamageDescription::getNode,          &PyDamageDescription::setNode, py::return_value_policy::reference_internal);
        
// -------------------------------------------------------------------------

    py::class_<PyItemGround>(m, "ItemGround")
        .def("__del__",                             &PyItemGround::del)
        
        .def("getPosition",                         &PyItemGround::getPosition)
        .def("getRotation",                         &PyItemGround::getRotation)
        
        .def_property_readonly("id",                &PyItemGround::getId)
        .def_property_readonly("instance",          &PyItemGround::getInstance)
        .def_property_readonly("amount",            &PyItemGround::getAmount)
        .def_property_readonly("world",             &PyItemGround::getWorld)
        
        .def_property("virtualWorld",               &PyItemGround::getVirtualWorld,         &PyItemGround::setVirtualWorld, py::return_value_policy::reference_internal);
        
// -------------------------------------------------------------------------

    py::class_<PyDaedalus>(m, "Daedalus")
        .def_static("index",                        [](std::string value){ return PyDaedalus::index(value); })
        .def_static("symbol",                       [](std::string value){ return PyDaedalus::symbol(value); })
        .def_static("instance",                     [](std::string value){ return PyDaedalus::instance(value); });
        
// -------------------------------------------------------------------------

    py::class_<PySky>(m, "Sky")
        .def_property_static("weather",             [](py::object){ return PySky::getWeather(); }, [](py::object, int value) { PySky::setWeather(value); })
        .def_property_static("raining",             [](py::object){ return PySky::getRaining(); }, [](py::object, int value) { PySky::setRaining(value); })
        .def_property_static("renderLightning",     [](py::object){ return PySky::getRenderLightning(); }, [](py::object, int value) { PySky::setRenderLightning(value); })
        .def_property_static("windScale",           [](py::object){ return PySky::getWindScale(); }, [](py::object, int value) { PySky::setWindScale(value); })
        .def_property_static("dontRain",            [](py::object){ return PySky::getDontRain(); }, [](py::object, int value) { PySky::setDontRain(value); })
        
        .def_static("setRainStartTime",             [](int hour, int min){ return PySky::setRainStartTime(hour, min); })
        .def_static("setRainStopTime",              [](int hour, int min){ return PySky::setRainStopTime(hour, min); })
        .def_static("getRainStartTime",             [](){ return PySky::getRainStartTime(); })
        .def_static("getRainStopTime",              [](){ return PySky::getRainStopTime(); });
        
// -------------------------------------------------------------------------

    py::class_<PyItemsGround>(m, "ItemsGround")
    
        .def_static("getById",                      [](int value){ return PyItemsGround::getById(value); })
        .def_static("create",                       [](py::dict value){ return PyItemsGround::create(value); })
        .def_static("destroy",                      [](int value){ return PyItemsGround::destroy(value); });
        
// -------------------------------------------------------------------------

    py::class_<PyMds>(m, "Mds")
    
        .def_static("id",                           [](std::string value){ return PyMds::id(value); })
        .def_static("name",                         [](int value){ return PyMds::name(value); });

// -------------------------------------------------------------------------

    py::class_<PyWay>(m, "Way")
        
        .def(py::init<std::string, std::string, std::string>())
        .def("getWaypoints",                        &PyWay::getWaypoints)
        .def("getCountWaypoints",                   &PyWay::getCountWaypoints)
        .def("__del__",                             &PyWay::del)
        
        .def_property_readonly("start",             &PyWay::getStart)
        .def_property_readonly("end",               &PyWay::getEnd);
    
// -------------------------------------------------------------------------

    m.def("getHostname",            &py_getHostname);
    m.def("getMaxSlots",            &py_getMaxSlots);
    m.def("getPlayersCount",        &py_getPlayersCount);
    
    m.def("getDistance2d",          &py_getDistance2d);
    m.def("getDistance3d",          &py_getDistance3d);
    m.def("getVectorAngle",         &py_getVectorAngle);
    
    m.def("exit",                   &py_exit, py::arg() = 0);
    m.def("getDayLength",           &py_getDayLength);
    m.def("getServerDescription",   &py_getServerDescription);
    m.def("getServerWorld",         &py_getServerWorld);
    m.def("getTime",                &py_getTime);
    m.def("serverLog",              &py_serverLog);
    m.def("setDayLength",           &py_setDayLength);
    m.def("setServerDescription",   &py_setServerDescription);
    m.def("setServerWorld",         &py_setServerWorld);
    m.def("setTime",                &py_setTime, py::arg(), py::arg(), py::arg() = 0);
    
    m.def("clearNpcActions",        &py_clearNpcActions);
    m.def("createNpc",              &py_createNpc, py::arg(), py::arg() = "PC_HERO");
    m.def("destroyNpc",             &py_destroyNpc);
    m.def("getNpcAction",           &py_getNpcAction);
    // m.def("getNpcActionType",    &py_getNpcActionType);
    m.def("getNpcActtions",         &py_getNpcActions);
    m.def("getNpcActtionsCount",    &py_getNpcActionsCount);
    m.def("getNpcHostPlayer",       &py_getNpcHostPlayer);
    m.def("getNpcLastActionId",     &py_getNpcLastActionId);
    m.def("isNpc",                  &py_isNpc);
    m.def("isNpcActionFinished",    &py_isNpcActionFinished);
    m.def("npcAttackMelee",         &py_npcAttackMelee);
    m.def("npcAttackRanged",        &py_npcAttackRanged);
    m.def("npcSpellCast",           &py_npcSpellCast);
    m.def("npcUseClosestMob",       &py_npcUseClosestMob);
    // m.def("pushNpcAction",       &py_pushNpcAction);
    m.def("setNpcHostPlayer",       &py_setNpcHostPlayer);
    
    m.def("sendMessageToAll",       &py_sendMessageToAll);
    m.def("sendMessageToPlayer",    &py_sendMessageToPlayer);
    m.def("sendPlayerMessageToAll", &py_sendPlayerMessageToAll);
    m.def("sendPlayerMessageToPlayer", &py_sendPlayerMessageToPlayer);
    
	m.def("addBan",	                &py_addBan);
	m.def("applyPlayerOverlay",	    &py_applyPlayerOverlay);
	m.def("ban",	                &py_ban, py::arg(), py::arg() = 0, py::arg());
	m.def("drawWeapon",	            &py_drawWeapon);
	m.def("equipItem",	            &py_equipItem, py::arg(), py::arg(), py::arg() = -1);
	m.def("getPlayerAmulet",	    &py_getPlayerAmulet);
	m.def("getPlayerAngle",	        &py_getPlayerAngle);
	m.def("getPlayerAni",	        &py_getPlayerAni);
	m.def("getPlayerArmor",	        &py_getPlayerArmor);
	m.def("getPlayerAtVector",	    &py_getPlayerAtVector);
	m.def("getPlayerBelt",	        &py_getPlayerBelt);
	m.def("getPlayerCameraPosition",&py_getPlayerCameraPosition);
	m.def("getPlayerCollision",	    &py_getPlayerCollision);
	m.def("getPlayerColor",	        &py_getPlayerColor);
	m.def("getPlayerContext",	    &py_getPlayerContext);
	m.def("getPlayerDexterity",	    &py_getPlayerDexterity);
	m.def("getPlayerFaceAnis",	    &py_getPlayerFaceAnis);
	m.def("getPlayerFatness",	    &py_getPlayerFatness);
	m.def("getPlayerFocus",	        &py_getPlayerFocus);
	m.def("getPlayerHealth",	    &py_getPlayerHealth);
	m.def("getPlayerHelmet",	    &py_getPlayerHelmet);
	m.def("getPlayerIP",	        &py_getPlayerIP);
	m.def("getPlayerInstance",	    &py_getPlayerInstance);
	m.def("getPlayerMacAddr",	    &py_getPlayerMacAddr);
	m.def("getPlayerMana",	        &py_getPlayerMana);
	m.def("getPlayerMaxHealth", 	&py_getPlayerMaxHealth);
	m.def("getPlayerMaxMana",	    &py_getPlayerMaxMana);
	m.def("getPlayerMeleeWeapon",	&py_getPlayerMeleeWeapon);
	m.def("getPlayerName",	        &py_getPlayerName);
	m.def("getPlayerPing",	        &py_getPlayerPing);
	m.def("getPlayerPosition",	    &py_getPlayerPosition);
	m.def("getPlayerRangedWeapon",	&py_getPlayerRangedWeapon);
	m.def("getPlayerRespawnTime",	&py_getPlayerRespawnTime);
	m.def("getPlayerRing",	        &py_getPlayerRing);
	m.def("getPlayerScale",	        &py_getPlayerScale);
	m.def("getPlayerSerial",	    &py_getPlayerSerial);
	m.def("getPlayerShield",	    &py_getPlayerShield);
	m.def("getPlayerSkillWeapon",	&py_getPlayerSkillWeapon);
	m.def("getPlayerSpell",	        &py_getPlayerSpell);
	m.def("getPlayerStrength",	    &py_getPlayerStrength);
	m.def("getPlayerTalent",	    &py_getPlayerTalent);
	m.def("getPlayerVirtualWorld",	&py_getPlayerVirtualWorld);
	m.def("getPlayerVisual",	    &py_getPlayerVisual);
	m.def("getPlayerWeaponMode",	&py_getPlayerWeaponMode);
	m.def("getPlayerWorld",	        &py_getPlayerWorld);
	m.def("giveItem",	            &py_giveItem);
	m.def("hitPlayer",	            &py_hitPlayer);
	m.def("isPlayerConnected",	    &py_isPlayerConnected);
	m.def("isPlayerDead",	        &py_isPlayerDead);
	m.def("isPlayerUnconscious",	&py_isPlayerUnconscious);
	m.def("kick",	                &py_kick);
	m.def("playAni",	            &py_playAni);
	m.def("playFaceAni",	        &py_playFaceAni);
	m.def("readySpell",         	&py_readySpell);
	m.def("removeItem",	            &py_removeItem);
	m.def("removePlayerOverlay",	&py_removePlayerOverlay);
	m.def("removeWeapon",	        &py_removeWeapon);
	m.def("respawnPlayer",	        &py_respawnPlayer);
	m.def("setPlayerAngle",	        &py_setPlayerAngle);
	m.def("setPlayerCollision",	    &py_setPlayerCollision);
	m.def("setPlayerColor",	        &py_setPlayerColor);
	m.def("setPlayerContext",	    &py_setPlayerContext);
	m.def("setPlayerDexterity", 	&py_setPlayerDexterity);
	m.def("setPlayerFatness",	    &py_setPlayerFatness);
	m.def("setPlayerHealth",	    &py_setPlayerHealth);
	m.def("setPlayerInstance",	    &py_setPlayerInstance);
	m.def("setPlayerInvisible",	    &py_setPlayerInvisible);
	m.def("setPlayerMana",	        &py_setPlayerMana);
	m.def("setPlayerMaxHealth",	    &py_setPlayerMaxHealth);
	m.def("setPlayerMaxMana",	    &py_setPlayerMaxMana);
	m.def("setPlayerName",	        &py_setPlayerName);
	m.def("setPlayerPosition",	    &py_setPlayerPosition);
	m.def("setPlayerRespawnTime",	&py_setPlayerRespawnTime);
	m.def("setPlayerScale",	        &py_setPlayerScale);
	m.def("setPlayerSkillWeapon",	&py_setPlayerSkillWeapon);
	m.def("setPlayerStrength",	    &py_setPlayerStrength);
	m.def("setPlayerTalent",	    &py_setPlayerTalent);
	m.def("setPlayerVirtualWorld",	&py_setPlayerVirtualWorld);
	m.def("setPlayerVisual",	    &py_setPlayerVisual);
	m.def("setPlayerWeaponMode",	&py_setPlayerWeaponMode);
	m.def("setPlayerWorld",	        &py_setPlayerWorld);
	m.def("spawnPlayer",	        &py_spawnPlayer);
	m.def("stopAni",	            &py_stopAni, py::arg(), py::arg() = "");
	m.def("stopFaceAni",	        &py_stopFaceAni, py::arg(), py::arg() = "");
	m.def("unequipItem",	        &py_unequipItem);
	m.def("unreadySpell",	        &py_unreadySpell);
	m.def("unspawnPlayer",	        &py_unspawnPlayer);
	m.def("useItem",	            &py_useItem);
	m.def("useItemToState",	        &py_useItemToState);
    
    m.def("findNearbyPlayers",          &py_findNearbyPlayers);
    m.def("getSpawnedPlayersForPlayer", &py_getSpawnedPlayersForPlayer);
    m.def("getStreamedPlayersByPlayer", &py_getStreamedPlayersByPlayer);
    
    m.def("getNearestWaypoint",         &py_getNearestWaypoint);
    m.def("getWaypoint",                &py_getWaypoint);
}