#include <sqapi.h>
#include <pybind11/embed.h>
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

SQInteger sq_onUnban(HSQUIRRELVM vm)
{
    SQObject obj;
    sq_getstackobj(vm, 2, &obj);
    Sqrat::Table banData = Sqrat::Table(obj, vm);
    
    py::dict kwargs = sqParseTable(banData);
    g2o.attr("callEvent")("onUnban", **kwargs);
    
    return 0;
}