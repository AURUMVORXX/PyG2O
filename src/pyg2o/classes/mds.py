from ..server import PythonWebsocketServer

class Mds:
    """
    This class represents mds manager for conversion between mds id & mds instance. This manager will work for every registered mds in `mds.xml` file.
    Original: [Mds](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-classes/mds/Mds/)
    """
    @staticmethod
    async def id(mdsName : str) -> int:
        """
        This method will convert the mds name to mds id.
        **Parameters:**
        * `str` **mdsName**: the mds name, e.g: `"HumanS_Sprint.mds"`.
        
        **Returns `int`:**
        the unique mds id.
        """
        data = f'return Mds.id({mdsName})'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    @staticmethod
    async def name(mdsId : int) -> str:
        """
        This method will convert the mds id to mds name.
        **Parameters:**
        * `int` **mdsId**: the mds id.
        
        **Returns `str`:**
        the mds name, e.g: `"HumanS_Sprint.mds"`.
        """
        data = f'return Mds.id({mdsId})'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result