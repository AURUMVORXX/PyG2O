# `event` onTime
This event is triggered each time when game time minute passes.

Original: [onExit](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/general/onTime/)

## Parameters
* `dict` **kwargs**:
    * `int` **day**: the current ingame day.
    * `int` **hour**: the current ingame hour.
    * `int` **min**: the current ingame minutes.

## Usage
```python
import pyg2o as g2o
        
@g2o.event('onTime')
async def onTickEvt(day, hour, min):
    print(f'Current time: Day {day}, Hour {hour}, Min {mins}')
```