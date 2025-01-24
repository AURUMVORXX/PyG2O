import sqg2o

class SkyMeta(type):
    @property
    def weather(self):
        return sqg2o.Sky.weather
    
    @weather.setter
    def weather(self, value):
        sqg2o.Sky.weather
        
    @property
    def raining(self):
        return sqg2o.Sky.raining
    
    @raining.setter
    def raining(self, value):
        sqg2o.Sky.raining = value
    
    @property
    def renderLightning(self):
        return sqg2o.Sky.renderLightning
    
    @renderLightning.setter
    def renderLightning(self, value):
        sqg2o.Sky.renderLightning = value
        
    @property
    def windScale(self):
        return sqg2o.Sky.windScale
    
    @windScale.setter
    def windScale(self, value):
        sqg2o.Sky.windScale = value
        
    @property
    def dontRain(self):
        return sqg2o.Sky.dontRain
    
    @dontRain.setter
    def dontRain(self, value):
        sqg2o.Sky.dontRain = value

class Sky(metaclass=SkyMeta):
    """
    This class represents data packet that gets send over the network.
    Original: [Sky](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-classes/game/Sky/)
    
    ## `int` weather
    Represents the sky weather. For more information see [Weather Constants](../../constants/weather.md)

    ## `bool` raining
    Represents the raining/snowing state.
    
    ## `bool` renderLightning
    Represents the lightning feature during raining state.
    Lightning will only be rendered during raining and when weatherWeight is larger than 0.5
    
    ## `float` windScale
    Represents the sky wind scale used during raining/snowing.
    
    ## `bool` dontRain
    Represents the sky dontRain feature.
    When it's enabled, the rain/snow won't fall.
    """
    
    @staticmethod
    def setRainStartTime(hour : int, minute : int):
        """
        This method will set the sky weather time when it starts raining/snowing.
        **Parameters:**
        * `int` **hour**: the sky weather raining start hour.
        * `int` **minute**: the sky weather raining start min.
        """
        sqg2o.Sky.setRainStartTime(hour, minute)
        
    @staticmethod
    def setRainStopTime(hour : int, minute : int):
        """
        This method will set the sky weather time when it stops raining/snowing.
        **Parameters:**
        * `int` **hour**: the sky weather raining stop hour.
        * `int` **minute**: the sky weather raining stop min.
        """
        sqg2o.Sky.setRainStopTime(hour, minute)
        
    @staticmethod
    def getRainStartTime() -> dict:
        """
        This method will get the sky weather time when it starts raining/snowing.
        **Returns `dict`:**
        * `int` **hour**: the sky weather raining start hour.
        * `int` **minute**: the sky weather raining start min.
        """
        return sqg2o.Sky.getRainStartTime()
    
    @staticmethod
    def getRainStopTime() -> dict:
        """
        This method will get the sky weather time when it stops raining/snowing.
        **Returns `dict`:**
        * `int` **hour**: the sky weather raining stop hour.
        * `int` **minute**: the sky weather raining stop min.
        """
        return sqg2o.Sky.getRainStopTime()
    