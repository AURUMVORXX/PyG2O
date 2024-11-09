#ifndef _PYFUNCTIONS_
#define _PYFUNCTIONS_

#include <pybind11/embed.h>
namespace py = pybind11;

// Shared functions
std::string py_getHostname();
int py_getMaxSlots();
int py_getPlayersCount();

float py_getDistance2d(float, float, float, float);
float py_getDistance3d(float, float, float, float, float, float);
float py_getVectorAngle(float, float, float, float);

void py_sendMessageToAll(int, int, int, std::string);
void py_sendMessageToPlayer(int, int, int, int, std::string);
void py_sendPlayerMessageToAll(int, int, int, int, std::string);
void py_sendPlayerMessageToPlayer(int, int, int, int, int, std::string);

void py_exit(int);
float py_getDayLength();
std::string py_getServerDescription();
std::string py_getServerWorld();
py::dict py_getTime();
void py_serverLog(std::string);
void py_setDayLength(float);
bool py_setServerDescription(std::string);
void py_setServerWorld(std::string);
void py_setTime(int, int, int);

void py_clearNpcActions(int);
int py_createNpc(std::string, std::string);
bool py_destroyNpc(int);
py::dict py_getNpcAction(int, int);
// ??? py_getNpcActionType
py::list py_getNpcActions(int);
int py_getNpcActionsCount(int);
int py_getNpcHostPlayer(int);
int py_getNpcLastActionId(int);
bool py_isNpc(int);
bool py_isNpcActionFinished(int, int);
void py_npcAttackMelee(int, int, int, int);
void py_npcAttackRanged(int, int);
void py_npcSpellCast(int, int);
void py_npcUseClosestMob(int, std::string, int);
//??? py_pushNpcAction
bool py_setNpcHostPlayer(int, int);

bool py_addBan(py::dict);
bool py_applyPlayerOverlay(int, int);
void py_ban(int, int, std::string);
void py_drawWeapon(int, int);
void py_equipItem(int, std::string, int);
std::string py_getPlayerAmulet(int);
float py_getPlayerAngle(int);
std::string py_getPlayerAni(int);
std::string py_getPlayerArmor(int);
py::dict py_getPlayerAtVector(int);
std::string py_getPlayerBelt(int);
py::dict py_getPlayerCameraPosition(int);
bool py_getPlayerCollision(int);
py::dict py_getPlayerColor(int);
int py_getPlayerContext(int, int);
int py_getPlayerDexterity(int);
py::list py_getPlayerFaceAnis(int);
float py_getPlayerFatness(int);
int py_getPlayerFocus(int);
int py_getPlayerHealth(int);
std::string py_getPlayerHelmet(int);
std::string py_getPlayerIP(int);
std::string py_getPlayerInstance(int);
std::string py_getPlayerMacAddr(int);
int py_getPlayerMana(int);
int py_getPlayerMaxHealth(int);
int py_getPlayerMaxMana(int);
std::string py_getPlayerMeleeWeapon(int);
std::string py_getPlayerName(int);
int py_getPlayerPing(int);
py::dict py_getPlayerPosition(int);
std::string py_getPlayerRangedWeapon(int);
int py_getPlayerRespawnTime(int);
std::string py_getPlayerRing(int, int);
py::dict py_getPlayerScale(int);
std::string py_getPlayerSerial(int);
std::string py_getPlayerShield(int);
int py_getPlayerSkillWeapon(int, int);
std::string py_getPlayerSpell(int, int);
int py_getPlayerStrength(int);
int py_getPlayerTalent(int, int);
int py_getPlayerVirtualWorld(int);
py::dict py_getPlayerVisual(int);
int py_getPlayerWeaponMode(int);
std::string py_getPlayerWorld(int);
void py_giveItem(int, std::string, int);
bool py_hitPlayer(int, int);
bool py_isPlayerConnected(int);
bool py_isPlayerDead(int);
bool py_isPlayerUnconscious(int);
void py_kick(int, std::string);
void py_playAni(int, std::string);
void py_playFaceAni(int, std::string);
void py_readySpell(int, int, int);
void py_removeItem(int, std::string, int);
bool py_removePlayerOverlay(int, int);
void py_removeWeapon(int);
void py_respawnPlayer(int);
void py_setPlayerAngle(int, float);
void py_setPlayerCollision(int, bool);
void py_setPlayerColor(int, int, int, int);
void py_setPlayerContext(int, int, int);
void py_setPlayerDexterity(int, int);
void py_setPlayerFatness(int, float);
void py_setPlayerHealth(int, int);
void py_setPlayerInstance(int, std::string);
void py_setPlayerInvisible(int, bool);
void py_setPlayerMana(int, int);
void py_setPlayerMaxHealth(int, int);
void py_setPlayerMaxMana(int, int);
void py_setPlayerName(int, std::string);
void py_setPlayerPosition(int, float, float, float);
void py_setPlayerRespawnTime(int, int);
void py_setPlayerScale(int, float, float, float);
void py_setPlayerSkillWeapon(int, int, int);
void py_setPlayerStrength(int, int);
void py_setPlayerTalent(int, int, int);
void py_setPlayerVirtualWorld(int, int);
void py_setPlayerVisual(int, std::string, int, std::string, int);
void py_setPlayerWeaponMode(int, int);
void py_setPlayerWorld(int, std::string, std::string);
void py_spawnPlayer(int);
void py_stopAni(int, std::string);
void py_stopFaceAni(int, std::string);
void py_unequipItem(int, std::string);
void py_unreadySpell(int);
void py_unspawnPlayer(int);
void py_useItem(int, std::string);
void py_useItemToState(int, std::string, int);

py::list py_findNearbyPlayers(py::dict, int, std::string, int);
py::list py_getSpawnedPlayersForPlayer(int);
py::list py_getStreamedPlayersByPlayer(int);
py::dict py_getNearestWaypoint(std::string, int, int, int);
py::dict py_getWaypoint(std::string, std::string);

#endif