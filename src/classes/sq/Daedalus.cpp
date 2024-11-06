#include <NoNut/core/CommonHeader.h>
#include "Daedalus.h"

namespace nonut
{
    Daedalus* Daedalus::get()
	{
		if (inst == nullptr)
		{
			inst = new Daedalus();
		}
		return inst;
	}

	Daedalus::Daedalus() :
		StaticClass("Daedalus"),
        
		METHOD_CTOR(index),
		METHOD_CTOR(symbol),
		METHOD_CTOR(instance)
	{
	}
}
