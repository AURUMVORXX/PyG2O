import sqg2o

class ItemsGround:
    """
    This class represents item ground manager.
    Original: [ItemsGround](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-classes/item/ItemsGround/)
    """
    @staticmethod
    def getById(id : int):
        """
        This method will retrieve the item ground object by its unique id.
        
        **Parameters:**
        * `int` **itemGroundId**: the unique item ground id.
        
        **Returns `ItemGround`:**
        the item ground object or `throws an exception` if the object cannot be found.
        """
        return sqg2o.ItemsGround.getById(id)
    
    @staticmethod
    def create(data : dict) -> int:
        """
        This method will create the item ground.
        
        **Parameters:**
        * `dict {instance, amount=1, physicsEnabled=false position={x=0,y=0,z=0}, rotation={x=0,y=0,z=0}, world=CONFIG_WORLD, virtualWorld=0}`:
        * `string` **instance**: the scripting instance of game item.
        * `bool` **physicsEnabled**: the physics state of the item ground.
        * `dict {x, y, z}` **position**: the position of the item ground in the world.
        * `dict {x, y, z}` **rotation**: the rotation of the item ground in the world.
        * `string` **world**: the world the item ground is in (.ZEN file path).
        * `int` **virtualWorld**: the virtual world id in range <0, 65535>.
        
        **Returns `int`:**
        the item ground id.
        """
        return sqg2o.ItemsGround.create(data)
    
    @staticmethod
    def destroy(id : int):
        """
        This method will destroy the item ground by it's unique id.
        **Parameters:**
        * `int` **itemGroundId**: the item ground unique id.
        """
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