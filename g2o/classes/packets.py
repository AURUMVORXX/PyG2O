import sqg2o

class Packet(sqg2o.Packet):
    """
    This class represents data packet that gets send over the network.
    Original: [Packet](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-classes/network/Packet/)
    
    ## `int` bitsUsed *(read-only)*
    Represents the total number of bits used by the script packet data.

    ## `int` bytesUsed *(read-only)*
    Represents the total number of bytes used by the script packet data.
    """
    def __init__(self):
        return super().__init__()
    
    def reset(self):
        """
        This method will clear the packet data, making it empty.
        """
        return super().reset()
    
    def send(self, playerid : int, reliability : int):
        """
        This method will send the packet data to the specified player.
        **Parameters:**
        * `int` **playerid**: the id of the player to whom you want to send the packet.
        * `int` **reliability**: the reliability type, for more information see [Reliability](../../constants/reliability.md).
        """
        return super().send(playerid, reliability)
    
    def sendToAll(self, reliability : int):
        """
        This method will send the packet data to the specified player.
        **Parameters:**
        * `int` **reliability**: the reliability type, for more information see [Reliability](../../constants/reliability.md).
        """
        return super().send(playerid, reliability)
    
    def writeInt8(self, value : int):
        """
        This method will append signed int8 value to the packet. (1 byte)
        **Parameters:**
        * `int` **value**: the number value in range -128 to 127.
        """
        return super().writeInt8(value)
    
    def writeUInt8(self, value : int):
        """
        This method will append unsigned int8 value to the packet. (1 byte)
        **Parameters:**
        * `int` **value**: the number value in range 0 to 255.
        """
        return super().writeInt8(value)
    
    def writeInt16(self, value : int):
        """
        This method will append signed int16 value to the packet. (2 bytes)
        **Parameters:**
        * `int` **value**: the number value in range -32768 to 32767.
        """
        return super().writeInt16(value)
    
    def writeUInt16(self, value : int):
        """
        This method will append unsigned int16 value to the packet. (2 bytes)
        **Parameters:**
        * `int` **value**: the number value in range 0 to 65535.
        """
        return super().writeInt16(value)
    
    def writeInt32(self, value : int):
        """
        This method will append signed int32 value to the packet. (4 bytes)
        **Parameters:**
        * `int` **value**: the number value in range -2147483648 to 2147483647.
        """
        return super().writeInt32(value)
    
    def writeUInt32(self, value : int):
        """
        !!! note
            By default squirrel uses int32 values, which means that this method behaves exactly the same as [writeInt32](Packet.md#g2o.classes.packets.Packet.writeInt32) in scripts.
        This method will append unsigned int32 value to the packet. (4 bytes)
        **Parameters:**
        * `int` **value**: the number value in range 0 to 4294967295.
        """
        return super().writeInt32(value)
    
    def writeBool(self, value : bool):
        """
        This method will append boolean value to the packet. (1 bit)
        **Parameters:**
        * `bool` **value**: the boolean value.
        """
        return super().writeBool(value)
    
    def writeFloat(self, value : float):
        """
        This method will append float value to the packet. (4 bytes)
        **Parameters:**
        * `float` **value**: the number value.
        """
        return super().writeFloat(value)
    
    def writeString(self, value : str):
        """
        !!! note
            The amount of bytes appended to the packet depends on the length of string, 1 byte = 1 char.
        This method will append string value to the packet.
        **Parameters:**
        * `str` **value**: the text value.
        """
        return super().writeString(value)
    
    def readInt8(self,) -> int:
        """
        This method will get signed int8 value from the packet. (1 byte)
        **Returns `int`:**
        the number value in range -128 to 127.
        """
        return super().readInt8()
    
    def readUInt8(self,) -> int:
        """
        This method will get unsigned int8 value from the packet. (1 byte)
        **Returns `int`:**
        the number value in range 0 to 255.
        """
        return super().readInt8()
    
    def readInt16(self) -> int:
        """
        This method will get signed int16 value from the packet. (2 bytes)
        **Returns `int`:**
        the number value in range -32768 to 32767.
        """
        return super().readInt16()
    
    def readUInt16(self) -> int:
        """
        This method will get unsigned int16 value from the packet. (2 bytes)
        **Returns `int`:**
        the number value in range 0 to 65535.
        """
        return super().readInt16()
    
    def readInt32(self) -> int:
        """
        This method will get signed int32 value from the packet. (4 bytes)
        **Returns `int`:**
        the number value in range -2147483648 to 2147483647.
        """
        return super().readInt32()
    
    def readUInt32(self) -> int:
        """
        This method will get unsigned int32 value from the packet. (4 bytes)
        **Returns `int`:**
        the number value in range 0 to 4294967295.
        """
        return super().readInt32()
    
    def readBool(self) -> bool:
        """
        This method will get signed int8 value from the packet. (1 byte)
        **Returns `bool`:**
        the boolean value.
        """
        return super().readBool()
    
    def readFloat(self) -> float:
        """
        This method will get float value from the packet. (4 bytes)
        **Returns `float`:**
        the number value.
        """
        return super().readFloat()
    
    def readString(self) -> str:
        """
        !!! note
            The amount of bytes appended to the packet depends on the length of string, 1 byte = 1 char.
        This method will get string value from the packet.
        **Returns `str`:**
        the text value.
        """
        return super().readString()
    
    @property
    def bitsUsed(self):
        return super().bitsUsed
    
    @property
    def bytesUsed(self):
        return super().bytesUsed