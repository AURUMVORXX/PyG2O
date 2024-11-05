#ifndef _PYPACKET_H_
#define _PYPACKET_H_

#include <classes/sq/Packet.h>

class PyPacket
{
private:
    nonut::Packet *sqpacket;
    
public:
    PyPacket()                                  { sqpacket = new nonut::Packet(); };
    PyPacket(SQObject obj)                      { sqpacket = new nonut::Packet(obj); }
    
    void reset()                                { sqpacket->reset(); }
    void send(nonut::Int id, nonut::Int value)  { sqpacket->send(id, value); }
    void sendToAll(nonut::Int value)            { sqpacket->sendToAll(value); };
    
    void writeInt8(nonut::Int value)            { sqpacket->writeInt8(value); }
    void writeUInt8(nonut::Int value)           { sqpacket->writeUInt8(value); }
    void writeInt16(nonut::Int value)           { sqpacket->writeInt16(value); }
    void writeUInt16(nonut::Int value)          { sqpacket->writeUInt16(value); }
    void writeInt32(nonut::Int value)           { sqpacket->writeInt32(value); }
    void writeUInt32(nonut::Int value)          { sqpacket->writeUInt32(value); }
    
    void writeBool(nonut::Bool value)           { sqpacket->writeBool(value); }
    void writeFloat(nonut::Float value)         { sqpacket->writeFloat(value); }
    void writeString(nonut::String value)       { sqpacket->writeString(value); }
    
    nonut::Int readInt8()                       { return sqpacket->readInt8(); }
    nonut::Int readUInt8()                      { return sqpacket->readUInt8(); }
    nonut::Int readInt16()                      { return sqpacket->readInt16(); }
    nonut::Int readUInt16()                     { return sqpacket->readUInt16(); }
    nonut::Int readInt32()                      { return sqpacket->readInt32(); }
    nonut::Int readUInt32()                     { return sqpacket->readUInt32(); }
    
    nonut::Bool readBool()                      { return sqpacket->readBool(); }
    nonut::Float readFloat()                    { return sqpacket->readFloat(); }
    nonut::String readString()                  { return sqpacket->readString(); }
    
    nonut::Int getBitsUsed()                    { return sqpacket->bitsUsed; }
    nonut::Int getBytesUsed()                   { return sqpacket->bytesUsed; }
    
    void del()                                  { delete sqpacket; }
};

#endif