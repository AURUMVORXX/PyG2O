#include <NoNut/core/CommonHeader.h>
#include "DamageDescription.h"

namespace nonut
{
	DamageDescription::DamageDescription(SQObject object) :
		Class("DamageDescription", object),
        
		PROPERTY_CTOR(flags),
		PROPERTY_CTOR(damage),
		PROPERTY_CTOR(item_instance),
		PROPERTY_CTOR(distance),
		PROPERTY_CTOR(spell_id),
		PROPERTY_CTOR(spell_level),
		PROPERTY_CTOR(node)
	{
	}
}
