# `event` onInit
This event is triggered when server successfully starts up.

Original: [onExit](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/general/onInit/)

## Parameters
No parameters.

## Usage
```python
import pyg2o as g2o
        
@g2o.event('onInit')
async def onInitEventHandler():
    print('Called onInit event')
```