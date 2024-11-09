import sqg2o

def getNearestWaypoint(world : str, x : int, y : int, z : int) -> dict:
    """
    This function is used to retrieve the information about nearest waypoint from the specified position.
    Original: [getNearestWaypoint](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/waypoint/getNearestWaypoint/)
    
    ## Declaration
    ```python
    def getNearestWaypoint(world : str, x : int, y : int, z : int) -> dict
    ```
    ## Parameters
    `str` **world**: the world name in which the waypoint exists.
    `int` **x**: the position in the world on the x axis.
    `int` **y**: the position in the world on the y axis.
    `int` **z**: the position in the world on the z axis.
    ## Returns
    `dict {name, x, y, z}`: Waypoint information.
    """
    return sqg2o.getNearestWaypoint(*locals())

def getWaypoint(world : str, name : str) -> dict:
    """
    This function is used to retrieve the position of specified waypoint.
    Original: [getWaypoint](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/waypoint/getWaypoint/)
    
    ## Declaration
    ```python
    def getWaypoint(world : str, name : str) -> dict
    ```
    ## Parameters
    `str` **world**: the world name in which the waypoint exists.
    `str` **name**: the name of the waypoint.
    ## Returns
    `dict {x, y, z}`: The position of waypoint.
    """
    return sqg2o.getWaypoint(*locals())