# `event` onPlayerTakeItem
> [!TIP] This event can be cancelled
!!! note
    Even if this event is triggered it doesn't mean, that player will get item to his inventory. It only means, that the player tried to get the item from the ground. Server is the last decide if the item can be taken from the ground. Canceling this event will prevent the item to be taken from the ground.

This event is triggered when player takes an item from the ground.

Original: [onPlayerTakeItem](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerTakeItem/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who tries to take the ground item.
    * `ItemGround` **itemGround**: the ground item object which player tried to to take.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerTakeItem')
def onTakeItem(**kwargs):
    item = itemm['itemGround']
    print(f'Player {kwargs['playerid']} took {item.instance} x{item.amount}')
```