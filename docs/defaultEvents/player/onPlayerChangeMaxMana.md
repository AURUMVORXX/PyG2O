# `event` onPlayerChangeMaxMana
This event is triggered when player maximum mana changes.

Original: [onPlayerChangeMaxMana](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerChangeMaxMana/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player maximum mana points gets changed.
    * `int` **oldMaxMP**: the previous maximum mana points of the player.
    * `int` **newMaxMP**:  the new maximum mana points of the player.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerChangeMaxMana')
def onChangeMaxMana(**kwargs):
    print(f'Player {kwargs['playerid']} changed maximum mana: {kwargs['oldMaxMP']} -> {kwargs['newMaxMP']}')
```