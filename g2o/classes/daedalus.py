import sqg2o

class Daedalus:
    """
    This class represents Daedalus scripting interface.
    Original: [Daedalus](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-classes/game/Daedalus/)
    """
    @staticmethod
    def index(value : str) -> int:
        """
        This method will get the daedalus symbol index by its name.
        **Parameters:**
        * `str` **name**: the name of the daedalus symbol.
        
        **Returns `int`:**
        the daedalus symbol index number.
        """
        return sqg2o.Daedalus.index(value)
    
    @staticmethod
    def symbol(value : str) -> dict:
        """
        This method will get the daedalus symbol by its name.
        **Parameters:**
        * `str` **name**: the name of the daedalus symbol.
        
        **Returns `dict`:**
        the daedalus symbol (empty if there's no symbol with given name)
        """
        return sqg2o.Daedalus.symbol(value)
    
    @staticmethod
    def instance(value : str) -> dict:
        """
        This method will get the all of the daedalus instance variables.
        **Parameters:**
        * `str` **instanceName**: the name of the daedalus instance.
        
        **Returns `dict`:**
        the object containing all of the daedalus instance variables.
        """
        return sqg2o.Daedalus.instance(value)