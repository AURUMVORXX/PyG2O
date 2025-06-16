from ..server import PythonWebsocketServer

class ItemsGround:
    """
    This class represents item ground manager.
    Original: [ItemsGround](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-classes/item/ItemsGround/)
    """
    @staticmethod
    async def getById(id : int):
        """
        This method will retrieve the item ground object by its unique id.
        
        **Parameters:**
        * `int` **itemGroundId**: the unique item ground id.
        
        **Returns `ItemGround`:**
        the item ground object or `throws an exception` if the object cannot be found.
        """
        data = f'return ItemsGround.getById({id})'
        
        # TODO: Добавить десериализацию ItemGround
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    @staticmethod
    async def create(data : dict) -> int:
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
        data = f'return ItemsGround.create({data})'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    @staticmethod
    async def destroy(id : int):
        """
        This method will destroy the item ground by it's unique id.
        **Parameters:**
        * `int` **itemGroundId**: the item ground unique id.
        """
        data = f'return ItemsGround.destroy({id})'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result

class ItemGround:
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
        self._id = -1
        self._instance = ''
        self._amount = -1
        self._world = -1
        self._virtualWorld = -1
        self._position = -1
        self._rotation = -1
    
    def getPosition(self) -> dict:
        """
        This method will get the item ground position on the world.
        **Returns `tuple(float, float, float)`:**
        `X-Y-Z` item ground position on the world.
        """
        return self._position
    
    def getRotation(self) -> dict:
        """
        This method will get the item ground rotation on the world.
        **Returns `tuple(float, float, float)`:**
        `X-Y-Z` item ground roration on the world.
        """
        return self._rotation
    
    async def setPosition(self, x: float, y: float, z: float):
        """
        This method will set the item ground position in the world.
        **Parameters:**
        * `float` **x**: the position in the world on the x axis.
        * `float` **y**: the position in the world on the y axis.
        * `float` **z**: the position in the world on the z axis.
        """
        data = f'return ItemsGround.getById({self.id}).setPosition({x}, {y}, {z})'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    async def setRotation(self, x: float, y: float, z: float):
        """
        This method will set the item ground rotation in the world.
        **Parameters:**
        * `float` **x**: the rotation in the world on the x axis.
        * `float` **y**: the rotation in the world on the y axis.
        * `float` **z**: the rotation in the world on the z axis.
        """
        data = f'return ItemsGround.getById({self.id}).setRotation({x}, {y}, {z})'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    async def get_physicsEnabled(self) -> bool:
        """
        This method will get the item ground physicsEnabled flag.
        **Returns:**
        * `bool`: ``true`` if physics is enabled, otherwise ``false``
        """
        data = f'return ItemsGround.getById({self.id}).physicsEnabled'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    async def set_physicsEnabled(self, enabled: bool):
        """
        This method will set the item ground physicsEnabled flag.
        **Parameters:**
        * `bool` **enabled**: represents the state of physicsEnabled flag
        """
        data = f'return ItemsGround.getById({self.id}).physicsEnabled = {enabled}'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def instance(self) -> str:
        return self._instance
    
    @property
    def amount(self) -> int:
        return self._amount
    
    @property
    def world(self) -> str:
        return self._world
    
    @property
    def virtualWorld(self) -> int:
        return self._virtualWorld
    
    @virtualWorld.setter
    def virtualWorld(self, value):
        self._virtualWorld = value
        
    def _initialize(self, **kwargs):
        self.__dict__.update(kwargs)