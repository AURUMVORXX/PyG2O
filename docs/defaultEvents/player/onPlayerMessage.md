# `event` onPlayerMessage
This event is triggered when a player types the message on the chat.

Original: [onPlayerMessage](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerMessage/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who typed the message.
    * `str` **message**: the message typed by the player.
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerMessage')
async def onMessage(playerid, message):
    print(pyg2o.getPlayerName(playerid), ' says ', message)
```