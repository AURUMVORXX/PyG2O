# `event` onNpcChangeHostPlayer

This event is triggered when server sends NPC action to streamed players.

Original: [onNpcChangeHostPlayer](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/npc/onNpcChangeHostPlayer/)

## Parameters
* `dict` **kwargs**:
    * `int` **npc_id**: the id of the remote npc.
    * `int` **current_id**: the id of the current host, can be -1 if there is no current host.
    * `int` **previous_id**: the id of the previous host, can be -1 if there was no previous host.

## Usage
```python
import pyg2o as g2o
        
@g2o.event('onNpcChangeHostPlayer')
async def onChangeHostPlayer(npc_id, previous_id, current_id):
    print(f'NPC {npc_id} changed host to {current_id}')
```