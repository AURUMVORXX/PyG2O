# `event` onPlayerChangeMaxHealth
This event is triggered when player maximum health changes.

Original: [onPlayerChangeMaxHealth](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerChangeMaxHealth/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player whose maxium health points gets changed.
    * `int` **oldMaxHP**: the previous maximum health points of the player.
    * `int` **newMaxHP**:  the new maximum health points of the player.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerChangeMaxHealth')
def onChangeMaxHealth(**kwargs):
    print(f'Player {kwargs['playerid']} changed maximum health: {kwargs['oldMaxHP']} -> {kwargs['newMaxHP']}')
```