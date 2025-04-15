# `event` onPlayerSpellSetup
This event is triggered when player prepares the spell.

Original: [onPlayerSpellSetup](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerSpellSetup/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who prepares the spell.
    * `str | null` **instance**: the item instance from Daedalus scripts.
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerSpellSetup')
async def onSpellSetup(playerid, instance):
    print(playerid, 'setuped a spell', instance)
```