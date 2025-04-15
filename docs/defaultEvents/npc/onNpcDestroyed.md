# `event` onNpcDestroyed

This event is triggered when remote NPC is created.

Original: [onNpcDestroyed](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/npc/onNpcDestroyed/)

## Parameters
* `dict` **kwargs**:
    * `int` **npc_id**: the id of the destroyed remote npc.

## Usage
```python
import pyg2o as g2o
        
@g2o.event('onNpcDestroyed')
async def onNpcDestroy(npc_id):
    print(f'NPC {npc_id} has been destroyed.')
```