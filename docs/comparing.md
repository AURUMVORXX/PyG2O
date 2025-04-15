
* `addEventHandler` replaced with decorator [event](functions/event/event.md)
```python
@pyg2o.event('onInit')
async def evtInitFirst():
    print('Hello')
    
@pyg2o.event('onInit', 100)       # '100' is priority
async def evtInitSecond():
    print('World')
```
---
* Positional arguments inside event handles replaced with keyword arguments (see names of all keywords on the each event page)
```python
@pyg2o.event('onPlayerChangeColor')
async def evtColor(playerid, r, g, b):
    pass
```
---
* `callEvent` now also requires to pass keyword arguments instead of positional arguments
```python
@pyg2o.event('MyTestEvent')
async def testEvt(name, id):
    print(name, id)
    
g2o.callEvent('MyTestEvent', name = 'aurumvorax', id = 15)
# OR
g2o.callEvent('MyTestEvent', {'name': 'aurumvorax', 'id': 15})
# OR
args = {'name': 'aurumvorax', 'id': 15}
asyncio.create_task(pyg2o.callEvent('MyTestEvent', args))
```
---
* `cancelEvent` temporarily disabled
---
* `isEventCancelled` replaced with built-in function property `cancelled`, alongside with the `eventName`
```python
@pyg2o.event('onPlayerDropItem')
async def evtDrop(**kwargs):
    print(evtDrop.cancelled)
    print(evtDrop.eventName)
```
---
Now all constants should be called via **Constant** class
```pyton
import pyg2o

@pyg2o.event('onInit')
async def evt_init():
    print(pyg2o.Constant.SERVER_SIDE)
```
* Following functions and classes have been removed <sub><sup>RIP :(</sub></sup>

    * `md5`
    * `sha1`
    * `sha256`
    * `sha384`
    * `sha512`
    * `setReloadCallback`
    * `setUnloadCallback`
    * `getTimerExecuteTimes`
    * `getTimerInterval`
    * `killTimer`
    * `setTimer`
    * `setTimerExecuteTimes`
    * `setTimerInterval`
    * `sscanf`
    * `hexToRgb`
    * `rgbToHex`
    * `getTickCount`
    * `eventValue`
    * `getPlayerMagicLevel`
    * `setPlayerMagicLevel`
    * `Packet`
    * `Way`
    * `NpcAction`
    
* Following constants has been removed:

    * `UNRELIABLE`
    * `UNRELIABLE_SEQUENCED`
    * `RELIABLE`
    * `RELIABLE_SEQUENCED`
    * `RELIABLE_ORDERED`
--- 
* All functions and events that returned/passed a `null` in the Squirrel, now passes an empty string. Most notable in this list are all equipment related functions and events
    * `onPlayerEquipAmulet`
    * `onPlayerEquipArmor`
    * `onPlayerEquipBelt`
    * `onPlayerEquipHandItem`
    * `onPlayerEquipHelmet`
    * `onPlayerEquipMeleeWeapon`
    * `onPlayerEquipRangedWeapon`
    * `onPlayerEquipRing`
    * `onPlayerEquipShield`
    * `onPlayerEquipSpell`
    * `getPlayerAmulet`
    * `getPlayerArmor`
    * `getPlayerBelt`
    * `getPlayerHelmet`
    * `getPlayerMeleeWeapon`
    * `getPlayerRangedWeapon`
    * `getPlayerRing`
    * `getPlayerShield`
    * `getPlayerSpell`