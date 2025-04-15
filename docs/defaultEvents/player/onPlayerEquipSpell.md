# `event` onPlayerEquipSpell
This event is triggered when player equips or unequips scroll or rune. When item is unequiped, empty `str` is returned instead.

Original: [onPlayerEquipSpell](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerEquipSpell/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who equips a spell.
    * `int` **slotId**: the slot id that the player puts the spell on in range `<0, 6>`.
    * `str` **instance**: the item instance from Daedalus scripts.
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerSpell')
async def onEquip(playerid, slotId, instance):
    print(f'Player {playerid} equipped {instance}')
```