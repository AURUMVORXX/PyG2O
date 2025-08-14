from ..server import PythonWebsocketServer
from ..call_repr import get_call_repr

async def getHostname() -> str:
    """
    This function will get the hostname of the server.
    Original: [getHostname](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/game/getHostname/)
    
    ## Declaration
    ```python
    async def getHostname() -> str
    ```
    ## Returns
    `str`: Server hostname.
    
    ## Usage
    ```python
    import g2o
    
    @g2o.event('onInit')
    def evtInit(**kwargs):
        print('Server hostname:', g2o.getHostname())
    ```
    """
    
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getOnlinePlayers():
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result
    
async def getMaxSlots() -> int:
    """
    This function will get the max number of slots available on the server.
    Original: [getMaxSlots](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/game/getMaxSlots/)
    
    ## Declaration
    ```python
    async def getMaxSlots() -> int
    ```
    ## Returns
    `int`: Max slots number on the server.
    
    ## Usage
    ```python
    import g2o
    
    @g2o.event('onInit')
    def evtInit(**kwargs):
        print('Server max slots:', g2o.getMaxSlots())
    ```
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayersCount() -> int:
    """
    This function will get the max number of slots available on the server.
    Original: [getPlayersCount](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/game/getPlayersCount/)
    
    ## Declaration
    ```python
    async def getPlayersCount() -> int
    ```
    ## Returns
    `int`: Number of players on the server.
    
    ## Usage
    ```python
    import g2o
    
    @g2o.event('onInit')
    def evtInit(**kwargs):
        print('Players online:', g2o.getPlayersCount())
    ```
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getServerPublic() -> bool:
    """
    This function will get the publicity state of the server.
    
    ## Declaration
    ```python
    async def getServerPublic() -> bool
    ```
    ## Returns
    `bool`: ``true`` if server is publicly available, otherwise ``false``
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def exit(exitCode : int = 0):
    """
    This function will close the server with specified exit code.
    Original: [exit](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/exit/)
    
    ## Declaration
    ```python
    async def exit(exitCode : int = 0)
    ```
    ## Parameters
    * `int` **exitCode**: exit status for g2o server.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getDayLength() -> float:
    """
    The function is used to get the day length in miliseconds.
    Original: [getDayLength](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/getDayLength/)
    
    ## Declaration
    ```python
    async def getDayLength() -> float
    ```
    ## Returns
    `float`: the current day length in miliseconds.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getServerDescription() -> str:
    """
    This function will get the description of the server.
    Original: [getServerDescription](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/getServerDescription/)
    
    ## Declaration
    ```python
    async def getServerDescription() -> str
    ```
    ## Returns
    `str`: Server description.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getServerWorld() -> str:
    """
    The function is used to get the path of the default world on the server.
    Original: [getServerWorld](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/getServerWorld/)
    
    ## Declaration
    ```python
    async def getServerWorld() -> str
    ```
    ## Returns
    `str`: The world path name.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getTime() -> tuple:
    """
    The function is used to get the path of the default world on the server.
    Original: [getTime](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/getTime/)
    
    ## Declaration
    ```python
    async def getTime() -> tuple
    ```
    ## Returns
    `tuple (day, hour, min)`: The current time in the game.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return (result['day'], result['hour'], result['min'])

async def serverLog(text : str):
    """
    This function will log the text into server.log file.
    Original: [serverLog](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/serverLog/)
    
    ## Declaration
    ```python
    async def serverLog(text : str)
    ```
    ## Parameters
    `str` **text**: the text message that you want to append to server.log file.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setDayLength(miliseconds : float):
    """
    !!! note
        Day length can't be smaller than 10 000 miliseconds.
        
    This function will set the day length in miliseconds.
    Original: [setDayLength](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/setDayLength/)
    
    ## Declaration
    ```python
    async def setDayLength(miliseconds : float)
    ```
    ## Parameters
    `float` **miliseconds**: day length in miliseconds.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setServerDescription(description : str):
    """
    This function will set the description of the server.
    Original: [setServerDescription](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/setServerDescription/)
    
    ## Declaration
    ```python
    async def setServerDescription(description : str)
    ```
    ## Parameters
    `str` **description**: the server description.
    ## Returns
    `bool`: `true` if server description was set successfully, otherwise `false`.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setServerWorld(world : str):
    """
    !!! note
        The server world limit is set to 32 characters.
    
    !!! note
        If the target world path is written with backslashes instead of normal slashes, you need to escape it with another backslashes e.g. "NEWWORLD\\NEWWORLD.ZEN".
        
    This function will change the default world to which players will enter after joining.
    Original: [setServerWorld](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/setServerWorld/)
    
    ## Declaration
    ```python
    async def setServerWorld(world : str)
    ```
    ## Parameters
    `str` **world**: the path to the target world.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setServerPublic(public : str):
    """
    This function will change the publicity state of the server.
    
    ## Declaration
    ```python
    async def setServerPublic(public : str)
    ```
    ## Parameters
    `bool` **public**: server public state.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setTime(hour : int, min : int, day : int = 0):
    """
    !!! note
        This functions supports ``pass_exception: bool`` optional argument for manual handling exceptions.
    This function will set the current time in the game to the given time, for all the players.
    Original: [setTime](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/setTime/)
    
    ## Declaration
    ```python
    async def setTime(hour : int, min : int, day : int = 0)
    ```
    ## Parameters
    `int` **hour**: the hour of new time (in the range between 0-23) or subtract value from hour (hour < 0).
    `int` **mins**: the minute of new time (in the range between 0-59) or subtract value from mins (mins < 0).
    `int` **day**: the day of new time or subtract value from day (day < 0).
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result
