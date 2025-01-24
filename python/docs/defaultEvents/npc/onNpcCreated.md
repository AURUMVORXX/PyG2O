# `event` onNpcCreated

This event is triggered when remote NPC is created.

Original: [onNpcCreated](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/npc/onNpcCreated/)

## Parameters
* `dict` **kwargs**:
    * `int` **npc_id**: the id of the newly created remote npc.

## Usage
```python
import g2o
        
@g2o.event('onNpcCreated')
def onNpcCreate(**kwargs):
    print(f'NPC {kwargs['npc_id']} has been created.')
```