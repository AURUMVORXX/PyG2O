#include <sqapi.h>
#include <pybind11/embed.h>
#include <iostream>
#include <pybind11/embed.h>
#include "sqevents.h"

namespace py = pybind11;
py::scoped_interpreter guard{};

py::module_ g2o 	= py::module_::import("g2o");
py::module_ scripts = py::module_::import("scripts");

extern "C" SQRESULT SQRAT_API sqmodule_load(HSQUIRRELVM vm, HSQAPI api)
{
	
	SqModule::Initialize(vm, api);
	Sqrat::DefaultVM::Set(vm);
	
	registerSquirrelEvents();

	return SQ_OK;
}