# `event` onNpcActionFinished

This event is triggered when NPC action was finished.

Original: [onNpcActionFinished](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/npc/onNpcActionFinished/)

## Parameters
* `dict` **kwargs**:
    * `int` **npc_id**: the npc identifier.
    * `int` **action_type**: the action type.
    * `int` **action_id**: the unique action identifier.
    * `bool` **result**: the result of finished action.

## Usage
```python
import pyg2o as g2o
        
@g2o.event('onNpcActionFinished')
async def onActionFinished(npc_id, action_type, action_id, result):
    print(f'NPC {npc_id} finished action {action_type} with the result {result}.')
```