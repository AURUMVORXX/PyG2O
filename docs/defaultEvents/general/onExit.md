# `event` onExit
This event is triggered when server is going to shut down.
You can use it, to save some data before closing up, or do something else.

Original: [onExit](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/general/onExit/)

## Parameters
No parameters.

## Usage
```python
import pyg2o as g2o
        
@g2o.event('onExit')
async def onExitEvt():
    print('Bye')
```