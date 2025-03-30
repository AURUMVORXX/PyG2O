import sqg2o
from g2o.exception import handle_exception

@handle_exception
def getDistance2d(
    x1: float = 0, 
    y1: float = 0, 
    x2: float = 0, 
    y2 : float = 0, 
    first: dict[str, float] = None, 
    second: dict[str, float] = None
) -> float:
    """
    !!! note
        This functions supports ``pass_exception: bool`` optional argument for manual handling exceptions.
    This function will get the 2d distance between two points.
    Original: [getDistance2d](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/math/getDistance2d/)
    
    ## Declaration
    ```python
    def getDistance2d(x1 : float, y1: float, x2 : float, y2 : float) -> float
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
    if first is not None and second is not None:
        return sqg2o.getDistance2d(first['x'], first['y'], second['x'], second['y'])
    else:
        return sqg2o.getDistance2d(x1, y1, x2, y2)

@handle_exception
def getDistance3d(
    x1 : float = 0, 
    y1: float = 0, 
    z1 : float = 0, 
    x2 : float = 0, 
    y2 : float = 0, 
    z2 : float = 0, 
    first: dict[str, float] = None, 
    second: dict[str, float] = None
) -> float:
    """
    !!! note
        This functions supports ``pass_exception: bool`` optional argument for manual handling exceptions.
    This function will get the 3d distance between two points.
    Original: [getDistance3d](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/math/getDistance3d/)
    
    ## Declaration
    ```python
    def getDistance3d(x1 : float, y1: float, z1 : float, x2 : float, y2 : float, z2 : float) -> float
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
    if first is not None and second is not None:
        return sqg2o.getDistance3d(first['x'], first['y'], first['z'], second['x'], second['y'], second['z'])
    else:
        return sqg2o.getDistance3d(x1, y1, z1, x2, y2, z2)

@handle_exception
def getVectorAngle(
    x1: float = 0, 
    y1: float = 0, 
    x2: float = 0, 
    y2 : float = 0, 
    first: dict[str, float] = None, 
    second: dict[str, float] = None
) -> float:
    """
    !!! note
        This functions supports ``pass_exception: bool`` optional argument for manual handling exceptions.
    This function will get angle on Y axis directed towards the second point.
    Original: [getVectorAngle](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/math/getVectorAngle/)
    
    ## Declaration
    ```python
    def getVectorAngle(x1 : float, y1: float, x2 : float, y2 : float) -> float
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
    if first is not None and second is not None:
        return sqg2o.getVectorAngle(first['x'], first['y'], second['x'], second['y'])
    else:
        return sqg2o.getVectorAngle(x1, y1, x2, y2)