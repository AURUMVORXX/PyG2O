#include "CommonHeader.h"
#include "Class.h"

namespace nonut
{
	Class::Class(const String& className, const SQObject classObjectInstance)
	{
		HSQUIRRELVM vm = Sqrat::DefaultVM::Get();
		if (classObjectInstance._type == OT_NULL)
		{
			bIsNull = true;
			const auto top = sq_gettop(vm);

			sq_pushroottable(vm); //push root table
			sq_pushstring(vm, className.c_str(), className.length()); //push class name

			if (sq_get(vm, -2) == SQ_OK) //retrieve class
			{
				sq_getstackobj(vm, -1, &classObject);
				sq_addref(vm, &classObject);
				if (sq_createinstance(vm, -1) == SQ_OK) //create class instance
				{
					//1. Get object ptr
					sq_getstackobj(vm, -1, &this->classObjectInstance); //retrieve object
					sq_addref(vm, &this->classObjectInstance);
					//Add ref thanks to which object will not be immediately deleted
					sq_pop(vm, 1); // pop class instance
				}
			}
			sq_settop(vm, top); // TODO: FIX LEAK PROPERLY
		}
		else
		{
			this->classObjectInstance = classObjectInstance;
			const auto top = sq_gettop(vm);
			sq_addref(vm, &this->classObjectInstance);

			sq_pushroottable(vm); //push root table
			sq_pushstring(vm, className.c_str(), className.length()); //push class name

			if (sq_get(vm, -2) == SQ_OK) //retrieve class
			{
				sq_getstackobj(vm, -1, &classObject);
				sq_addref(vm, &classObject);
			}

			sq_settop(vm, top);
		}
	}

	Class::~Class()
	{
		HSQUIRRELVM vm = Sqrat::DefaultVM::Get();
		sq_release(vm, &classObject);
		sq_release(vm, &classObjectInstance);
		sq_resetobject(&classObject);
		sq_resetobject(&classObjectInstance);
	}

	SQObject Class::getInstance() const
	{
		return classObjectInstance;
	}
	
	bool Class::isNull() const
	{
		return bIsNull;
	}
}
