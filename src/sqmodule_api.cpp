#include "pch.h"

namespace SqModule
{
	HSQUIRRELVM vm;
	HSQAPI api;

	SQPRINTFUNCTION print;
	SQPRINTFUNCTION error;

	void init(HSQUIRRELVM vm, HSQAPI api)
	{
		SqModule::vm = vm;
		SqModule::api = api;

		SqModule::print = sq_getprintfunc(vm);
		SqModule::error = sq_geterrorfunc(vm);

		Sqrat::DefaultVM::Set(vm);
	}
}
