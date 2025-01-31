#include <CommonHeader.h>
#include "Packet.h"

namespace nonut
{
	Packet::Packet() :
		Class("Packet"),
		METHOD_CTOR(reset),
		METHOD_CTOR(send),
		METHOD_CTOR(sendToAll),
		METHOD_CTOR(writeBool),
		METHOD_CTOR(writeInt8),
		METHOD_CTOR(writeUInt8),
		METHOD_CTOR(writeInt16),
		METHOD_CTOR(writeUInt16),
		METHOD_CTOR(writeInt32),
		METHOD_CTOR(writeUInt32),
		METHOD_CTOR(writeFloat),
		METHOD_CTOR(writeString),
		METHOD_CTOR(readBool),
		METHOD_CTOR(readInt8),
		METHOD_CTOR(readUInt8),
		METHOD_CTOR(readInt16),
		METHOD_CTOR(readUInt16),
		METHOD_CTOR(readInt32),
		METHOD_CTOR(readUInt32),
		METHOD_CTOR(readFloat),
		METHOD_CTOR(readString),
		
		PROPERTY_CTOR(bitsUsed),
		PROPERTY_CTOR(bytesUsed)
	{
		classCtor();
	}

	Packet::Packet(SQObject object) :
		Class("Packet", object),
		METHOD_CTOR(reset),
		METHOD_CTOR(send),
		METHOD_CTOR(sendToAll),
		METHOD_CTOR(writeBool),
		METHOD_CTOR(writeInt8),
		METHOD_CTOR(writeUInt8),
		METHOD_CTOR(writeInt16),
		METHOD_CTOR(writeUInt16),
		METHOD_CTOR(writeInt32),
		METHOD_CTOR(writeUInt32),
		METHOD_CTOR(writeFloat),
		METHOD_CTOR(writeString),
		METHOD_CTOR(readBool),
		METHOD_CTOR(readInt8),
		METHOD_CTOR(readUInt8),
		METHOD_CTOR(readInt16),
		METHOD_CTOR(readUInt16),
		METHOD_CTOR(readInt32),
		METHOD_CTOR(readUInt32),
		METHOD_CTOR(readFloat),
		METHOD_CTOR(readString),
		
		PROPERTY_CTOR(bitsUsed),
		PROPERTY_CTOR(bytesUsed)
	{
	}
}
