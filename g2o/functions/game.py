import sqg2o

def getHostname() -> str:
    """
    This function will get the hostname of the server.
    Original: [getHostname](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/game/getHostname/)
    
    ## Declaration
    ```python
    def getHostname() -> str
    ```
    ## Returns
    `str`: Server hostname.
    
    ## Usage
    ```python
    import g2o
    
    @g2o.event('onInit')
    def evtInit(**kwargs):
        print('Server hostname:', g2o.getHostname())
    ```
    """
    return sqg2o.getHostname()

def getMaxSlots() -> int:
    """
    This function will get the max number of slots available on the server.
    Original: [getMaxSlots](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/game/getMaxSlots/)
    
    ## Declaration
    ```python
    def getMaxSlots() -> int
    ```
    ## Returns
    `int`: Max slots number on the server.
    
    ## Usage
    ```python
    import g2o
    
    @g2o.event('onInit')
    def evtInit(**kwargs):
        print('Server max slots:', g2o.getMaxSlots())
    ```
    """
    return sqg2o.getMaxSlots()

def getPlayersCount() -> int:
    """
    This function will get the max number of slots available on the server.
    Original: [getPlayersCount](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/game/getPlayersCount/)
    
    ## Declaration
    ```python
    def getPlayersCount() -> int
    ```
    ## Returns
    `int`: Number of players on the server.
    
    ## Usage
    ```python
    import g2o
    
    @g2o.event('onInit')
    def evtInit(**kwargs):
        print('Players online:', g2o.getPlayersCount())
    ```
    """
    return sqg2o.getPlayersCount()

def exit(exitCode : int = 0):
    """
    This function will close the server with specified exit code.
    Original: [exit](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/exit/)
    
    ## Declaration
    ```python
    def exit(exitCode : int = 0)
    ```
    ## Parameters
    * `int` **exitCode**: exit status for g2o server.
    """
    return sqg2o.exit(exitCode)

def getDayLength() -> float:
    """
    The function is used to get the day length in miliseconds.
    Original: [getDayLength](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/getDayLength/)
    
    ## Declaration
    ```python
    def getDayLength() -> float
    ```
    ## Returns
    `float`: the current day length in miliseconds.
    """
    return sqg2o.getDayLength()

def getServerDescription() -> str:
    """
    This function will get the description of the server.
    Original: [getServerDescription](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/getServerDescription/)
    
    ## Declaration
    ```python
    def getServerDescription() -> str
    ```
    ## Returns
    `str`: Server description.
    """
    return sqg2o.getServerDescription()

def getServerWorld() -> str:
    """
    The function is used to get the path of the default world on the server.
    Original: [getServerWorld](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/getServerWorld/)
    
    ## Declaration
    ```python
    def getServerWorld() -> str
    ```
    ## Returns
    `str`: The world path name.
    """
    return sqg2o.getServerWorld()

def getTime() -> dict:
    """
    The function is used to get the path of the default world on the server.
    Original: [getTime](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/getTime/)
    
    ## Declaration
    ```python
    def getTime() -> dict
    ```
    ## Returns
    `dict {day, hour, min}`: The current time in the game.
    """
    return sqg2o.getTime()

def serverLog(text : str):
    """
    This function will log the text into server.log file.
    Original: [serverLog](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/serverLog/)
    
    ## Declaration
    ```python
    def serverLog(text : str)
    ```
    ## Parameters
    `str` **text**: the text message that you want to append to server.log file.
    """
    return sqg2o.serverLog(text)

def setDayLength(miliseconds : float):
    """
    !!! note
        Day length can't be smaller than 10 000 miliseconds.
        
    This function will set the day length in miliseconds.
    Original: [setDayLength](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/setDayLength/)
    
    ## Declaration
    ```python
    def setDayLength(miliseconds : float)
    ```
    ## Parameters
    `float` **miliseconds**: day length in miliseconds.
    """
    return sqg2o.setDayLength(miliseconds)

def setServerDescription(description : str):
    """
    This function will set the description of the server.
    Original: [setServerDescription](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/setServerDescription/)
    
    ## Declaration
    ```python
    def setServerDescription(description : str)
    ```
    ## Parameters
    `str` **description**: the server description.
    ## Returns
    `bool`: `true` if server description was set successfully, otherwise `false`.
    """
    return sqg2o.setServerDescription(description)

def setServerWorld(world : str):
    """
    !!! note
        The server world limit is set to 32 characters.
    
    !!! note
        If the target world path is written with backslashes instead of normal slashes, you need to escape it with another backslashes e.g. "NEWWORLD\\NEWWORLD.ZEN".
        
    This function will change the default world to which players will enter after joining.
    Original: [setServerWorld](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/setServerWorld/)
    
    ## Declaration
    ```python
    def setServerWorld(world : str)
    ```
    ## Parameters
    `str` **world**: the path to the target world.
    """
    return sqg2o.setServerWorld(world)

def setTime(hour : int, min : int, day : int = 0):
    """
    This function will set the current time in the game to the given time, for all the players.
    Original: [setTime](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/game/setTime/)
    
    ## Declaration
    ```python
    def setTime(hour : int, min : int, day : int = 0)
    ```
    ## Parameters
    `int` **hour**: the hour of new time (in the range between 0-23).
    `int` **min**: the minute of new time (in the range between 0-59).
    `int` **day**: the day of new time.
    """
    return sqg2o.setTime(hour, min, day)