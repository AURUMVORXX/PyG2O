# `event` onTick
This event is triggered in every server main loop iteration.

## Parameters
No parameters.

## Usage
```python
import g2o
        
@g2o.event('onTick')
def onTickEvt(**kwargs):
    print('Tock')
```