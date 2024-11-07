#include "CustomTypes.h"

#include "Array.h"
#include "Property.h"

namespace nonut
{
#define GET_SLOT(slot, type) slot = arrayWrapper.get<type>(#slot)

	void GameTime::convert(SQObject object)
	{
		Array arrayWrapper(object);
		GET_SLOT(day, Int);
		GET_SLOT(hour, Int);
		GET_SLOT(min, Int);
	}

	void Position2d::convert(SQObject object)
	{
		Array arrayWrapper(object);
		GET_SLOT(x, Int);
		GET_SLOT(y, Int);
	}

	void Position3d::convert(SQObject object)
	{
		Array arrayWrapper(object);
		GET_SLOT(x, Float);
		GET_SLOT(y, Float);
		GET_SLOT(z, Float);
	}

	void Size2d::convert(SQObject object)
	{
		Array arrayWrapper(object);
		GET_SLOT(width, Int);
		GET_SLOT(height, Int);
	}

	void Rect::convert(SQObject object)
	{
		Array arrayWrapper(object);
		GET_SLOT(x, Int);
		GET_SLOT(y, Int);
		GET_SLOT(width, Int);
		GET_SLOT(height, Int);
	}

	void UV::convert(SQObject object)
	{
		Array arrayWrapper(object);
		GET_SLOT(x, Float);
		GET_SLOT(y, Float);
		GET_SLOT(width, Float);
		GET_SLOT(height, Float);
	}

	void Resolution::convert(SQObject object)
	{
		Array arrayWrapper(object);
		GET_SLOT(x, Int);
		GET_SLOT(y, Int);
		GET_SLOT(bpp, Int);
	}

	void Item::convert(SQObject object)
	{
		Array arrayWrapper(object);
		GET_SLOT(instance, Int);
		GET_SLOT(amount, Int);
		GET_SLOT(name, String);
	}

	void Color::convert(SQObject object)
	{
		Array arrayWrapper(object);
		GET_SLOT(r, Int);
		GET_SLOT(g, Int);
		GET_SLOT(b, Int);
	}

	void BodyVisual::convert(SQObject object)
	{
		Array arrayWrapper(object);
		GET_SLOT(bodyModel, String);
		GET_SLOT(bodyTxt, Int);
		GET_SLOT(headModel, String);
		GET_SLOT(headTxt, Int);
	}

	void NetworkStats::convert(SQObject object)
	{
		Array arrayWrapper(object);
		GET_SLOT(packetReceived, Int);
		GET_SLOT(packetlossTotal, Int);
		GET_SLOT(packetlossLastSecond, Int);
		GET_SLOT(messagesInResendBuffer, Int);
		GET_SLOT(messageInSendBuffer, Int);
		GET_SLOT(bytesInResendBuffer, Int);
		GET_SLOT(bytesInSendBuffer, Int);
	}

	void Position3dWithName::convert(SQObject object)
	{
		Array arrayWrapper(object);
		GET_SLOT(name, String);
		GET_SLOT(x, Float);
		GET_SLOT(y, Float);
		GET_SLOT(z, Float);
	}
	
	void SqDict::convert(SQObject object)
	{
		Sqrat::Table tab = Sqrat::Table(object);
		Sqrat::Object::iterator tabIterator;
		int i = 0;
		
		while (tab.Next(tabIterator))
		{
			HSQOBJECT key   = tabIterator.getKey();
			HSQOBJECT value = tabIterator.getValue();
			
			if (key._type != OT_STRING)
				continue;
			
			if (value._type == OT_STRING)
				data[sq_objtostring(&key)] = sq_objtostring(&value);
			else if (value._type == OT_INTEGER)
				data[sq_objtostring(&key)] = sq_objtointeger(&value);
			else if (value._type == OT_FLOAT)
				data[sq_objtostring(&key)] = sq_objtofloat(&value);
			else if (value._type == OT_TABLE)
			{
				SqDict result = SqDict();
				result.convert(value);
				data[sq_objtostring(&key)] = result.data;
			}
		}
	}
}
