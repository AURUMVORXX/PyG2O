#include "CommonHeader.h"
#include "Array.h"

namespace nonut
{
	Array::Array(const SQObject object) : object(object), cachedSize(size())
	{
	}

	Array::~Array() = default;

	size_t Array::size() const
	{
		HSQUIRRELVM vm = Sqrat::DefaultVM::Get();
		sq_pushobject(vm, object);
		const auto result = sq_getsize(vm, -1);
		sq_pop(vm, 1);
		return static_cast<size_t>(result);
	}
}
