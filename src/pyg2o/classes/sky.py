from ..server import PythonWebsocketServer

class Sky:
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
    async def get_weather():
        data = 'return Sky.weather'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    @staticmethod
    async def set_weather(value):
        data = 'return Sky.weather = value'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    @staticmethod
    async def get_raining():
        data = 'return Sky.raining'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    @staticmethod
    async def set_raining(value):
        data = 'return Sky.raining = value'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    @staticmethod
    async def get_renderLightning():
        data = 'return Sky.renderLightning'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    @staticmethod
    async def set_renderLightning(value):
        data = 'return Sky.renderLightning = value'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    @staticmethod
    async def get_windScale():
        data = 'return Sky.windScale'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    @staticmethod
    async def set_windScale(value):
        data = 'return Sky.windScale = value'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
        
    @staticmethod
    async def get_dontRain():
        data = 'return Sky.dontRain'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    @staticmethod
    async def set_dontRain(value):
        data = 'return Sky.dontRain = value'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    @staticmethod
    async def setRainStartTime(hour : int, minute : int):
        """
        This method will set the sky weather time when it starts raining/snowing.
        **Parameters:**
        * `int` **hour**: the sky weather raining start hour.
        * `int` **minute**: the sky weather raining start min.
        """
        data = f'return Sky.setRainStartTime({hour}, {minute})'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
        
    @staticmethod
    async def setRainStopTime(hour : int, minute : int):
        """
        This method will set the sky weather time when it stops raining/snowing.
        **Parameters:**
        * `int` **hour**: the sky weather raining stop hour.
        * `int` **minute**: the sky weather raining stop min.
        """
        data = f'return Sky.setRainStopTime({hour}, {minute})'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
        
    @staticmethod
    async def getRainStartTime() -> dict:
        """
        This method will get the sky weather time when it starts raining/snowing.
        **Returns `dict`:**
        * `int` **hour**: the sky weather raining start hour.
        * `int` **minute**: the sky weather raining start min.
        """
        data = 'return Sky.getRainStartTime()'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    
    @staticmethod
    async def getRainStopTime() -> dict:
        """
        This method will get the sky weather time when it stops raining/snowing.
        **Returns `dict`:**
        * `int` **hour**: the sky weather raining stop hour.
        * `int` **minute**: the sky weather raining stop min.
        """
        data = 'return Sky.getRainStopTime()'
        
        server = await PythonWebsocketServer.get_server()
        result = await server.make_request(data)
        return result
    