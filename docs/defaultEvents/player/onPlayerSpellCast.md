# `event` onPlayerSpellCast
> [!TIP] This event can be cancelled
!!! note
    Right now transformation and summon spells are not supported, despite this event will be triggered for them. Cancelling this event willl prevent this action to be synced to other players.
    
This event is triggered when player is casting some spell.

Original: [onPlayerSpellCast](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerSpellCast/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who casts the spell.
    * `str | null` **instance**: the item instance from Daedalus scripts.
    * `int` **spellLevel**: the level of charged spell.
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerSpellCast')
async def onSpellCast(playerid, instance, spellLevel):
    print(playerid, 'casted a spell', instance)
```