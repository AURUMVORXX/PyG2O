#include <sqapi.h>
#include <pybind11/embed.h>
#include "sqevents.h"
#include "sqcontainers.h"

namespace py = pybind11;
using namespace pybind11::literals;

extern py::module_ g2o;
extern py::module_ pysys;

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

void callEvent(const char* eventName, py::dict kwargs)
{
    try
	{
        bool result = g2o.attr("callEvent")(eventName, **kwargs).cast<bool>();
        if (result)
        {
            Sqrat::RootTable().GetFunction("cancelEvent").Execute();
        }
	}
	catch (py::error_already_set &e)
	{
        pysys.attr("stderr").attr("write")(e.what());
	}
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
    
    addEventHandler("onPlayerCommand", sq_onPlayerCommand, 0);
    addEventHandler("onPlayerDamage", sq_onPlayerDamage, 0);
    addEventHandler("onPlayerDead", sq_onPlayerDead, 0);
    addEventHandler("onPlayerDisconnect", sq_onPlayerDisconnect, 0);
    addEventHandler("onPlayerDropItem", sq_onPlayerDropItem, 0);
    addEventHandler("onPlayerEnterWorld", sq_onPlayerEnterWorld, 0);
    addEventHandler("onPlayerJoin", sq_onPlayerJoin, 0);
    addEventHandler("onPlayerMessage", sq_onPlayerMessage, 0);
    addEventHandler("onPlayerMobInteract", sq_onPlayerMobInteract, 0);
    addEventHandler("onPlayerRespawn", sq_onPlayerRespawn, 0);
    addEventHandler("onPlayerShoot", sq_onPlayerShoot, 0);
    addEventHandler("onPlayerSpellCast", sq_onPlayerSpellCast, 0);
    addEventHandler("onPlayerSpellSetup", sq_onPlayerSpellSetup, 0);
    addEventHandler("onPlayerTakeItem", sq_onPlayerTakeItem, 0);
    addEventHandler("onPlayerTeleport", sq_onPlayerTeleport, 0);
    addEventHandler("onPlayerToggleFaceAni", sq_onPlayerToggleFaceAni, 0);
    
    addEventHandler("onPlayerEquipAmulet", sq_onPlayerEquipAmulet, 0);
    addEventHandler("onPlayerEquipArmor", sq_onPlayerEquipArmor, 0);
    addEventHandler("onPlayerEquipBelt", sq_onPlayerEquipBelt, 0);
    addEventHandler("onPlayerEquipHandItem", sq_onPlayerEquipHandItem, 0);
    addEventHandler("onPlayerEquipHelmet", sq_onPlayerEquipHelmet, 0);
    addEventHandler("onPlayerEquipMeleeWeapon", sq_onPlayerEquipMeleeWeapon, 0);
    addEventHandler("onPlayerEquipRangedWeapon", sq_onPlayerEquipRangedWeapon, 0);
    addEventHandler("onPlayerEquipRing", sq_onPlayerEquipRing, 0);
    addEventHandler("onPlayerEquipShield", sq_onPlayerEquipShield, 0);
    addEventHandler("onPlayerEquipSpell", sq_onPlayerEquipSpell, 0);
    
    addEventHandler("onPacket", sq_onPacket, 0);
    
    addEventHandler("onPlayerUseCheat", sq_onPlayerUseCheat, 0);
    
    addEventHandler("onNpcActionFinished", sq_onNpcActionFinished, 0);
    addEventHandler("onNpcActionSent", sq_onNpcActionSent, 0);
    addEventHandler("onNpcChangeHostPlayer", sq_onNpcChangeHostPlayer, 0);
    addEventHandler("onNpcCreated", sq_onNpcCreated, 0);
    addEventHandler("onNpcDestroyed", sq_onNpcDestroyed, 0);
}