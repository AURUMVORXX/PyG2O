# `event` onPlayerDropItem
This event is triggered when player drops an item from his inventory to the ground.

Original: [onPlayerDropItem](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerDropItem/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who tries to drop the item on the ground.
    * `ItemGround` **itemGround**: the ground item object which represents the dropped item by the player.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerDropItem')
def onDropItem(**kwargs):
    item = itemm['itemGround']
    print(f'Player {kwargs['playerid']} dropped {item.instance} x{item.amount}')
```