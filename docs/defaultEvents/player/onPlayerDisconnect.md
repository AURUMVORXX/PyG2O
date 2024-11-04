# `event` onPlayerDisconnect
This event is triggered when a player gets disconnected with the server.

Original: [onPlayerDisconnect](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerDisconnect/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: he id of the player who disconnected from the server.
    * `int` **reason**: the reason why player got disconnected. For more information see **TBD**.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerDisconnect')
def onChangeDC(**kwargs):
    print(f'Player {kwargs['playerid']} has left from the server')
```