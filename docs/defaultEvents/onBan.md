# `event` onBan
!!! note
    If serial/mac/ip/name indexes doesn't exist, then the parameters has not been specified when ban was added.
    If timestamp doesn't exist, then ban was permanent.

This event is triggered when new ban is being added.

## Parameters
* `dict` **kwargs**:
    * `str` **mac**: MAC address of the banned player.
    * `str` **ip**: IP address of the banned player.
    * `str` **serial**: serial of the banned player.
    * `str` **name**: nickname of the banned player.
    * `int` **timestamp**: timestamp when the ban expires.

## Usage
```python
import g2o
from datetime import datetime
        
@g2o.event('onBan')
def onBan(**kwargs):
    print(f'Player {kwargs['name']} has been banned.')
    if ('timestamp' in kwargs):
        banExpires = datetime.fromtimestamp(kwargs['timestamp'])
        print(f'Ban expires at {banExpires}')
```