# `event` onPlayerChangeWorld
> [!TIP] This event can be cancelled
This event is triggered when player tries to change his currently played world (ZEN).

Original: [onPlayerChangeWorld](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerChangeWorld/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who tries to change the played world.
    * `str` **world**: a filename name of the world.
    * `str` **waypoint**:  a name of the waypoint that the player will be teleported to.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerChangeWorld')
def onChangeWorld(**kwargs):
    print(f'Player {kwargs['playerid']} teleported to {kwargs['world']} at {kwargs['waypoint']}')
```