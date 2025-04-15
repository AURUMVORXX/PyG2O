from ..server import PythonWebsocketServer

class Daedalus:
    """
    This class represents Daedalus scripting interface.
    Original: [Daedalus](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-classes/game/Daedalus/)
    """
    @staticmethod
    async def index(value : str) -> int:
        """
        This method will get the daedalus symbol index by its name.
        **Parameters:**
        * `str` **name**: the name of the daedalus symbol.
        
        **Returns `int`:**
        the daedalus symbol index number.
        """
        data = f'return Daedalus.index({value})'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    @staticmethod
    async def symbol(value : str) -> dict:
        """
        This method will get the daedalus symbol by its name.
        **Parameters:**
        * `str` **name**: the name of the daedalus symbol.
        
        **Returns `dict`:**
        the daedalus symbol (empty if there's no symbol with given name)
        """
        data = f'return Daedalus.symbol({value})'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    @staticmethod
    async def instance(value : str) -> dict:
        """
        This method will get the all of the daedalus instance variables.
        **Parameters:**
        * `str` **instanceName**: the name of the daedalus instance.
        
        **Returns `dict`:**
        the object containing all of the daedalus instance variables.
        """
        data = f'return Daedalus.instance({value})'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result