#ifndef _DAEDALUS_H_
#define _DAEDALUS_H_
#include <string>

#include <NoNut/core/StaticClass.h>
#include <NoNut/core/CustomTypes.h>

namespace nonut
{
	class Daedalus : public StaticClass
	{
	public:
        static Daedalus* get();
    
        Function<Int, String> index;
        Function<SqDict, String> symbol;
		    Function<SqDict, String> instance;
        
    private:
    
        static inline Daedalus* inst = nullptr;
        
        Daedalus();
	};
}
#endif

