from ..server import PythonWebsocketServer
from ..call_repr import get_call_repr
from typing import Optional

async def getNearestWaypoint(world : str, x : int, y : int, z : int, distance: int = -1) -> Optional[tuple]:
    """
    This function is used to retrieve the information about nearest waypoint from the specified position.
    Original: [getNearestWaypoint](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/waypoint/getNearestWaypoint/)
    
    ## Declaration
    ```python
    async def getNearestWaypoint(world : str, x : int, y : int, z : int) -> Optional[tuple]
    ```
    ## Parameters
    `str` **world**: the world name in which the waypoint exists.
    `int` **x**: the position in the world on the x axis.
    `int` **y**: the position in the world on the y axis.
    `int` **z**: the position in the world on the z axis.
    ## Returns
    `tuple (name, x, y, z)`: Waypoint information.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return (result['name'], result['x'], result['y'], result['z']) if result is not None else (None, None, None)

async def getWaypoint(world : str, name : str) -> Optional[tuple]:
    """
    This function is used to retrieve the position of specified waypoint.
    Original: [getWaypoint](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/waypoint/getWaypoint/)
    
    ## Declaration
    ```python
    async def getWaypoint(world : str, name : str) -> Optional[tuple]
    ```
    ## Parameters
    `str` **world**: the world name in which the waypoint exists.
    `str` **name**: the name of the waypoint.
    ## Returns
    `dict {x, y, z}`: The position of waypoint.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return (result['x'], result['y'], result['z']) if result is not None else (None, None, None)
