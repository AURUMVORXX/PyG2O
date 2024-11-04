# `event` onPlayerEquipShield
This event is triggered when player equips or unequips shield. When item is unequiped, `null` is returned instead.

Original: [onPlayerEquipShield](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerEquipShield/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who equips a shield.
    * `str` **str | null**: instance: the item instance from Daedalus scripts.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerEquipShield')
def onEquip(**kwargs):
    print(f'Player {kwargs['playerid']} equipped {kwargs['instance']}')
```