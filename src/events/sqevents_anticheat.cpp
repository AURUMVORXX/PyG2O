#include <sqapi.h>
#include <pybind11/embed.h>
#include "NoNut/core/Utils.h"
#include "sqevents.h"

SQInteger sq_onPlayerUseCheat(HSQUIRRELVM vm)
{
    SQInteger playerid, type;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &type);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "type"_a=type);
    callEvent("onPlayerUseCheat", kwargs);
    
    return 0;
}