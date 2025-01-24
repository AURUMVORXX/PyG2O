# `event` onPlayerRespawn
This event is triggered when a player respawns after death.

Original: [onPlayerRespawn](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerRespawn/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who respawned after death.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerRespawn')
def onRespawn(**kwargs):
    print(kwargs['playerid'], 'respawned.')
```