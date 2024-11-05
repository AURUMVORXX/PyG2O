# `event` onPlayerEquipHandItem
This event is triggered when game adds item to player hand, e.g: when player opens or consumes any item. When item is removed from hand, `null` is returned instead.

Original: [onPlayerEquipHandItem](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerEquipHandItem/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who gets an item to his hand.
    * `int` **hand**: the id of the hand in which player holds item. For more information see [Hand](../../constants/hand.md).
    * `str` **str | null**: instance: the item instance from Daedalus scripts.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerEquipHandItem')
def onEquip(**kwargs):
    print(f'Player {kwargs['playerid']} has {kwargs['instance']}, used hand with id {kwargs['hand']}')
```