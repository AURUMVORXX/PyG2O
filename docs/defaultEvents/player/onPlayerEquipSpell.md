# `event` onPlayerEquipSpell
This event is triggered when player equips or unequips scroll or rune. When item is unequiped, `null` is returned instead.

Original: [onPlayerEquipSpell](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerEquipSpell/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who equips a spell.
    * `int` **slotId**: the slot id that the player puts the spell on in range `<0, 6>`.
    * `str` **str | null**: instance: the item instance from Daedalus scripts.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerSpell')
def onEquip(**kwargs):
    print(f'Player {kwargs['playerid']} equipped spell {kwargs['instance']} at slot {kwargs['slotId']}')
```