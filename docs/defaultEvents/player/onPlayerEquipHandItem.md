# `event` onPlayerEquipHandItem
This event is triggered when game adds item to player hand, e.g: when player opens or consumes any item. When item is removed from hand, empty `str` is returned instead.

Original: [onPlayerEquipHandItem](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerEquipHandItem/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who gets an item to his hand.
    * `int` **hand**: the id of the hand in which player holds item. For more information see [Hand](../../constants/hand.md).
    * `str` **instance**: the item instance from Daedalus scripts.
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerEquipHandItem')
async def onEquip(playerid, hand, instance):
    print(f'Player {playerid} equipped {instance}')
```