from ..server import PythonWebsocketServer
from ..call_repr import get_call_repr

async def getDistance2d(x1 : float, y1: float, x2 : float, y2 : float) -> float:
    """
    !!! note
        This functions supports ``pass_exception: bool`` optional argument for manual handling exceptions.
    This function will get the 2d distance between two points.
    Original: [getDistance2d](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/math/getDistance2d/)
    
    ## Declaration
    ```python
    async def getDistance2d(x1 : float, y1: float, x2 : float, y2 : float) -> float
    ```
    
    ## Parameters
    * `float` **x1**: the position on X axis of the first point.
    * `float` **y1**: the position on Y axis of the first point.
    * `float` **x2**: the position on X axis of the second point.
    * `float` **y2**: the position on Y axis of the second point.
    **OR**
    * `dict[str, float]` **first**: the poistion on XY axis of the first point.
    * `dict[str, float]` **second**: the position of XY axis of the second point.
    ## Returns
    `float`: Returns the calculated 2d distance between two points as floating point number.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getDistance3d(x1 : float, y1: float, z1 : float, x2 : float, y2 : float, z2 : float) -> float:
    """
    !!! note
        This functions supports ``pass_exception: bool`` optional argument for manual handling exceptions.
    This function will get the 3d distance between two points.
    Original: [getDistance3d](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/math/getDistance3d/)
    
    ## Declaration
    ```python
    async def getDistance3d(x1 : float, y1: float, z1 : float, x2 : float, y2 : float, z2 : float) -> float
    ```
    
    ## Parameters
    * `float` **x1**: the position on X axis of the first point.
    * `float` **y1**: the position on Y axis of the first point.
    * `float` **z1**: the position on Z axis of the first point.
    * `float` **x2**: the position on X axis of the second point.
    * `float` **y2**: the position on Y axis of the second point.
    * `float` **z2**: the position on Z axis of the second point.
    **OR**
    * `dict[str, float]` **first**: the position on XYZ axis of the first point.
    * `dict[str, float]` **second**: the position on XYZ axic of the second point.
    ## Returns
    `float`: Returns the calculated 3d distance between two points as floating point number.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getVectorAngle(x1 : float, y1: float, x2 : float, y2 : float) -> float:
    """
    !!! note
        This functions supports ``pass_exception: bool`` optional argument for manual handling exceptions.
    This function will get angle on Y axis directed towards the second point.
    Original: [getVectorAngle](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/math/getVectorAngle/)
    
    ## Declaration
    ```python
    async def getVectorAngle(x1 : float, y1: float, x2 : float, y2 : float) -> float
    ```
    
    ## Parameters
    * `float` **x1**: the position on X axis of the first point.
    * `float` **y1**: the position on Y axis of the first point.
    * `float` **x2**: the position on X axis of the second point.
    * `float` **y2**: the position on Y axis of the second point.
    **OR**
    * `dict[str, float]` **first**: the poistion on XY axis of the first point.
    * `dict[str, float]` **second**: the position of XY axis of the second point.
    ## Returns
    `float`: Returns the angle on Y axis directed towards the second point.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result
