#include <NoNut/core/CommonHeader.h>
#include "ItemGround.h"

namespace nonut
{
	ItemGround::ItemGround() :
		Class("ItemGround"),
        
		METHOD_CTOR(getPosition),
		METHOD_CTOR(getRotation),
		
		PROPERTY_CTOR(id),
		PROPERTY_CTOR(instance),
		PROPERTY_CTOR(amount),
		PROPERTY_CTOR(world),
		PROPERTY_CTOR(virtualWorld)
	{
		classCtor();
	}

	ItemGround::ItemGround(SQObject object) :
		Class("ItemGround", object),
        
		METHOD_CTOR(getPosition),
		METHOD_CTOR(getRotation),
		
		PROPERTY_CTOR(id),
		PROPERTY_CTOR(instance),
		PROPERTY_CTOR(amount),
		PROPERTY_CTOR(world),
		PROPERTY_CTOR(virtualWorld)
	{
	}
}
