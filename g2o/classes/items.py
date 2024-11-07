import sqg2o

class ItemsGround:
    
    @staticmethod
    def getById(id : int):
        return sqg2o.ItemsGround.getById(id)
    
    @staticmethod
    def create(data : dict) -> int:
        return sqg2o.ItemsGround.create(data)
    
    @staticmethod
    def destroy(id : int):
        sqg2o.ItemsGround.destroy(id)

class ItemGround(sqg2o.ItemGround):
    """
    This class represents item on the ground.
    Original: [ItemGround](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-classes/item/ItemGround//)
    
    ## `int` id *(read-only)*
    Represents the unique id of the item ground.

    ## `str` instance *(read-only)*
    Represents the item instance of the item ground.
    
    ## `int` amount *(read-only)*
    Represents the item amount of item ground.
    
    ## `str` world *(read-only)*
    Represents the item ground world (.ZEN file path).
    
    ## `int` virtualWorld
    Represents the virtual world of item ground.
    """
    def __init__(self):
        return super().__init__()
    
    def getPosition() -> tuple:
        """
        This method will get the item ground position on the world.
        **Returns `tuple(float, float, float)`:**
        `X-Y-Z` item ground position on the world.
        """
        return super().getPosition()
    
    def getRotation() -> tuple:
        """
        This method will get the item ground rotation on the world.
        **Returns `tuple(float, float, float)`:**
        `X-Y-Z` item ground roration on the world.
        """
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