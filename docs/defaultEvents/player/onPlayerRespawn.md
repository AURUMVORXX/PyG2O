# `event` onPlayerRespawn
This event is triggered when a player respawns after death.

Original: [onPlayerRespawn](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerRespawn/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who respawned after death.
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerRespawn')
async def onRespawn(playerid):
    print(playerid, 'respawned.')
```