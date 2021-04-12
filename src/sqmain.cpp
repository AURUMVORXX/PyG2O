#include "pch.h"

extern "C" SQRESULT SQRAT_API sqmodule_load(HSQUIRRELVM vm, HSQAPI api)
{
	SqModule::init(vm, api);

	return SQ_OK;
}
