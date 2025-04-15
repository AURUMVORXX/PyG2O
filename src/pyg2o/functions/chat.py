from ..server import PythonWebsocketServer
from ..call_repr import get_call_repr

async def sendMessageToAll(r : int, g : int, b : int, text : str):
    """
    This function will send a chat message to every connected player.
    Sending a message triggers client side event [onPlayerMessage](../../defaultEvents/player/onPlayerMessage.md) with playerid set as `-1`.
    Original: [sendMessageToAll](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/chat/sendMessageToAll/)
    
    ## Declaration
    ```python
    async def sendMessageToAll(r : int, g : int, b : int, text : str)
    ```
    
    ## Parameters
    * `int` **r**: the red color component in RGB model.
    * `int` **g**: the green color component in RGB model.
    * `int` **b**: the blue color component in RGB model.
    * `str` **text**: that will be send.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def sendMessageToPlayer(playerid : int, r : int, g : int, b : int, text : str):
    """
    This function will send a chat message to specific player.
    Sending a message triggers client side event [onPlayerMessage](../../defaultEvents/player/onPlayerMessage.md) with playerid set as `-1`.
    Original: [sendMessageToPlayer](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/chat/sendMessageToPlayer/)
    
    ## Declaration
    ```python
    async def sendMessageToPlayer(playerid : int, r : int, g : int, b : int, text : str)
    ```
    
    ## Parameters
    * `int` **playerid**: the id of the player which will receive a message.
    * `int` **r**: the red color component in RGB model.
    * `int` **g**: the green color component in RGB model.
    * `int` **b**: the blue color component in RGB model.
    * `str` **text**: that will be send.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def sendPlayerMessageToAll(senderid : int, r : int, g : int, b : int, text : str):
    """
    This function will send a chat message from one player to every player. Sending a message
    Sending a message triggers client side event [onPlayerMessage](../../defaultEvents/player/onPlayerMessage.md) with playerid set as **senderid**.
    Original: [sendPlayerMessageToAll](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/chat/sendPlayerMessageToAll/)
    
    ## Declaration
    ```python
    async def sendPlayerMessageToAll(senderid : int, r : int, g : int, b : int, text : str)
    ```
    
    ## Parameters
    * `int` **senderid**: the id of the player which will send a message.
    * `int` **r**: the red color component in RGB model.
    * `int` **g**: the green color component in RGB model.
    * `int` **b**: the blue color component in RGB model.
    * `str` **text**: that will be send.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def sendPlayerMessageToPlayer(senderid : int, receiverid : int, r : int, g : int, b : int, text : str):
    """
    This function will send a chat message from one player to another player.
    Sending a message triggers client side event [onPlayerMessage](../../defaultEvents/player/onPlayerMessage.md) with playerid set as **senderid**.
    Original: [sendPlayerMessageToPlayer](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/chat/sendPlayerMessageToPlayer/)
    
    ## Declaration
    ```python
    async def sendPlayerMessageToPlayer(senderid : int, receiverid : int, r : int, g : int, b : int, text : str)
    ```
    
    ## Parameters
    * `int` **senderid**: the id of the player which will send a message.
    * `int` **receiverid**: the id of the player which will receive a message.
    * `int` **r**: the red color component in RGB model.
    * `int` **g**: the green color component in RGB model.
    * `int` **b**: the blue color component in RGB model.
    * `str` **text**: that will be send.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result