#ifndef _MDS_H
#define _MDS_H
#include <string>

#include <StaticClass.h>
#include <CustomTypes.h>

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

