# `event` onPlayerChangeMaxHealth
This event is triggered when player maximum health changes.

Original: [onPlayerChangeMaxHealth](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerChangeMaxHealth/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player whose maxium health points gets changed.
    * `int` **previous**: the previous maximum health points of the player.
    * `int` **current**:  the new maximum health points of the player.
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerChangeMaxHealth')
async def onChangeMaxHealth(playerid, previous, current):
    print(f'Player {playerid} changed maximum health: {previous} -> {current}')
```