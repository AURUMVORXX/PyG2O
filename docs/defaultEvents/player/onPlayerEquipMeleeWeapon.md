# `event` onPlayerEquipMeleeWeapon
This event is triggered when player equips or unequips melee weapon. When item is unequiped, empty `str` is returned instead.

Original: [onPlayerEquipMeleeWeapon](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerEquipMeleeWeapon/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who equips an melee weapon.
    * `str` **instance**: the item instance from Daedalus scripts.
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerEquipMeleeWeapon')
async def onEquip(playerid, instance):
    print(f'Player {playerid} equipped {instance}')
```