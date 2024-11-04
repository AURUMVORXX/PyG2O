#include <sqapi.h>
#include <pybind11/embed.h>
#include "events/sqevents.h"

namespace py = pybind11;
py::scoped_interpreter guard{};

py::module_ pysys   = py::module_::import("sys");
py::module_ g2o;
py::module_ scripts;


extern "C" SQRESULT SQRAT_API sqmodule_load(HSQUIRRELVM vm, HSQAPI api)
{
	try
	{
		g2o 		= py::module_::import("g2o");
		scripts 	= py::module_::import("scripts");

	}
	catch (py::error_already_set &e)
	{
		pysys.attr("stderr").attr("write")(e.what());
	}
	
	SqModule::Initialize(vm, api);
	Sqrat::DefaultVM::Set(vm);
	
	registerSquirrelEvents();

	return SQ_OK;
}