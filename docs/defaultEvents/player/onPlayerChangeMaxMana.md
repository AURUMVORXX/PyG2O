# `event` onPlayerChangeMaxMana
This event is triggered when player maximum mana changes.

Original: [onPlayerChangeMaxMana](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerChangeMaxMana/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player maximum mana points gets changed.
    * `int` **previous**: the previous maximum mana points of the player.
    * `int` **current**:  the new maximum mana points of the player.
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerChangeMaxMana')
async def onChangeMaxMana(playerid, previous, current):
    print(f'Player {playerid} changed maximum mana: {previous} -> {current}')
```