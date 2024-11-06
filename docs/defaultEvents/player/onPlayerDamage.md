# `event` onPlayerDamage
> [!TIP] This event can be cancelled
This event is triggered when player receives damage.

Original: [onPlayerDamage](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerDamage/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who died.
    * `int` **killerid**: the id of the killer. If killerid is set to `-1`, it means that there was no killer. In this particular case damage source can be fall from a tall object or scripts.
    * `DamageDescription` **description**: a structure containing damage information. For more information see [DamageDescription](../../classes/game/DamageDescription.md)
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerDamage')
def onDamage(**kwargs):
    desc = kwargs['description']
    print(f'Ouch! Player {kwargs['playerid']} just received {desc.damage} damage.')
```