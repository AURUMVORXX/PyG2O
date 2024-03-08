#include <sqapi.h>

/* squirreldoc (func)
*
* This is an entry point for the module.
*
* @version	0.1
* @side		shared
* @name		sqmodule_load
* @param	(HSQUIRRELVM) vm the squirrel vm.
* @param	(HSQAPI) api the api ptr containing all of the squirrel functions.
* @return	(int) returns a function status.
*
*/
extern "C" SQRESULT SQRAT_API sqmodule_load(HSQUIRRELVM vm, HSQAPI api)
{
	SqModule::Initialize(vm, api);

	return SQ_OK;
}
