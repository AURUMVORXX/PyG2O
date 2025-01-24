# `event` onPlayerChangeWeaponMode
This event is triggered when player changes the weapon mode.

Original: [onPlayerChangeWeaponMode](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/player/onPlayerChangeWeaponMode/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player which changes the weapon mode.
    * `int` **oldWeaponMode**: the old weapon mode which was used by the player. For more information see [Weapon mode](../../constants/weapon-mode.md).
    * `int` **newWeaponMode**:  the new weapon mode in which player is currently using. For more information see [Weapon mode](../../constants/weapon-mode.md).
    
## Usage
```python
import g2o
        
@g2o.event('onPlayerChangeWeaponMode')
def onChangeWM(**kwargs):
    print(f'Player {kwargs['playerid']} changed wm: {kwargs['oldWeaponMode']} -> {kwargs['newWeaponMode']}')
```