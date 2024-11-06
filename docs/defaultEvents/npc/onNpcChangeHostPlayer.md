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
import g2o
        
@g2o.event('onNpcChangeHostPlayer')
def onChangeHostPlayer(**kwargs):
    print(f'NPC {kwargs['npc_id']} sent {kwargs['action_type']} to all players.')
```