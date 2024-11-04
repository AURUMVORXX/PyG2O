# `event` onPlayerEquipRangedWeapon
This event is triggered when player equips or unequips ranged weapon. When item is unequiped, `null` is returned instead.

Original: [onPlayerEquipRangedWeapon](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerEquipRangedWeapon/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who equips an ranged weapon.
    * `str` **str | null**: instance: the item instance from Daedalus scripts.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerEquipRangedWeapon')
def onEquip(**kwargs):
    print(f'Player {kwargs['playerid']} equipped {kwargs['instance']}')
```