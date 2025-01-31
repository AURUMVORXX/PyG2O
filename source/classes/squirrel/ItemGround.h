#ifndef _ITEMGROUND_H
#define _ITEMGROUND_H
#include <string>

#include <Class.h>
#include <CustomTypes.h>

namespace nonut
{
	class ItemGround : public Class
	{
	public:
		ItemGround(SQObject object);
        
        Function<nonut::Position3d> getPosition;
        Function<nonut::Position3d> getRotation;
        
		// Properties
		Property<Int>       id;
		Property<String>    instance;
		Property<Int>       amount;
		Property<String>    world;
		Property<Int>       virtualWorld;
	};
}
#endif

