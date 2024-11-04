#include <sqapi.h>
#include <pybind11/embed.h>
#include "sqevents.h"
#include "sqcontainers.h"

namespace py = pybind11;
using namespace pybind11::literals;

extern py::module_ g2o;

void addEventHandler(const char* eventName, SQFUNCTION closure, unsigned int priority = 9999)
{
    using namespace SqModule;

    Sqrat::Function sq_addEventHandler = Sqrat::RootTable().GetFunction("addEventHandler");

    if (sq_addEventHandler.IsNull())
        return;

    HSQOBJECT closureHandle;

    sq_newclosure(vm, closure, 0);
    sq_getstackobj(vm, -1, &closureHandle);

    Sqrat::Function func(vm, Sqrat::RootTable().GetObject(), closureHandle);
    sq_addEventHandler(eventName, func, priority);

    sq_pop(vm, 1);
}

void registerSquirrelEvents()
{
    addEventHandler("onInit", sq_onInit, 0);
    addEventHandler("onExit", sq_onExit, 0);
    addEventHandler("onTick", sq_onTick, 0);
    addEventHandler("onTime", sq_onTime, 0);
    addEventHandler("onBan", sq_onBan, 0);
    addEventHandler("onUnban", sq_onUnban, 0);
    
    addEventHandler("onPlayerChangeColor", sq_onPlayerChangeColor, 0);
    addEventHandler("onPlayerChangeFocus", sq_onPlayerChangeFocus, 0);
    addEventHandler("onPlayerChangeHealth", sq_onPlayerChangeHealth, 0);
    addEventHandler("onPlayerChangeMana", sq_onPlayerChangeMana, 0);
    addEventHandler("onPlayerChangeMaxHealth", sq_onPlayerChangeMaxHealth, 0);
    addEventHandler("onPlayerChangeMaxMana", sq_onPlayerChangeMaxMana, 0);
    addEventHandler("onPlayerChangeWeaponMode", sq_onPlayerChangeWeaponMode, 0);
    addEventHandler("onPlayerChangeWorld", sq_onPlayerChangeWorld, 0);
}