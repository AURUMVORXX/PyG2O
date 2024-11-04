#include "Constant.h"

namespace nonut
{
	SQObject getConstTable()
	{
		SQObject obj;
		HSQUIRRELVM vm = Sqrat::DefaultVM::Get();
		sq_pushconsttable(vm);
		sq_getstackobj(vm, -1, &obj);
		sq_pop(vm, 1); // No addref needed, since the consttable is always around
		return obj;
	}
}
