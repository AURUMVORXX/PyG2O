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
import g2o
        
@g2o.event('onPlayerChangeColor')
def onChangeColor(**kwargs):
    # Slicing out playerid and converting from {r: num, g: num, b: num} 
    # to (num, num, num)
    rgbColor = tuple(list(kwargs.values())[1:])
    # Formating rgb into hex color
    hexColor = '#%02x%02x%02x' % rgbColor
    print(f'Player {kwargs['playerid']} changed his color to {hexColor}')
```