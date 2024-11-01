#pragma once

SQInteger sq_onInit(HSQUIRRELVM);
SQInteger sq_onExit(HSQUIRRELVM);
SQInteger sq_onTick(HSQUIRRELVM);
SQInteger sq_onTime(HSQUIRRELVM);

void registerSquirrelEvents();