#include <NoNut/core/CommonHeader.h>
#include "ItemsGround.h"

namespace nonut
{
    ItemsGround* ItemsGround::get()
	{
		if (inst == nullptr)
		{
			inst = new ItemsGround();
		}
		return inst;
	}

	ItemsGround::ItemsGround() :
		StaticClass("ItemsGround"),
        
        METHOD_CTOR(getById),
        METHOD_CTOR(create),
        METHOD_CTOR(destroy)
	{
	}
}
