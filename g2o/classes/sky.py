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
            
    @staticmethod
    def setRainStartTime(hour : int, minute : int):
        sqg2o.Sky.setRainStartTime(hour, minute)
        
    @staticmethod
    def setRainStopTime(hour : int, minute : int):
        sqg2o.Sky.setRainStopTime(hour, minute)
        
    @staticmethod
    def getRainStartTime() -> dict:
        return sqg2o.Sky.getRainStartTime()
    
    @staticmethod
    def getRainStopTime() -> dict:
        return sqg2o.Sky.getRainStopTime()
    