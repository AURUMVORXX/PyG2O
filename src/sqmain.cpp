#include "pch.h"

extern "C" SQRESULT SQRAT_API sqmodule_load(HSQUIRRELVM vm, HSQAPI api)
{
	SqModule::Initalize(vm, api);
	Sqrat::DefaultVM::Set(vm);

	return SQ_OK;
}
