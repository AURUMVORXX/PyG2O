#ifndef _WAY_H
#define _WAY_H
#include <string>

#include <NoNut/core/Class.h>
#include <NoNut/core/CustomTypes.h>

namespace nonut
{
	class Way : public Class
	{
	public:
		Way(String, String, String);
		explicit Way(SQObject object);

		Property<String> start;
        Property<String> end;
        
        Function<SqList> getWaypoints;
        Function<Int> getCountWaypoints;
	};
}
#endif

