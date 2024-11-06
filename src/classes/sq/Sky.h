#ifndef _SKY_H_
#define _SKY_H_
#include <string>

#include <NoNut/core/StaticClass.h>
#include <NoNut/core/CustomTypes.h>

namespace nonut
{
	class Sky : public StaticClass
	{
	public:
        static Sky* get();
        
        Function<void, Int, Int> setRainStartTime;
        Function<SqDict> getRainStartTime;
        Function<void, Int, Int> setRainStopTime;
        Function<SqDict> getRainStopTime;
        
        Property<Int> weather;
        Property<Bool> raining;
        Property<Bool> renderLightning;
        Property<Float> windScale;
        Property<Bool> dontRain;
        
    private:
    
        static inline Sky* inst = nullptr;
        
        Sky();
	};
}
#endif

