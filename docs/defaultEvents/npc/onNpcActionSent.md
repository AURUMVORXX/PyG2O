# `event` onNpcActionSent

This event is triggered when NPC host is changed. Every remote NPC is hosted by one of spawned players in order to get valid position of NPC.

Original: [onNpcActionSent](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/npc/onNpcActionSent/)

## Parameters
* `dict` **kwargs**:
    * `int` **npc_id**: the npc identifier.
    * `int` **current_id**: the action type.
    * `int` **previous_id**: the unique action identifier.

## Usage
```python
import pyg2o as g2o
        
@g2o.event('onNpcActionSent')
async def onActionSent(npc_id, action_type, action_id):
    print(f'NPC {npc_id} sent action {action_id}.')
```