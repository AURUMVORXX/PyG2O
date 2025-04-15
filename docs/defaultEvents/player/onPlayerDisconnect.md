# `event` onPlayerDisconnect
This event is triggered when a player gets disconnected with the server.

Original: [onPlayerDisconnect](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerDisconnect/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: he id of the player who disconnected from the server.
    * `int` **reason**: the reason why player got disconnected. For more information see [Network](../../constants/network.md).
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerDisconnect')
async def onDC(playerid, reason):
    print(f'Player {playerid} has left from the server')
```