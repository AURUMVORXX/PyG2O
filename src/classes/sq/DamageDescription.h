#ifndef _DAMAGEDESCRIPTION_H_
#define _DAMAGEDESCRIPTION_H_
#include <string>

#include <NoNut/core/Class.h>
#include <NoNut/core/CustomTypes.h>

namespace nonut
{
	class DamageDescription : public Class
	{
	public:
		DamageDescription();
		explicit DamageDescription(SQObject object);

		// Properties
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

