#include <sqapi.h>
#include <pybind11/embed.h>
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
    
    sq_getinteger(vm, 2, &day);
    sq_getinteger(vm, 3, &hour);
    sq_getinteger(vm, 4, &min);
    
    py::dict kwargs = py::dict("day"_a=day, "hour"_a=hour, "min"_a=min);
    g2o.attr("callEvent")("onTime", **kwargs);
    
    return 0;
}

SQInteger sq_onBan(HSQUIRRELVM vm)
{
    SQObject obj;
    sq_getstackobj(vm, 2, &obj);
    Sqrat::Table banData = Sqrat::Table(obj, vm);
    
    py::dict kwargs = sqParseTable(banData);
    g2o.attr("callEvent")("onBan", **kwargs);
    
    return 0;
}

void registerSquirrelEvents()
{
    addEventHandler("onInit", sq_onInit, 0);
    addEventHandler("onExit", sq_onExit, 0);
    addEventHandler("onTick", sq_onTick, 0);
    addEventHandler("onTime", sq_onTime, 0);
    addEventHandler("onBan", sq_onBan, 0);
}