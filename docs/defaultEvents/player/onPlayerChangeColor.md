# `event` onPlayerChangeColor
This event is triggered when player nickname color was changed for all players.

Original: [onPlayerChangeColor](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerChangeColor/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player whose nickname color was changed.
    * `int` **r**: the amount of red in the nickname color `(0 - 255)`.
    * `int` **g**: the amount of green in the nickname color `(0 - 255)`.
    * `int` **b**: the amount of blue in the nickname color `(0 - 255)`.
    
## Usage
```python
import pyg2o as g2o
        
@g2o.event('onPlayerChangeColor')
async def onChangeColor(playerid, r, g, b):
    rgbColor = tuple(r, g, b)
    hexColor = '#%02x%02x%02x' % rgbColor
    print(f'Player {playerid} changed his color to {hexColor}')
```