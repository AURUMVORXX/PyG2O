# `event` onPlayerChangeMana
This event is triggered when player mana changes.

Original: [onPlayerChangeMana](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerChangeMana/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player mana points gets changed.
    * `int` **previous**: the previous mana points of the player.
    * `int` **current**:  the new mana points of the player.
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerChangeMana')
async def onChangeMana(playerid, previous, current):
    print(f'Player {playerid} changed mana: {previous} -> {current}')
```