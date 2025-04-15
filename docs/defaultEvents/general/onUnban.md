# `event` onUnban
> [!TIP] This event can be cancelled
!!! note
    If serial/mac/ip/name indexes doesn't exist, then the parameters has not been specified when ban was added.
    If timestamp doesn't exist, then ban was permanent.

This event is triggered when ban with specified info is being removed.

Original: [onExit](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/general/onUnban/)

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
        
@g2o.event('onUnban')
async def onUnban(banInfo):
    print(f'Player {banInfo['name']} has been unbanned.')
```