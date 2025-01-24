# `event` onPlayerChangeHealth
This event is triggered when player health changes.

Original: [onPlayerChangeHealth](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerChangeHealth/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player whose health points gets changed.
    * `int` **oldHP**: the previous health points of the player.
    * `int` **newHP**:  the new health points of the player.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerChangeHealth')
def onChangeHealth(**kwargs):
    print(f'Player {kwargs['playerid']} changed health: {kwargs['oldHP']} -> {kwargs['newHP']}')
```