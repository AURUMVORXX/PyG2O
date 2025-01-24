#include <CommonHeader.h>
#include "Mds.h"

namespace nonut
{
    Mds* Mds::get()
	{
		if (inst == nullptr)
		{
			inst = new Mds();
		}
		return inst;
	}

	Mds::Mds() :
		StaticClass("Mds"),
        
        METHOD_CTOR(id),
        METHOD_CTOR(name)
	{
	}
}
