#ifndef _ITEMGROUND_H
#define _ITEMGROUND_H
#include <string>

#include <NoNut/core/Class.h>
#include <NoNut/core/CustomTypes.h>

namespace nonut
{
	class ItemGround : public Class
	{
	public:
		ItemGround();
		explicit ItemGround(SQObject object);
        
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

