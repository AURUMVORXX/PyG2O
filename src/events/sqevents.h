#ifndef _SQEVENTS_H_
#define _SQEVENTS_H

namespace py = pybind11;
using namespace pybind11::literals;

void callEvent(const char*, py::dict);

SQInteger sq_onInit(HSQUIRRELVM);
SQInteger sq_onExit(HSQUIRRELVM);
SQInteger sq_onTick(HSQUIRRELVM);
SQInteger sq_onTime(HSQUIRRELVM);
SQInteger sq_onBan(HSQUIRRELVM);
SQInteger sq_onUnban(HSQUIRRELVM);

SQInteger sq_onPlayerChangeColor(HSQUIRRELVM);
SQInteger sq_onPlayerChangeFocus(HSQUIRRELVM);
SQInteger sq_onPlayerChangeHealth(HSQUIRRELVM);
SQInteger sq_onPlayerChangeMana(HSQUIRRELVM);
SQInteger sq_onPlayerChangeMaxHealth(HSQUIRRELVM);
SQInteger sq_onPlayerChangeMaxMana(HSQUIRRELVM);
SQInteger sq_onPlayerChangeWeaponMode(HSQUIRRELVM);
SQInteger sq_onPlayerChangeWorld(HSQUIRRELVM);
SQInteger sq_onPlayerCommand(HSQUIRRELVM);
SQInteger sq_onPlayerDead(HSQUIRRELVM);
SQInteger sq_onPlayerDisconnect(HSQUIRRELVM);
SQInteger sq_onPlayerEnterWorld(HSQUIRRELVM);
SQInteger sq_onPlayerEquipAmulet(HSQUIRRELVM);
SQInteger sq_onPlayerEquipArmor(HSQUIRRELVM);
SQInteger sq_onPlayerEquipBelt(HSQUIRRELVM);
SQInteger sq_onPlayerEquipHandItem(HSQUIRRELVM);
SQInteger sq_onPlayerEquipHelmet(HSQUIRRELVM);
SQInteger sq_onPlayerEquipMeleeWeapon(HSQUIRRELVM);
SQInteger sq_onPlayerEquipRangedWeapon(HSQUIRRELVM);
SQInteger sq_onPlayerEquipRing(HSQUIRRELVM);
SQInteger sq_onPlayerEquipShield(HSQUIRRELVM);
SQInteger sq_onPlayerEquipSpell(HSQUIRRELVM);
SQInteger sq_onPlayerJoin(HSQUIRRELVM);
SQInteger sq_onPlayerMessage(HSQUIRRELVM);
SQInteger sq_onPlayerMobInteract(HSQUIRRELVM);
SQInteger sq_onPlayerRespawn(HSQUIRRELVM);
SQInteger sq_onPlayerShoot(HSQUIRRELVM);
SQInteger sq_onPlayerSpellCast(HSQUIRRELVM);
SQInteger sq_onPlayerSpellSetup(HSQUIRRELVM);
SQInteger sq_onPlayerTeleport(HSQUIRRELVM);
SQInteger sq_onPlayerToggleFaceAni(HSQUIRRELVM);

SQInteger sq_onPacket(HSQUIRRELVM);

void registerSquirrelEvents();

#endif