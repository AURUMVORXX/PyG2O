import sqg2o

class Packet(sqg2o.Packet):
    def __init__(self):
        return super().__init__()
    
    def reset(self):
        return super().reset()
    
    def send(self, playerid : int, reliability : int):
        return super().send(playerid, reliability)
    
    def writeInt8(self, value : int):
        return super().writeInt8(value)
    
    def writeUInt8(self, value : int):
        return super().writeInt8(value)
    
    def writeInt16(self, value : int):
        return super().writeInt16(value)
    
    def writeUInt16(self, value : int):
        return super().writeInt16(value)
    
    def writeInt32(self, value : int):
        return super().writeInt32(value)
    
    def writeUInt32(self, value : int):
        return super().writeInt32(value)
    
    def writeBool(self, value : bool):
        return super().writeBool(value)
    
    def writeFloat(self, value : float):
        return super().writeFloat(value)
    
    def writeString(self, value : str):
        return super().writeString(value)
    
    def readInt8(self,) -> int:
        return super().readInt8()
    
    def readUInt8(self,) -> int:
        return super().readInt8()
    
    def readInt16(self) -> int:
        return super().readInt16()
    
    def readUInt16(self) -> int:
        return super().readInt16()
    
    def readInt32(self) -> int:
        return super().readInt32()
    
    def readUInt32(self) -> int:
        return super().readInt32()
    
    def readBool(self) -> bool:
        return super().readBool()
    
    def readFloat(self) -> float:
        return super().readFloat()
    
    def readString(self) -> str:
        return super().readString()
    
    @property
    def bitsUsed(self):
        return super().bitsUsed
    
    @property
    def bytesUsed(self):
        return super().bytesUsed