# `event` onPlayerChangeMana
This event is triggered when player mana changes.

Original: [onPlayerChangeMana](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerChangeMana/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player mana points gets changed.
    * `int` **oldMP**: the previous mana points of the player.
    * `int` **newMP**:  the new mana points of the player.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerChangeMana')
def onChangeMana(**kwargs):
    print(f'Player {kwargs['playerid']} changed mana: {kwargs['oldMP']} -> {kwargs['newMP']}')
```