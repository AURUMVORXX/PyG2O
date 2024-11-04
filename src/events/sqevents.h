#ifndef _SQEVENTS_H_
#define _SQEVENTS_H

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

void registerSquirrelEvents();

#endif