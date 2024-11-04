# `event` onInit
This event is triggered when server successfully starts up.

## Parameters
No parameters.

## Usage
```python
import g2o
        
@g2o.event('onInit')
def onInitEventHandler(**kwargs):
    print('Called onInit event')
```