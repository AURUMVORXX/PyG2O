# `event` onPlayerEquipRing
This event is triggered when player equips or unequips ring. When item is unequiped, empty `str` is returned instead.

Original: [onPlayerEquipRing](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerEquipRing/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who equips a ring.
    * `int` **hand**: the hand id that the player is putting the ring on. For more information see [Hand](../../constants/hand.md).
    * `str` **instance**: the item instance from Daedalus scripts.
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerEquipRing')
async def onEquip(playerid, hand, instance):
    print(f'Player {playerid} equipped {instance}')
```