#ifndef _ITEMSGROUND_H_
#define _ITEMSGROUND_H_
#include <string>

#include <NoNut/core/StaticClass.h>
#include <NoNut/core/CustomTypes.h>
#include "ItemGround.h"
#include <pybind11/embed.h>
namespace py = pybind11;

namespace nonut
{
	class ItemsGround : public StaticClass
	{
	public:
        static ItemsGround* get();
        
        Function<ItemGround, Int> getById;
        Function<Int, SQObject> create;
        Function<void, Int> destroy;
        
    private:
    
        static inline ItemsGround* inst = nullptr;
        
        ItemsGround();
	};
}
#endif

