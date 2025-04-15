# `event` onPlayerCommand
This event is triggered when a player uses command on the chat.
Command always begins with forward slash `/`.

Original: [onPlayerCommand](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerCommand/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who typed the command.
    * `str` **command**: used command name on the chat.
    * `str` **params**:  command parameters divided by space.
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerCommand')
async def onCommand(playerid, command, params):
    # Spliting and formating params
    params = [eval(x) if not x.isalpha() else x for params.split()]
    
    if command == 'add' and len(params) == 2:
        print('Sum is: ', params[0] + params[1])            # /add 5 10 -> output: Sum is 15
```