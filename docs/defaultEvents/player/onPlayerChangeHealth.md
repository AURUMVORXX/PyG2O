# `event` onPlayerChangeHealth
This event is triggered when player health changes.

Original: [onPlayerChangeHealth](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerChangeHealth/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player whose health points gets changed.
    * `int` **previous**: the previous health points of the player.
    * `int` **current**:  the new health points of the player.
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerChangeHealth')
async def onChangeHealth(playerid, previous, current):
    print(f'Player {playerid} changed health: {previous} -> {current}')
```