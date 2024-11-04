#ifndef CORE_COMMONHEADER_H_
#define CORE_COMMONHEADER_H_

#include "sqrat.h"

namespace nonut
{
	using Int = SQInteger;
	using UInt = SQUnsignedInteger;
	using UInt32 = SQUnsignedInteger32;
	using Float = SQFloat;
	using Bool = SQBool;
	using String = std::string;

	constexpr SQObject SQ_NULL{ OT_NULL };
}

#endif // CORE_COMMONHEADER_H_
