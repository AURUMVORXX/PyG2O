# `event` onPlayerJoin
This event is triggered when a player successfully joined the server.

Original: [onPlayerJoin](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerJoin/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who joined the server.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerJoin')
def onJoin(**kwargs):
    print(kwargs['playerid'], 'joined to the server.')
```