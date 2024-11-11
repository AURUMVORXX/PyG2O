import sqg2o

def getDistance2d(x1 : float, y1: float, x2 : float, y2 : float) -> float:
    """
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
    ## Returns
    `float`: Returns the calculated 2d distance between two points as floating point number.
    """
    return sqg2o.getDistance2d(x1, y1, x2, y2)

def getDistance3d(x1 : float, y1: float, z1 : float, x2 : float, y2 : float, z2 : float) -> float:
    """
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
    ## Returns
    `float`: Returns the calculated 3d distance between two points as floating point number.
    """
    return sqg2o.getDistance3d(x1, y1, z1, x2, y2, z2)

def getVectorAngle(x1 : float, y1: float, x2 : float, y2 : float) -> float:
    """
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
    ## Returns
    `float`: Returns the angle on Y axis directed towards the second point.
    """
    return sqg2o.getVectorAngle(x1, y1, x2, y2)