# `event` onExit
This event is triggered when server is going to shut down.
You can use it, to save some data before closing up, or do something else.

## Parameters
No parameters.

## Usage
```python
import g2o
        
@g2o.event('onExit')
def onExitEvt(**kwargs):
    print('Bye')
```