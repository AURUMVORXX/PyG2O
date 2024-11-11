
import sqg2o

class Way(sqg2o.Way):
    """
    This class represents Way constructed from waypoints.
    Original: [Way](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-classes/waypoint/Way/)
    
    ## `str` start *(read-only)*
    Represents the start waypoint for Way.
    
    ## `str` end *(read-only)*
    Represents the end waypoint for Way.
    """
    def __init__(self, world : str, startWp : str, endWp : str):
        """
        ## Parameters
        `str` **world**: the name of the world from config.xml.
        `str` **startWp**: the name of the start waypoint.
        `str` **endWp**: the name of the end waypoint.
        """
        return super().__init__(world, startWp, endWp)
        
    def getWaypoints(self) -> list:
        """
        This method will get the all waypoints between startWp & endWp.
        
        ## Returns
        `list [str]`: the list containing the names of all of the Way waypoints.
        """
        return super().getWaypoints()
    
    def getCountWaypoints(self):
        """
        This method will get the number of waypoints between start waypoint & end waypoint.
        
        ## Returns
        `int`: the number of waypoints.
        """
        return super().getCountWaypoints()
    
    @property
    def start(self):
        return super().start
    
    @property
    def end(self):
        return super().end