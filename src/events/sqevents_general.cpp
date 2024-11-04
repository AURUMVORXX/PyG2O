#include <sqapi.h>
#include <pybind11/embed.h>
#include "NoNut/core/Utils.h"
#include "sqcontainers.h"
#include "sqevents.h"

namespace py = pybind11;
using namespace pybind11::literals;

extern py::module_ g2o;

SQInteger sq_onInit(HSQUIRRELVM vm)
{
    py::object result = g2o.attr("callEvent")("onInit");
    return 0;
}

SQInteger sq_onExit(HSQUIRRELVM vm)
{
    py::object result = g2o.attr("callEvent")("onExit");
    return 0;
}

SQInteger sq_onTick(HSQUIRRELVM vm)
{
    py::object result = g2o.attr("callEvent")("onTick");
    return 0;
}

SQInteger sq_onTime(HSQUIRRELVM vm)
{
    SQInteger day, hour, min;
    
    nonut::sqGetValue(vm, 2, &day);
    nonut::sqGetValue(vm, 3, &hour);
    nonut::sqGetValue(vm, 4, &min);
    
    py::dict kwargs = py::dict("day"_a=day, "hour"_a=hour, "min"_a=min);
    g2o.attr("callEvent")("onTime", **kwargs);
    
    return 0;
}

SQInteger sq_onBan(HSQUIRRELVM vm)
{
    HSQOBJECT obj;
    nonut::sqGetValue(vm, 2, &obj);
    Sqrat::Table banData = Sqrat::Table(obj, vm);
    
    py::dict kwargs = sqParseTable(banData);
    g2o.attr("callEvent")("onBan", **kwargs);
    
    return 0;
}

SQInteger sq_onUnban(HSQUIRRELVM vm)
{
    HSQOBJECT obj;
    nonut::sqGetValue(vm, 2, &obj);
    Sqrat::Table banData = Sqrat::Table(obj, vm);
    
    py::dict kwargs = sqParseTable(banData);
    g2o.attr("callEvent")("onUnban", **kwargs);
    
    return 0;
}