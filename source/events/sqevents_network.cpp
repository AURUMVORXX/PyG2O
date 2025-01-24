#include <sqapi.h>
#include <pybind11/embed.h>
#include <Utils.h>
#include "python/Packet.h"
#include "sqevents.h"

namespace py = pybind11;
using namespace pybind11::literals;

extern py::module_ g2o;

SQInteger sq_onPacket(HSQUIRRELVM vm)
{
    SQInteger playerid;
    HSQOBJECT data;
    
    nonut::sqGetValue(vm, 2, &playerid);
    nonut::sqGetValue(vm, 3, &data);
    
    py::dict kwargs = py::dict("playerid"_a=playerid, "data"_a=PyPacket(data));
    callEvent("onPacket", kwargs);
    
    return 0;
}