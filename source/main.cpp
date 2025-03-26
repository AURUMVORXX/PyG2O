#include <sqapi.h>
#include <pybind11/embed.h>
#include "sqevents.h"
#include "sqconstants.h"
#include "squirrel/functions.h"
#include "bind.h"

namespace py = pybind11;
py::scoped_interpreter guard{};

py::module_ g2o;

extern "C" SQRESULT SQRAT_API sqmodule_load(HSQUIRRELVM vm, HSQAPI api)
{
	SqModule::Initialize(vm, api);
	Sqrat::DefaultVM::Set(vm);
	
	try
	{
		py::dict locals = py::dict();
		py::exec(R"(
			import site
			import json
			import sys
			import importlib
			import importlib.util
			site.addsitedir('.')
			import os
			
			if 'VIRTUAL_ENV' in os.environ:
				packages_path = os.path.join(os.environ['VIRTUAL_ENV'], 'Lib', 'site-packages')
				sys.path.append(packages_path)
			
			entry_point = 'pyg2o_entry'
			try:
				with open('pyg2o.json', 'r') as f:
					json = json.loads(f.read())
					entry_point = json['entry']
			except Exception as e:
				pass
				
			try:
				spec = importlib.util.find_spec(entry_point)
				if spec is not None:
					if spec.submodule_search_locations:
						sys.path.append(spec.submodule_search_locations[0])
			except Exception as e:
				print(e)

			spec = importlib.util.find_spec('g2o')
			if spec is not None:
				if spec.submodule_search_locations:
					sys.path.append(spec.submodule_search_locations[0])
					
		)", py::globals(), locals);
		
		registerSquirrelConstants();
		registerSquirrelObjects();
		g2o 		= py::module_::import("g2o");
		
		py::module_ importlib = py::module_::import("importlib");
		importlib.attr("import_module")(locals["entry_point"]);
	}
	catch (py::error_already_set &e)
	{
		py::print(e.what());
		return SQ_ERROR;
	}
	
	registerSquirrelEvents();
	return SQ_OK;
}