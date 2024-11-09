#ifndef _MDS_H
#define _MDS_H
#include <string>

#include <NoNut/core/StaticClass.h>
#include <NoNut/core/CustomTypes.h>

namespace nonut
{
	class Mds : public StaticClass
	{
	public:
        static Mds* get();
        
        Function<Int, String> id;
        Function<String, Int> name;
        
    private:
    
        static inline Mds* inst = nullptr;
        
        Mds();
	};
}
#endif

