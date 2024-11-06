#include <NoNut/core/CommonHeader.h>
#include "Sky.h"

namespace nonut
{
    Sky* Sky::get()
	{
		if (inst == nullptr)
		{
			inst = new Sky();
		}
		return inst;
	}

	Sky::Sky() :
		StaticClass("Sky"),
        
        PROPERTY_CTOR(weather),
        PROPERTY_CTOR(raining),
        PROPERTY_CTOR(renderLightning),
        PROPERTY_CTOR(windScale),
        PROPERTY_CTOR(dontRain),
        
		METHOD_CTOR(getRainStartTime),
		METHOD_CTOR(getRainStopTime),
		METHOD_CTOR(setRainStartTime),
        METHOD_CTOR(setRainStopTime)
	{
	}
}
