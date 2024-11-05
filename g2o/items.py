import sqg2o

class ItemGround(sqg2o.ItemGround):
    def __init__(self):
        return super().__init__()
    
    def getPosition() -> tuple:
        return super().getPosition()
    
    def getRotation() -> tuple:
        return super().getRotation()
    
    @property
    def id(self):
        return super().id
    
    @property
    def instance(self):
        return super().instance
    
    @property
    def amount(self):
        return super().amount
    
    @property
    def world(self):
        return super().world
    
    @property
    def virtualWorld(self):
        return super().virtualWorld
    
    @virtualWorld.setter
    def virtualWorld(self, value):
        super().virtualWorld = value