#include <sqapi.h>
#include <pybind11/embed.h>
#include "NoNut/core/Utils.h"
#include "sqcontainers.h"
#include "sqevents.h"

SQInteger sq_onNpcActionFinished(HSQUIRRELVM vm)
{
    SQInteger npc_id, action_type, action_id;
    SQBool result;
    
    nonut::sqGetValue(vm, 2, &npc_id);
    nonut::sqGetValue(vm, 3, &action_type);
    nonut::sqGetValue(vm, 4, &action_id);
    nonut::sqGetValue(vm, 5, &result);
    
    py::dict kwargs = py::dict("npc_id"_a=npc_id, "action_type"_a=action_type, "action_id"_a=action_id, "result"_a=result);
    callEvent("onNpcActionFinished", kwargs);
    
    return 0;
}

SQInteger sq_onNpcActionSent(HSQUIRRELVM vm)
{
    SQInteger npc_id, action_type, action_id;
    
    nonut::sqGetValue(vm, 2, &npc_id);
    nonut::sqGetValue(vm, 3, &action_type);
    nonut::sqGetValue(vm, 4, &action_id);
    
    py::dict kwargs = py::dict("npc_id"_a=npc_id, "action_type"_a=action_type, "action_id"_a=action_id);
    callEvent("onNpcActionSent", kwargs);
    
    return 0;
}

SQInteger sq_onNpcChangeHostPlayer(HSQUIRRELVM vm)
{
    SQInteger npc_id, current_id, previous_id;
    
    nonut::sqGetValue(vm, 2, &npc_id);
    nonut::sqGetValue(vm, 3, &current_id);
    nonut::sqGetValue(vm, 4, &previous_id);
    
    py::dict kwargs = py::dict("npc_id"_a=npc_id, "current_id"_a=current_id, "previous_id"_a=previous_id);
    callEvent("onNpcChangeHostPlayer", kwargs);
    
    return 0;
}

SQInteger sq_onNpcCreated(HSQUIRRELVM vm)
{
    SQInteger npc_id;
    
    nonut::sqGetValue(vm, 2, &npc_id);
    
    py::dict kwargs = py::dict("npc_id"_a=npc_id);
    callEvent("onNpcCreated", kwargs);
    
    return 0;
}

SQInteger sq_onNpcDestroyed(HSQUIRRELVM vm)
{
    SQInteger npc_id;
    
    nonut::sqGetValue(vm, 2, &npc_id);
    
    py::dict kwargs = py::dict("npc_id"_a=npc_id);
    callEvent("onNpcDestroyed", kwargs);
    
    return 0;
}