#include <sqapi.h>
#include <pybind11/embed.h>
#include "NoNut/core/Utils.h"
#include <classes/py/DamageDescription.h>
#include <classes/py/ItemGround.h>
#include "sqevents.h"

namespace py = pybind11;
using namespace pybind11::literals;

extern py::module_ g2o;

SQInteger sq_onPlayerChangeColor(HSQUIRRELVM vm)
{
    SQInteger playerid, r, g, b;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &r);
    nonut::sqGetValue(vm, 4, &g);
    nonut::sqGetValue(vm, 5, &b);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "r"_a=r, "g"_a=g, "b"_a=b);
    callEvent("onPlayerChangeColor", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerChangeFocus(HSQUIRRELVM vm)
{
    SQInteger playerid, oldFocusId, newFocusId;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &oldFocusId);
    nonut::sqGetValue(vm, 4, &newFocusId);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "oldFocusId"_a=oldFocusId, "newFocusId"_a=newFocusId);
    callEvent("onPlayerChangeFocus", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerChangeHealth(HSQUIRRELVM vm)
{
    SQInteger playerid, oldHP, newHP;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &oldHP);
    nonut::sqGetValue(vm, 4, &newHP);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "oldHP"_a=oldHP, "newHP"_a=newHP);
    callEvent("onPlayerChangeHealth", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerChangeMana(HSQUIRRELVM vm)
{
    SQInteger playerid, oldMP, newMP;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &oldMP);
    nonut::sqGetValue(vm, 4, &newMP);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "oldMP"_a=oldMP, "newMP"_a=newMP);
    callEvent("onPlayerChangeMana", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerChangeMaxHealth(HSQUIRRELVM vm)
{
    SQInteger playerid, oldMaxHP, newMaxHP;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &oldMaxHP);
    nonut::sqGetValue(vm, 4, &newMaxHP);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "oldMaxHP"_a=oldMaxHP, "newMaxHP"_a=newMaxHP);
    callEvent("onPlayerChangeMaxHealth", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerChangeMaxMana(HSQUIRRELVM vm)
{
    SQInteger playerid, oldMaxMP, newMaxMP;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &oldMaxMP);
    nonut::sqGetValue(vm, 4, &newMaxMP);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "oldMaxMP"_a=oldMaxMP, "newMaxMP"_a=newMaxMP);
    callEvent("onPlayerChangeMaxMana", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerChangeWeaponMode(HSQUIRRELVM vm)
{
    SQInteger playerid, oldWeaponMode, newWeaponMode;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &oldWeaponMode);
    nonut::sqGetValue(vm, 4, &newWeaponMode);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "oldWeaponMode"_a=oldWeaponMode, "newWeaponMode"_a=newWeaponMode);
    callEvent("onPlayerChangeWeaponMode", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerChangeWorld(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* world = nullptr;
    const SQChar* waypoint = nullptr;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &world);
    nonut::sqGetValue(vm, 4, &waypoint);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "world"_a=world, "waypoint"_a=waypoint);
    callEvent("onPlayerChangeWorld", kwargs);
    
    return 0;
}

// -------------------------------------------------------

SQInteger sq_onPlayerCommand(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* command;
    const SQChar* params;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &command);
    nonut::sqGetValue(vm, 4, &params);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "command"_a=command, "params"_a=params);
    callEvent("onPlayerCommand", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerDamage(HSQUIRRELVM vm)
{
    SQInteger playerid, killerid;
    HSQOBJECT sqobj;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &killerid);
    nonut::sqGetValue(vm, 4, &sqobj);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "killerid"_a=killerid, "description"_a=PyDamageDescription(sqobj));
    callEvent("onPlayerDamage", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerDead(HSQUIRRELVM vm)
{
    SQInteger playerid, killerid;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &killerid);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "killerid"_a=killerid);
    callEvent("onPlayerDead", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerDisconnect(HSQUIRRELVM vm)
{
    SQInteger playerid, reason;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &reason);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "reason"_a=reason);
    callEvent("onPlayerDisconnect", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerDropItem(HSQUIRRELVM vm)
{
    SQInteger playerid;
    HSQOBJECT sqobj;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &sqobj);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "itemGround"_a=PyItemGround(sqobj));
    callEvent("onPlayerDropItem", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEnterWorld(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* world;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &world);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "world"_a=world);
    callEvent("onPlayerEnterWorld", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerJoin(HSQUIRRELVM vm)
{
    SQInteger playerid;
    
    nonut::sqGetValue(vm, 2, &playerid);
    
    py::dict kwargs = py::dict("playerid"_a=playerid);
    callEvent("onPlayerJoin", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerMessage(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* message;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &message);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "message"_a=message);
    callEvent("onPlayerMessage", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerMobInteract(HSQUIRRELVM vm)
{
    SQInteger playerid, from, to;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &from);
    nonut::sqGetValue(vm, 3, &to);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "from"_a=from, "to"_a = to);
    callEvent("onPlayerMobInteract", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerRespawn(HSQUIRRELVM vm)
{
    SQInteger playerid;
    
    nonut::sqGetValue(vm, 2, &playerid);
    
    py::dict kwargs = py::dict("playerid"_a=playerid);
    callEvent("onPlayerRespawn", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerShoot(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* munition;
    
    nonut::sqGetValue(vm, 2, &playerid);
    if (sq_gettype(vm, 3) != OT_NULL)
        nonut::sqGetValue(vm, 3, &munition);
    
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "munition"_a=munition);
    callEvent("onPlayerShoot", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerSpellCast(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance;
    SQInteger spellLevel;
    
    nonut::sqGetValue(vm, 2, &playerid);
    if (sq_gettype(vm, 3) != OT_NULL)
        nonut::sqGetValue(vm, 3, &instance);
    nonut::sqGetValue(vm, 4, &spellLevel);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance, "spellLevel"_a=spellLevel);
    callEvent("onPlayerSpellCast", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerSpellSetup(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance;
    
    nonut::sqGetValue(vm, 2, &playerid);
    if (sq_gettype(vm, 3) != OT_NULL)
        nonut::sqGetValue(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    callEvent("onPlayerSpellSetup", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerTakeItem(HSQUIRRELVM vm)
{
    SQInteger playerid;
    HSQOBJECT sqobj;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &sqobj);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "itemGround"_a=PyItemGround(sqobj));
    callEvent("onPlayerTakeItem", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerTeleport(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* vobName;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &vobName);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "vobName"_a=vobName);
    callEvent("onPlayerTeleport", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerToggleFaceAni(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* aniName;
    SQBool toggle;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &aniName);
    nonut::sqGetValue(vm, 4, &toggle);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "vobName"_a=aniName, "toggle"_a = toggle);
    callEvent("onPlayerToggleFaceAni", kwargs);
    
    return 0;
}

// -------------------------------------------------------

SQInteger sq_onPlayerEquipAmulet(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance = "";
    
    nonut::sqGetValue(vm, 2, &playerid);
    if (sq_gettype(vm, 3) != OT_NULL)
        nonut::sqGetValue(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    callEvent("onPlayerEquipAmulet", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipArmor(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance = "";
    
    nonut::sqGetValue(vm, 2, &playerid);
    if (sq_gettype(vm, 3) != OT_NULL)
        nonut::sqGetValue(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    callEvent("onPlayerEquipArmor", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipBelt(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance = "";
    
    nonut::sqGetValue(vm, 2, &playerid);
    if (sq_gettype(vm, 3) != OT_NULL)
        nonut::sqGetValue(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    callEvent("onPlayerEquipBelt", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipHandItem(HSQUIRRELVM vm)
{
    SQInteger playerid, hand;
    const SQChar* instance = "";
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &hand);
    if (sq_gettype(vm, 4) != OT_NULL)
        nonut::sqGetValue(vm, 4, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "hand"_a = hand, "instance"_a=instance);
    callEvent("onPlayerEquipHandItem", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipHelmet(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance = "";
    
    nonut::sqGetValue(vm, 2, &playerid);
    if (sq_gettype(vm, 3) != OT_NULL)
        nonut::sqGetValue(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    callEvent("onPlayerEquipHelmet", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipMeleeWeapon(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance = "";
    
    nonut::sqGetValue(vm, 2, &playerid);
    if (sq_gettype(vm, 3) != OT_NULL)
        nonut::sqGetValue(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    callEvent("onPlayerEquipMeleeWeapon", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipRangedWeapon(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance = "";
    
    nonut::sqGetValue(vm, 2, &playerid);
    if (sq_gettype(vm, 3) != OT_NULL)
        nonut::sqGetValue(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    callEvent("onPlayerEquipRangedWeapon", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipRing(HSQUIRRELVM vm)
{
    SQInteger playerid, hand;
    const SQChar* instance = "";
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &hand);
    if (sq_gettype(vm, 4) != OT_NULL)
        nonut::sqGetValue(vm, 4, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "hand"_a = hand, "instance"_a=instance);
    callEvent("onPlayerEquipRing", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipShield(HSQUIRRELVM vm)
{
    SQInteger playerid;
    const SQChar* instance = "";
    
    nonut::sqGetValue(vm, 2, &playerid);
    if (sq_gettype(vm, 3) != OT_NULL)
        nonut::sqGetValue(vm, 3, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "instance"_a=instance);
    callEvent("onPlayerEquipShield", kwargs);
    
    return 0;
}

SQInteger sq_onPlayerEquipSpell(HSQUIRRELVM vm)
{
    SQInteger playerid, slotId;
    const SQChar* instance = "";
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &slotId);
    if (sq_gettype(vm, 4) != OT_NULL)
        nonut::sqGetValue(vm, 4, &instance);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "slotId"_a = slotId, "instance"_a=instance);
    callEvent("onPlayerEquipSpell", kwargs);
    
    return 0;
}