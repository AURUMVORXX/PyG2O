# `event` onNpcDestroyed

This event is triggered when remote NPC is created.

Original: [onNpcDestroyed](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/npc/onNpcDestroyed/)

## Parameters
* `dict` **kwargs**:
    * `int` **npc_id**: the id of the destroyed remote npc.

## Usage
```python
import g2o
        
@g2o.event('onNpcDestroyed')
def onNpcDestroy(**kwargs):
    print(f'NPC {kwargs['npc_id']} has been destroyed.')
```