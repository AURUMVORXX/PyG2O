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
    SQInteger playerid, world, waypoint;
    
    sq_getinteger(vm, 2, &playerid);
    sq_getinteger(vm, 3, &world);
    sq_getinteger(vm, 4, &waypoint);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "world"_a=world, "waypoint"_a=waypoint);
    g2o.attr("callEvent")("onPlayerChangeWorld", **kwargs);
    
    return 0;
}