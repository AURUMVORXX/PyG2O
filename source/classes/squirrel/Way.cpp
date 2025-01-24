#include <CommonHeader.h>
#include "Way.h"

namespace nonut
{
	Way::Way(String world, String startWp, String endWp) :
		Class("Way"),
		METHOD_CTOR(getWaypoints),
        METHOD_CTOR(getCountWaypoints),
        
        PROPERTY_CTOR(start),
        PROPERTY_CTOR(end)
	{
		classCtor(world, startWp, endWp);
	}

	Way::Way(SQObject object) :
		Class("Way", object),
		METHOD_CTOR(getWaypoints),
        METHOD_CTOR(getCountWaypoints),
        
        PROPERTY_CTOR(start),
        PROPERTY_CTOR(end)
	{
	}
}
