# `event` onPlayerEquipMeleeWeapon
This event is triggered when player equips or unequips melee weapon. When item is unequiped, `null` is returned instead.

Original: [onPlayerEquipMeleeWeapon](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerEquipMeleeWeapon/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who equips an melee weapon.
    * `str` **str | null**: instance: the item instance from Daedalus scripts.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerEquipMeleeWeapon')
def onEquip(**kwargs):
    print(f'Player {kwargs['playerid']} equipped {kwargs['instance']}')
```