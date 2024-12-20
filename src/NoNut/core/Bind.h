#ifndef NONUT_CORE_BIND_H
#define NONUT_CORE_BIND_H

#include "CommonHeader.h"
#include <vector>

namespace nonut
{
	//TODO: Finish Bind and remove placeholder

	class Bind
	{
	public:
		static void registerFunction(String funcName, const SQFUNCTION func, size_t funcSize)
		{
			HSQUIRRELVM vm = Sqrat::DefaultVM::Get();
			const auto top = sq_gettop(vm);
			sq_pushroottable(vm);
			sq_pushstring(vm, funcName.c_str(), funcName.length());
			sq_newclosure(vm, func, 0); //create a new function
			sq_newslot(vm, -3, SQFalse);
			sq_settop(vm, top);
		}

		//template<typename F>
		//static void Function(String functionName, F& function)
		//{
		//	
		//}
	};
}
#endif // NONUT_CORE_BIND_H
