#include "StaticClass.h"

namespace nonut
{
	StaticClass::StaticClass(const String& className)
	{
		HSQUIRRELVM vm = Sqrat::DefaultVM::Get();
		const auto top = sq_gettop(vm);

		sq_pushroottable(vm); //push root table
		sq_pushstring(vm, className.c_str(), className.length()); //push class instance name

		if (sq_get(vm, -2) == SQ_OK) //retrieve class instance
		{
			sq_getstackobj(vm, -1, &classObjectInstance);
			sq_addref(vm, &classObjectInstance);
			sq_getclass(vm, -1);
			sq_getstackobj(vm, -1, &classObject);
			sq_addref(vm, &classObject);
		}
		sq_settop(vm, top); // TODO: FIX LEAK PROPERLY
	}

	StaticClass::~StaticClass()
	{
		HSQUIRRELVM vm = Sqrat::DefaultVM::Get();
		sq_release(vm, &classObject);
		sq_release(vm, &classObjectInstance);
		sq_resetobject(&classObject);
		sq_resetobject(&classObjectInstance);
	}
}
