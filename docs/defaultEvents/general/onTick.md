# `event` onTick
This event is triggered in every server main loop iteration.

Original: [onExit](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/general/onTick/)

## Parameters
No parameters.

## Usage
```python
import pyg2o as g2o
        
@g2o.event('onTick')
async def onTickEvt():
    print('Tock')
```