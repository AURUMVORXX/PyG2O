# `event` onPlayerTeleport
This event is triggered when player gets teleported by the game to the specified vob.

Original: [onPlayerTeleport](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerTeleport/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who gets teleported by the game.
    * `str` **vobName**: represents the name of the vob that player gets teleported to.
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerTeleport')
async def onTeleport(playerid, vobName):
    print(playerid, 'teleported to', vobName)
```