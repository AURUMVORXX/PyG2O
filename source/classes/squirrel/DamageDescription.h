#ifndef _DAMAGEDESCRIPTION_H_
#define _DAMAGEDESCRIPTION_H_
#include <string>

#include <Class.h>
#include <CustomTypes.h>

namespace nonut
{
	class DamageDescription : public Class
	{
	public:
		DamageDescription(SQObject object);

		Property<Int>       flags;
		Property<Int>       damage;
		Property<String>    item_instance;
		Property<Int>       distance;
		Property<Int>       spell_id;
		Property<Int>       spell_level;
		Property<String>    node;
	};
}
#endif

