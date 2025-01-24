# `event` onPlayerMobInteract
This event is triggered when player interacts with any kind of mob object in the world. In Gothic, mobs are special vobs on the map, that hero can interact with. For example bed, door, chest etc.

Original: [onPlayerMobInteract](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerMobInteract/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: represents previous state of mob. If value is `1`, then mob was used, in any other case value is `0`.
    * `int` **from**: represents current state of mob. If value is `1`, then mob is used, in any other case value is `0`.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerMobInteract')
def onMobInteract(**kwargs):
    if kwargs['to'] == 1:
        print(kwargs['playerid'], 'started interaction with the MOB')
```