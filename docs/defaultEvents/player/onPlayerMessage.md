# `event` onPlayerMessage
This event is triggered when a player types the message on the chat.

Original: [onPlayerMessage](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerMessage/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who typed the message.
    * `str` **message**: the message typed by the player.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerMessage')
def onMessage(**kwargs):
    print(kwargs['playerid'], 'says', kwargs['message'])
```