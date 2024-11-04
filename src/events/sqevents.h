#ifndef _SQEVENTS_H_
#define _SQEVENTS_H

SQInteger sq_onInit(HSQUIRRELVM);
SQInteger sq_onExit(HSQUIRRELVM);
SQInteger sq_onTick(HSQUIRRELVM);
SQInteger sq_onTime(HSQUIRRELVM);
SQInteger sq_onBan(HSQUIRRELVM);
SQInteger sq_onUnban(HSQUIRRELVM);

void registerSquirrelEvents();

#endif