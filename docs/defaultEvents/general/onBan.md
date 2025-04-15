# `event` onBan
> [!TIP] This event can be cancelled
!!! note
    If serial/mac/ip/name indexes doesn't exist, then the parameters has not been specified when ban was added.
    If timestamp doesn't exist, then ban was permanent.

This event is triggered when new ban is being added.

Original: [onBan](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/general/onBan/)

## Parameters
* `dict` **kwargs**:
    * `str` **mac**: MAC address of the banned player.
    * `str` **ip**: IP address of the banned player.
    * `str` **serial**: serial of the banned player.
    * `str` **name**: nickname of the banned player.
    * `int` **timestamp**: timestamp when the ban expires.

## Usage
```python
import pyg2o as g2o
from datetime import datetime
        
@g2o.event('onBan')
async def onBan(banInfo):
    print(f'Player {banInfo['name']} has been banned.')
    if ('timestamp' in banInfo):
        banExpires = datetime.fromtimestamp(banInfo['timestamp'])
        print(f'Ban expires at {banExpires}')
```