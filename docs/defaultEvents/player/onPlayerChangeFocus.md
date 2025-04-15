# `event` onPlayerChangeFocus
This event is triggered when player targets another player.

Original: [onPlayerChangeFocus](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerChangeFocus/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player which changes the focus.
    * `int` **oldFocusId**: the old playerid targeted by the player. Can be `-1` if player wasn't targeting other player.
    * `int` **newFocusId**:  the new playerid targeted by the player. Can be `-1` if player doesn't target anyone.
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerChangeFocus')
async def onChangeFocus(playerid, oldFocusId, newFocusId):
    if newFocusId != -1:
        print(f'Player {playerid} is looking at {newFocusId}')
    else
        print(f'Player {playerid} is looking at... who?')
```