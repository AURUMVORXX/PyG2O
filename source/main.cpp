#include <sqapi.h>
#include <pybind11/embed.h>
#include "sqevents.h"
#include "sqconstants.h"
#include "squirrel/functions.h"

namespace py = pybind11;
py::scoped_interpreter guard{};

py::module_ g2o;

extern "C" SQRESULT SQRAT_API sqmodule_load(HSQUIRRELVM vm, HSQAPI api)
{
	SqModule::Initialize(vm, api);
	Sqrat::DefaultVM::Set(vm);
	
	try
	{
		registerSquirrelConstants();
		
		py::exec(R"(
			import site
			import json
			import importlib
			
			venv_path = 'test_venv/Lib/site-packages'
			site.addsitedir('.')
			
			entry_point = 'pyg2o_entry'
			
			try:
				with open('pyg2o.json', 'r') as f:
					json = json.loads(f.read())
					entry_point = json['entry']
			except Exception as e:
				pass
				
			try:
				importlib.import_module(entry_point)
			except Exception as e:
				print(e)
		)");
		
		g2o 		= py::module_::import("g2o");
	}
	catch (py::error_already_set &e)
	{
		py::print(e.what());
		return SQ_ERROR;
	}
	
	registerSquirrelEvents();
	return SQ_OK;
}