# `event` onTick
This event is triggered in every server main loop iteration.

Original: [onExit](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/general/onTick/)

## Parameters
No parameters.

## Usage
```python
import g2o
        
@g2o.event('onTick')
def onTickEvt(**kwargs):
    print('Tock')
```