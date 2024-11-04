# `event` onPlayerEquipBelt
This event is triggered when player equips or unequips belt. When item is unequiped, `null` is returned instead.

Original: [onPlayerEquipBelt](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerEquipBelt/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who equips a belt.
    * `str` **str | null**: instance: the item instance from Daedalus scripts.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerEquipBelt')
def onEquip(**kwargs):
    print(f'Player {kwargs['playerid']} equipped {kwargs['instance']}')
```