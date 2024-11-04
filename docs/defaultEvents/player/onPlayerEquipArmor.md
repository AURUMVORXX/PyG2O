# `event` onPlayerEquipAmulet
This event is triggered when player equips or unequips armor. When item is unequiped, `null` is returned instead.

Original: [onPlayerEquipArmor](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerEquipArmor/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who equips an armor.
    * `str` **str | null**: instance: the item instance from Daedalus scripts.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerEquipArmor')
def onEquip(**kwargs):
    print(f'Player {kwargs['playerid']} equipped {kwargs['instance']}')
```