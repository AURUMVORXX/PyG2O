# `event` onPlayerEnterWorld
This event is triggered when player entered the world (**ZEN**) and was successfully spawned in it.

Original: [onPlayerEnterWorld](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerEnterWorld/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who entered the world.
    * `str` **world**: an filename name of the world.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerEnterWorld')
def onEnterWorld(**kwargs):
    print(f'Player {kwargs['playerid']} entered world {kwargs['world']}')
```