#include "pch.h"

extern "C" SQRESULT SQRAT_API sqmodule_load(HSQUIRRELVM vm, HSQAPI api)
{
	// Module Init
	sqModule::vm = vm;
	sqModule::api = api;

	sqModule::print = sq_getprintfunc(vm);
	sqModule::error = sq_geterrorfunc(vm);

	Sqrat::DefaultVM::Set(vm);

	return SQ_OK;
}
