# `event` onPlayerEquipHelmet
This event is triggered when player equips or unequips helmet. When item is unequiped, empty `str` is returned instead.

Original: [onPlayerEquipHelmet](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerEquipHelmet/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who equips a helmet.
    * `str` **instance**: the item instance from Daedalus scripts.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerEquipHelmet')
def onEquip(**kwargs):
    print(f'Player {kwargs['playerid']} equipped {kwargs['instance']}')
```