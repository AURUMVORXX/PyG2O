# `event` onPlayerShoot
This event is triggered when player shoot using ranged weapon.

Original: [onPlayerShoot](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerShoot/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who just shot.
    * `str | null` **munition**: the item instance from Daedalus scripts.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerShoot')
def onShoot(**kwargs):
    print(kwargs['playerid'], 'made a shot.')
```