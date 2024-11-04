# `event` onTime
This event is triggered each time when game time minute passes.

## Parameters
* `dict` **kwargs**:
    * `int` **day**: the current ingame day.
    * `int` **hour**: the current ingame hour.
    * `int` **min**: the current ingame minutes.

## Usage
```python
import g2o
        
@g2o.event('onTick')
def onTickEvt(**kwargs):
    day = kwargs['day']
    hour = kwargs['hour']
    mins = kwargs['min']
    print(f'Current time: Day {day}, Hour {hour}, Min {mins}')
```