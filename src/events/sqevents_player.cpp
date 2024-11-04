#include <sqapi.h>
#include <pybind11/embed.h>
#include "sqevents.h"

namespace py = pybind11;
using namespace pybind11::literals;

extern py::module_ g2o;

SQInteger sq_onPlayerChangeColor(HSQUIRRELVM vm)
{
    SQInteger playerid, r, g, b;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getinteger(vm, 3, &r);
    sq_getinteger(vm, 4, &g);
    sq_getinteger(vm, 5, &b);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "r"_a=r, "g"_a=g, "b"_a=b);
    g2o.attr("callEvent")("onPlayerChangeColor", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerChangeFocus(HSQUIRRELVM vm)
{
    SQInteger playerid, oldFocusId, newFocusId;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getinteger(vm, 3, &oldFocusId);
    sq_getinteger(vm, 4, &newFocusId);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "oldFocusId"_a=oldFocusId, "newFocusId"_a=newFocusId);
    g2o.attr("callEvent")("onPlayerChangeFocus", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerChangeHealth(HSQUIRRELVM vm)
{
    SQInteger playerid, oldHP, newHP;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getinteger(vm, 3, &oldHP);
    sq_getinteger(vm, 4, &newHP);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "oldHP"_a=oldHP, "newHP"_a=newHP);
    g2o.attr("callEvent")("onPlayerChangeHealth", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerChangeMana(HSQUIRRELVM vm)
{
    SQInteger playerid, oldMP, newMP;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getinteger(vm, 3, &oldMP);
    sq_getinteger(vm, 4, &newMP);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "oldMP"_a=oldMP, "newMP"_a=newMP);
    g2o.attr("callEvent")("onPlayerChangeMana", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerChangeMaxHealth(HSQUIRRELVM vm)
{
    SQInteger playerid, oldMaxHP, newMaxHP;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getinteger(vm, 3, &oldMaxHP);
    sq_getinteger(vm, 4, &newMaxHP);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "oldMaxHP"_a=oldMaxHP, "newMaxHP"_a=newMaxHP);
    g2o.attr("callEvent")("onPlayerChangeMaxHealth", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerChangeMaxMana(HSQUIRRELVM vm)
{
    SQInteger playerid, oldMaxMP, newMaxMP;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getinteger(vm, 3, &oldMaxMP);
    sq_getinteger(vm, 4, &newMaxMP);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "oldMaxMP"_a=oldMaxMP, "newMaxMP"_a=newMaxMP);
    g2o.attr("callEvent")("onPlayerChangeMaxMana", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerChangeWeaponMode(HSQUIRRELVM vm)
{
    SQInteger playerid, oldWeaponMode, newWeaponMode;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getinteger(vm, 3, &oldWeaponMode);
    sq_getinteger(vm, 4, &newWeaponMode);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "oldWeaponMode"_a=oldWeaponMode, "newWeaponMode"_a=newWeaponMode);
    g2o.attr("callEvent")("onPlayerChangeWeaponMode", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerChangeWorld(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* world;
    const SQChar* waypoint;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getstring(vm, 3, &world);
    sq_getstring(vm, 4, &waypoint);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "world"_a=world, "waypoint"_a=waypoint);
    g2o.attr("callEvent")("onPlayerChangeWorld", **kwargs);
    
    return 0;
}

// -------------------------------------------------------

SQInteger sq_onPlayerCommand(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* command;
    const SQChar* params;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getstring(vm, 3, &command);
    sq_getstring(vm, 4, &params);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "command"_a=command, "params"_a=params);
    g2o.attr("callEvent")("onPlayerCommand", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerDead(HSQUIRRELVM vm)
{
    SQInteger playerid, killerid;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getinteger(vm, 3, &killerid);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "killerid"_a=killerid);
    g2o.attr("callEvent")("onPlayerDead", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerDisconnect(HSQUIRRELVM vm)
{
    SQInteger playerid, reason;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getinteger(vm, 3, &reason);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "reason"_a=reason);
    g2o.attr("callEvent")("onPlayerDisconnect", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEnterWorld(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* world;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getstring(vm, 3, &world);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "world"_a=world);
    g2o.attr("callEvent")("onPlayerEnterWorld", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerJoin(HSQUIRRELVM vm)
{
    SQInteger playerid;
    
    sq_getinteger(vm, 2, &playerid);
    
    py::dict kwargs = py::dict("playerid"_a=playerid);
    g2o.attr("callEvent")("onPlayerJoin", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerMessage(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* message;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getstring(vm, 3, &message);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "message"_a=message);
    g2o.attr("callEvent")("onPlayerMessage", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerMobInteract(HSQUIRRELVM vm)
{
    SQInteger playerid, from, to;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getinteger(vm, 3, &from);
    sq_getinteger(vm, 3, &to);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "from"_a=from, "to"_a = to);
    g2o.attr("callEvent")("onPlayerMobInteract", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerRespawn(HSQUIRRELVM vm)
{
    SQInteger playerid;
    
    sq_getinteger(vm, 2, &playerid);
    
    py::dict kwargs = py::dict("playerid"_a=playerid);
    g2o.attr("callEvent")("onPlayerRespawn", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerShoot(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* munition;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getstring(vm, 3, &munition);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "munition"_a=munition);
    g2o.attr("callEvent")("onPlayerShoot", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerSpellCast(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getstring(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    g2o.attr("callEvent")("onPlayerSpellCast", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerSpellSetup(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getstring(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    g2o.attr("callEvent")("onPlayerSpellSetup", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerTeleport(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* vobName;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getstring(vm, 3, &vobName);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "vobName"_a=vobName);
    g2o.attr("callEvent")("onPlayerTeleport", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerToggleFaceAni(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* aniName;
    SQBool toggle;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getstring(vm, 3, &aniName);
    sq_getbool(vm, 4, &toggle);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "vobName"_a=aniName, "toggle"_a = toggle);
    g2o.attr("callEvent")("onPlayerToggleFaceAni", **kwargs);
    
    return 0;
}

// -------------------------------------------------------

SQInteger sq_onPlayerEquipAmulet(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getstring(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    g2o.attr("callEvent")("onPlayerEquipAmulet", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipArmor(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getstring(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    g2o.attr("callEvent")("onPlayerEquipArmor", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipBelt(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getstring(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    g2o.attr("callEvent")("onPlayerEquipBelt", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipHandItem(HSQUIRRELVM vm)
{
    SQInteger playerid, hand;
    const SQChar* instance;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getinteger(vm, 3, &hand);
    sq_getstring(vm, 4, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "hand"_a = hand, "instance"_a=instance);
    g2o.attr("callEvent")("onPlayerEquipHandItem", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipHelmet(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getstring(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    g2o.attr("callEvent")("onPlayerEquipHelmet", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipMeleeWeapon(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getstring(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    g2o.attr("callEvent")("onPlayerEquipMeleeWeapon", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipRangedWeapon(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getstring(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    g2o.attr("callEvent")("onPlayerEquipRangedWeapon", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipRing(HSQUIRRELVM vm)
{
    SQInteger playerid, hand;
    const SQChar* instance;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getinteger(vm, 3, &hand);
    sq_getstring(vm, 4, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "hand"_a = hand, "instance"_a=instance);
    g2o.attr("callEvent")("onPlayerEquipRing", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipShield(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getstring(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    g2o.attr("callEvent")("onPlayerEquipShield", **kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipSpell(HSQUIRRELVM vm)
{
    SQInteger playerid, slotId;
    const SQChar* instance;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getinteger(vm, 3, &slotId);
    sq_getstring(vm, 4, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "slotId"_a = slotId, "instance"_a=instance);
    g2o.attr("callEvent")("onPlayerEquipSpell", **kwargs);
    
    return 0;
}