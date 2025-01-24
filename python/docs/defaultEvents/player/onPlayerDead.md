# `event` onPlayerDead
This event is triggered when one player kills another player.

Original: [onPlayerDead](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerDead/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who died.
    * `int` **killerid**: the id of the player who killed other player. If killerid is set to `-1`, it means that there was no killer.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerDead')
def onDead(**kwargs):
    print(kwargs['playerid'], 'killed by', kwargs['killerid'])
```