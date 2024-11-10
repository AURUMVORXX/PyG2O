import sqg2o

def findNearbyPlayers(position : dict, radius : int, world : str, virtual_world : int = 0) -> list:
    """
    This function will search for nearest players, that matches given query arguments.
    Original: [findNearbyPlayers](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/streamer/findNearbyPlayers/)
    
    ## Declaration
    ```python
    def findNearbyPlayers(position : dict, radius : int, world : str, virtual_world : int = 0) -> list
    ```
    ## Parameters
    `dict {x, y, z}` **position**: the centroid position.
    `int` **radius**: the maximum radius to search from centroid.
    `str` **world**: the world used to find players.
    `int` **virtual_world**: the virtual world used to find players.
    ## Returns
    `list [int]`: ids of nearby players.
    """
    return sqg2o.findNearbyPlayers(position, radius, world, virtual_world)

def getSpawnedPlayersForPlayer(id : int) -> list:
    """
    This function is used to retrieve currently spawned players for given player.
    Original: [getSpawnedPlayersForPlayer](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/streamer/getSpawnedPlayersForPlayer/)
    
    ## Declaration
    ```python
    def getSpawnedPlayersForPlayer(id : int) -> list
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `list [int]`: ids of spawned players.
    """
    return sqg2o.getSpawnedPlayersForPlayer(id)

def getStreamedPlayersByPlayer(id : int) -> list:
    """
    This function is used to retrieve currently streamed players by given player. More details: Streamed players are basically clients, that has spawned given player in their game. Please notice, that player can be spawned only one way. Which means that there are situation were player 1 is spawned for player 2, but not the other way arount. Simple examples: - Invisible players cannot be seen, but they can see everyone nearby. - Flying around world using camera.
    Original: [getStreamedPlayersByPlayer](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/streamer/getStreamedPlayersByPlayer/)
    
    ## Declaration
    ```python
    def getStreamedPlayersByPlayer(id : int) -> list
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `list [int]`: ids of streamed players.
    """
    return sqg2o.getStreamedPlayersByPlayer(id)