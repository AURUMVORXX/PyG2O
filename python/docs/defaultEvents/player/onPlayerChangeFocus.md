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
import g2o
        
@g2o.event('onPlayerChangeFocus')
def onChangeFocus(**kwargs):
    focusId = kwargs['newFocusId']
    if focusId != -1:
        print(f'Player {kwargs['playerid']} is looking at {focusId}')
    else
        print(f'Player {kwargs['playerid']} is looking at... who?')
```