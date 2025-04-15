# `event` onNpcCreated

This event is triggered when remote NPC is created.

Original: [onNpcCreated](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/npc/onNpcCreated/)

## Parameters
* `dict` **kwargs**:
    * `int` **npc_id**: the id of the newly created remote npc.

## Usage
```python
import pyg2o as g2o
        
@g2o.event('onNpcCreated')
async def onNpcCreate(npc_id):
    print(f'NPC {npc_id} has been created.')
```