# `event` onPlayerUseCheat
!!! note
    Detecting some type of forbidden tools may take, even a few minutes. Server need time to analyze player data.

This event is triggered when player uses some of forbidden cheat tools.

Original: [onPlayerUseCheat](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/anticheat/onPlayerUseCheat/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who used some type of trainer/cheat.
    * `int` **type**: the type of used trainer/cheat. For more information see [AntiCheat constants](../../constants/anticheat.md)

## Usage
```python
import pyg2o
        
@pyg2o.event('onPlayerUseCheat')
async def onCheat(playerid, type):
    print(f'Player {playerid} used forbidden cheat tool type {type}.')
```