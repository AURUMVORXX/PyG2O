#include <sqapi.h>
#include <pybind11/embed.h>
#include "pyfunctions.h"
#include "sqfunctions.h"
#include "classes/Dictionary.h"
#include <NoNut/core/CustomTypes.h>
namespace py = pybind11;
#define SERVERFUNC nonut::ServerFunctions::getInstance()

std::string py_getHostname()                                                                     { return SERVERFUNC->getHostname(); }
int         py_getMaxSlots()                                                                     { return SERVERFUNC->getMaxSlots(); }
int         py_getPlayersCount()                                                                 { return SERVERFUNC->getPlayersCount(); }

float       py_getDistance2d(float x1, float y1, float x2, float y2)                             { return SERVERFUNC->getDistance2d(x1, y1, x2, y2); }
float       py_getDistance3d(float x1, float y1, float z1, float x2, float y2, float z2)         { return SERVERFUNC->getDistance3d(x1, y1, z1, x2, y2, z2); }
float       py_getVectorAngle(float x1, float y1, float x2, float y2)                            { return SERVERFUNC->getVectorAngle(x1, y1, x2, y2); }

void        py_sendMessageToAll(int r, int g, int b, std::string text)                           { return SERVERFUNC->sendMessageToAll(r, g, b, text); }
void        py_sendMessageToPlayer(int id, int r, int g, int b, std::string text)                { return SERVERFUNC->sendMessageToPlayer(id, r, g, b, text); }
void        py_sendPlayerMessageToAll(int id, int r, int g, int b, std::string text)             { return SERVERFUNC->sendPlayerMessageToAll(id, r, g, b, text); }
void        py_sendPlayerMessageToPlayer(int id, int to, int r, int g, int b, std::string text)  { return SERVERFUNC->sendPlayerMessageToPlayer(id, to, r, g, b, text); }

void        py_exit(int code)                                                                    { return SERVERFUNC->exit(code); }
float       py_getDayLength()                                                                    { return SERVERFUNC->getDayLength(); }
std::string py_getServerDescription()                                                            { return SERVERFUNC->getServerDescription(); }
std::string py_getServerWorld()                                                                  { return SERVERFUNC->getServerWorld(); }
py::dict    py_getTime()                                                                         { return SERVERFUNC->getTime().data; }
void        py_serverLog(std::string text)                                                       { return SERVERFUNC->serverLog(text); }
void        py_setDayLength(float ms)                                                            { return SERVERFUNC->setDayLength(ms); }
bool        py_setServerDescription(std::string text)                                            { return SERVERFUNC->setServerDescription(text); }
void        py_setServerWorld(std::string text)                                                  { return SERVERFUNC->setServerWorld(text); }
void        py_setTime(int h, int m, int d)                                                      { return SERVERFUNC->setTime(h, m, d); }

void        py_clearNpcActions(int npc_id)                                                       { return SERVERFUNC->clearNpcActions(npc_id); }
int         py_createNpc(std::string name, std::string instance)                                 { return SERVERFUNC->createNpc(name, instance); }
bool        py_destroyNpc(int npc_id)                                                            { return SERVERFUNC->destroyNpc(npc_id); }
py::dict    py_getNpcAction(int npc_id, int index)                                               { return SERVERFUNC->getNpcAction(npc_id, index).data; }
// ??? py_getNpcActionType
py::list    py_getNpcActions(int npc_id)                                                         { return SERVERFUNC->getNpcActions(npc_id).data; }
int         py_getNpcActionsCount(int npc_id)                                                    { return SERVERFUNC->getNpcActionsCount(npc_id); }
int         py_getNpcHostPlayer(int npc_id)                                                      { return SERVERFUNC->getNpcHostPlayer(npc_id); }
int         py_getNpcLastActionId(int npc_id)                                                    { return SERVERFUNC->getNpcLastActionId(npc_id); }
bool        py_isNpc(int npc_id)                                                                 { return SERVERFUNC->isNpc(npc_id); }
bool        py_isNpcActionFinished(int npc_id, int action_id)                                    { return SERVERFUNC->isNpcActionFinished(npc_id, action_id); }
void        py_npcAttackMelee(int a_id, int e_id, int a_type, int combo)                         { return SERVERFUNC->npcAttackMelee(a_id, e_id, a_type, combo); }
void        py_npcAttackRanged(int a_id, int e_id)                                               { return SERVERFUNC->npcAttackRanged(a_id, e_id); }
void        py_npcSpellCast(int a_id, int e_id)                                                  { return SERVERFUNC->npcSpellCast(a_id, e_id); }
void        py_npcUseClosestMob(int npc_id, std::string sceme, int target_state)                 { return SERVERFUNC->npcUseClosestMob(npc_id, sceme, target_state); }
//??? py_pushNpcAction
bool        py_setNpcHostPlayer(int npc_id, int host_id)                                         { return SERVERFUNC->setNpcHostPlayer(npc_id, host_id); }

bool        py_addBan(py::dict info)                                                             
{ 
    Sqrat::Table* pTable    = PyDictionary::toSqObject(info); 
    nonut::Int result       = SERVERFUNC->addBan(pTable->GetObject());
    delete pTable;
    return result;
}
bool        py_applyPlayerOverlay(int id, int overlayId)                                         { return SERVERFUNC->applyPlayerOverlay(id, overlayId); }
void        py_ban(int id, int minutes, std::string reason)                                      { return SERVERFUNC->ban(id, minutes, reason); }
void        py_drawWeapon(int id, int weaponMode)                                                { return SERVERFUNC->drawWeapon(id, weaponMode); }
void        py_equipItem(int id, std::string instance, int slotId)                               { return SERVERFUNC->equipItem(id, instance, slotId); }
std::string py_getPlayerAmulet(int id)                                                           { return SERVERFUNC->getPlayerAmulet(id); }
float       py_getPlayerAngle(int id)                                                            { return SERVERFUNC->getPlayerAngle(id); }
std::string py_getPlayerAni(int id)                                                              { return SERVERFUNC->getPlayerAni(id); }
std::string py_getPlayerArmor(int id)                                                            { return SERVERFUNC->getPlayerArmor(id); }
py::dict    py_getPlayerAtVector(int id)                                                         
{ 
    py::dict result;
    nonut::Position3d pos = SERVERFUNC->getPlayerAtVector(id);
    
    result["x"] = pos.x;
    result["y"] = pos.y;
    result["z"] = pos.z;
    return result;
}
std::string py_getPlayerBelt(int id)                                                             { return SERVERFUNC->getPlayerBelt(id); }
py::dict    py_getPlayerCameraPosition(int id)                                                   
{ 
    py::dict result;
    nonut::Position3d pos = SERVERFUNC->getPlayerCameraPosition(id);
    
    result["x"] = pos.x;
    result["y"] = pos.y;
    result["z"] = pos.z;
    return result;
}
bool        py_getPlayerCollision(int id)                                                        { return SERVERFUNC->getPlayerCollision(id); }
py::dict    py_getPlayerColor(int id)
{ 
    py::dict result;
    nonut::Color color = SERVERFUNC->getPlayerColor(id);
    
    result["r"] = color.r;
    result["g"] = color.g;
    result["b"] = color.b;
    return result;
}
int         py_getPlayerContext(int id, int type)                                                { return SERVERFUNC->getPlayerContext(id, type); }
int         py_getPlayerDexterity(int id)                                                        { return SERVERFUNC->getPlayerDexterity(id); }
py::list    py_getPlayerFaceAnis(int id)                                                         { return SERVERFUNC->getPlayerFaceAnis(id).data; }
float       py_getPlayerFatness(int id)                                                          { return SERVERFUNC->getPlayerFatness(id); }
int         py_getPlayerFocus(int id)                                                            { return SERVERFUNC->getPlayerFocus(id); }
int         py_getPlayerHealth(int id)                                                           { return SERVERFUNC->getPlayerHealth(id); }
std::string py_getPlayerHelmet(int id)                                                           { return SERVERFUNC->getPlayerHelmet(id); }
std::string py_getPlayerIP(int id)                                                               { return SERVERFUNC->getPlayerIP(id); }
std::string py_getPlayerInstance(int id)                                                         { return SERVERFUNC->getPlayerInstance(id); }
std::string py_getPlayerMacAddr(int id)                                                          { return SERVERFUNC->getPlayerMacAddr(id); }
int         py_getPlayerMana(int id)                                                             { return SERVERFUNC->getPlayerMana(id); }
int         py_getPlayerMaxHealth(int id)                                                        { return SERVERFUNC->getPlayerMaxHealth(id); }
int         py_getPlayerMaxMana(int id)                                                          { return SERVERFUNC->getPlayerMaxMana(id); }
std::string py_getPlayerMeleeWeapon(int id)                                                      { return SERVERFUNC->getPlayerMeleeWeapon(id); }
std::string py_getPlayerName(int id)                                                             { return SERVERFUNC->getPlayerName(id); }
int         py_getPlayerPing(int id)                                                             { return SERVERFUNC->getPlayerPing(id); }
py::dict    py_getPlayerPosition(int id)                                                         
{ 
    py::dict result;
    
    nonut::Position3d pos = SERVERFUNC->getPlayerPosition(id);
    
    result["x"] = pos.x;
    result["y"] = pos.y;
    result["z"] = pos.z;
    return result;
}
std::string py_getPlayerRangedWeapon(int id)                                                     { return SERVERFUNC->getPlayerRangedWeapon(id); }
int         py_getPlayerRespawnTime(int id)                                                      { return SERVERFUNC->getPlayerRespawnTime(id); }
std::string py_getPlayerRing(int id, int handId)                                                 { return SERVERFUNC->getPlayerRing(id, handId); }
py::dict    py_getPlayerScale(int id)                                                            { return SERVERFUNC->getPlayerScale(id).data; }
std::string py_getPlayerSerial(int id)                                                           { return SERVERFUNC->getPlayerSerial(id); }
std::string py_getPlayerShield(int id)                                                           { return SERVERFUNC->getPlayerShield(id); }
int         py_getPlayerSkillWeapon(int id, int skillId)                                         { return SERVERFUNC->getPlayerSkillWeapon(id, skillId); }
std::string py_getPlayerSpell(int id, int slotId)                                                { return SERVERFUNC->getPlayerSpell(id, slotId); }
int         py_getPlayerStrength(int id)                                                         { return SERVERFUNC->getPlayerStrength(id); }
int         py_getPlayerTalent(int id, int talentId)                                             { return SERVERFUNC->getPlayerTalent(id, talentId); }
int         py_getPlayerVirtualWorld(int id)                                                     { return SERVERFUNC->getPlayerVirtualWorld(id); }
py::dict    py_getPlayerVisual(int id)                                                           { return SERVERFUNC->getPlayerVisual(id).data; }
int         py_getPlayerWeaponMode(int id)                                                       { return SERVERFUNC->getPlayerWeaponMode(id); }
std::string py_getPlayerWorld(int id)                                                            { return SERVERFUNC->getPlayerWorld(id); }
void        py_giveItem(int id, std::string instance, int amount)                                { return SERVERFUNC->giveItem(id, instance, amount); }
bool        py_hitPlayer(int id, int targetid)                                                   { return SERVERFUNC->hitPlayer(id, targetid); }
bool        py_isPlayerConnected(int id)                                                         { return SERVERFUNC->isPlayerConnected(id); }
bool        py_isPlayerDead(int id)                                                              { return SERVERFUNC->isPlayerDead(id); }
bool        py_isPlayerUnconscious(int id)                                                       { return SERVERFUNC->isPlayerUnconscious(id); }
void        py_kick(int id, std::string reason)                                                  { return SERVERFUNC->kick(id, reason); }
void        py_playAni(int id, std::string aniName)                                              { return SERVERFUNC->playAni(id, aniName); }
void        py_playFaceAni(int id, std::string aniName)                                          { return SERVERFUNC->playFaceAni(id, aniName); }
void        py_readySpell(int id, int slotId, int manaInvested)                                  { return SERVERFUNC->readySpell(id, slotId, manaInvested); }
void        py_removeItem(int id, std::string instance, int amount)                              { return SERVERFUNC->removeItem(id, instance, amount); }
bool        py_removePlayerOverlay(int id, int overlayId)                                        { return SERVERFUNC->removePlayerOverlay(id, overlayId); }
void        py_removeWeapon(int id)                                                              { return SERVERFUNC->removeWeapon(id); }
void        py_respawnPlayer(int id)                                                             { return SERVERFUNC->respawnPlayer(id); }
void        py_setPlayerAngle(int id, float angle)                                               { return SERVERFUNC->setPlayerAngle(id, angle); }
void        py_setPlayerCollision(int id, bool collision)                                        { return SERVERFUNC->setPlayerCollision(id, collision); }
void        py_setPlayerColor(int id, int r, int g, int b)                                       { return SERVERFUNC->setPlayerColor(id, r, g, b); }
void        py_setPlayerContext(int id, int type, int value)                                     { return SERVERFUNC->setPlayerContext(id, type, value); }
void        py_setPlayerDexterity(int id, int dexterity)                                         { return SERVERFUNC->setPlayerDexterity(id, dexterity); }
void        py_setPlayerFatness(int id, float fatness)                                           { return SERVERFUNC->setPlayerFatness(id, fatness); }
void        py_setPlayerHealth(int id, int health)                                               { return SERVERFUNC->setPlayerHealth(id, health); }
void        py_setPlayerInstance(int id, std::string instance)                                   { return SERVERFUNC->setPlayerInstance(id, instance); }
void        py_setPlayerInvisible(int id, bool toggle)                                           { return SERVERFUNC->setPlayerInvisible(id, toggle); }
void        py_setPlayerMana(int id, int mana)                                                   { return SERVERFUNC->setPlayerMana(id, mana); }
void        py_setPlayerMaxHealth(int id, int maxHealth)                                         { return SERVERFUNC->setPlayerMaxHealth(id, maxHealth); }
void        py_setPlayerMaxMana(int id, int maxMana)                                             { return SERVERFUNC->setPlayerMaxMana(id, maxMana); }
void        py_setPlayerName(int id, std::string name)                                           { return SERVERFUNC->setPlayerName(id, name); }
void        py_setPlayerPosition(int id, float x, float y, float z)                              { return SERVERFUNC->setPlayerPosition(id, x, y, z); }
void        py_setPlayerRespawnTime(int id, int respawnTime)                                     { return SERVERFUNC->setPlayerRespawnTime(id, respawnTime); }
void        py_setPlayerScale(int id, float x, float y, float z)                                 { return SERVERFUNC->setPlayerScale(id, x, y, z); }
void        py_setPlayerSkillWeapon(int id, int skillId, int percentage)                         { return SERVERFUNC->setPlayerSkillWeapon(id, skillId, percentage); }
void        py_setPlayerStrength(int id, int strength)                                           { return SERVERFUNC->setPlayerStrength(id, strength); }
void        py_setPlayerTalent(int id, int talentId, int talentValue)                            { return SERVERFUNC->setPlayerTalent(id, talentId, talentValue); }
void        py_setPlayerVirtualWorld(int id, int virtualWorld)                                   { return SERVERFUNC->setPlayerVirtualWorld(id, virtualWorld); }
void        py_setPlayerVisual(int id, std::string bMdl, int bTxt, std::string hMdl, int hTxt)   { return SERVERFUNC->setPlayerVisual(id, bMdl, bTxt, hMdl, hTxt); }
void        py_setPlayerWeaponMode(int id, int weaponMode)                                       { return SERVERFUNC->setPlayerWeaponMode(id, weaponMode); }
void        py_setPlayerWorld(int id, std::string world, std::string startPointName)             { return SERVERFUNC->setPlayerWorld(id, world, startPointName); }
void        py_spawnPlayer(int id)                                                               { return SERVERFUNC->spawnPlayer(id); }
void        py_stopAni(int id, std::string aniName)                                              { return SERVERFUNC->stopAni(id, aniName); }
void        py_stopFaceAni(int id, std::string aniName)                                          { return SERVERFUNC->stopFaceAni(id, aniName); }
void        py_unequipItem(int id, std::string instance)                                         { return SERVERFUNC->unequipItem(id, instance); }
void        py_unreadySpell(int id)                                                              { return SERVERFUNC->unreadySpell(id); }
void        py_unspawnPlayer(int id)                                                             { return SERVERFUNC->unspawnPlayer(id); }
void        py_useItem(int id, std::string instance)                                             { return SERVERFUNC->useItem(id, instance); }
void        py_useItemToState(int id, std::string instance, int state)                           { return SERVERFUNC->useItemToState(id, instance, state); }

py::list    py_findNearbyPlayers(py::dict position, int radius, std::string world, int vWorld)   
{ 
    Sqrat::Table* pTable    = PyDictionary::toSqObject(position);
    py::list result         = SERVERFUNC->findNearbyPlayers(pTable->GetObject(), radius, world, vWorld).data;
    delete pTable;
    return result;
}
py::list    py_getSpawnedPlayersForPlayer(int id)                                                { return SERVERFUNC->getSpawnedPlayersForPlayer(id).data; }
py::list    py_getStreamedPlayersByPlayer(int id)                                                { return SERVERFUNC->getStreamedPlayersByPlayer(id).data; }
py::dict    py_getNearestWaypoint(std::string world, int x, int y, int z)                        { return SERVERFUNC->getNearestWaypoint(world, x, y, z).data; }
py::dict    py_getWaypoint(std::string world, std::string name)                                  { return SERVERFUNC->getWaypoint(world, name).data; }