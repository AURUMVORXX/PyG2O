# `event` onPlayerTeleport
This event is triggered when player face animation is toggled (played or stopped), due to eating or other activities.

Original: [onPlayerToggleFaceAni](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerToggleFaceAni/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who gets teleported by the game.
    * `str` **aniName**: the face animation name.
    * `bool` **toggle**: `true` when player is started playing face animation, otherwise `false`.
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerToggleFaceAni')
async def onToggleFA(playerid, aniName, toggle):
    if toggle:
        print(playerid, 'started face ani', aniName)
```