## Events

* `addEventHandler` replaced with decorator [event](events/event.md)
```python
@g2o.event('onInit')
def evtInitFirst(**kwargs):
    print('Hello')
    
@g2o.event('onInit', 100)       # '100' is priority
def evtInitSecond(**kwargs):
    print('World')
```
---
* Positional arguments replaced with keyword arguments (see names of all keywords on the each event page)
```python
@g2o.event('onPlayerChangeColor')
def evtColor(**kwargs):
    playerid = kwargs['playerid']
    r = kwargs['r']
    b = kwargs['b']
```
---
* `callEvent` now also requires to pass keyword arguments instead of positional arguments
```python
@g2o.event('MyTestEvent')
def testEvt(**kwargs):
    print(kwargs)
    
g2o.callEvent('MyTestEvent', name = 'aurumvorax', id = 15)
# OR
g2o.callEvent('MyTestEvent', {'name': 'aurumvorax', 'id': 15})
# OR
args = {'name': 'aurumvorax', 'id': 15}
g2o.callEvent('MyTestEvent', args)
```
---
* `cancelEvent` replaced with returning `False` inside the handler
<sup>*(you don't need to explicitly return `True` if you don't want to cancel the event)*</sup>
```python
@g2o.event('onPlayerTakeItem')
def evtTake(**kwargs):
    return False
```
---
* `isEventCancelled` replaced with built-in function property `cancelled`, alongside with the `eventName` (if you need it for some reason)
```python
@g2o.event('onPlayerDropItem')
def evtDrop(**kwargs):
    print(evtDrop.cancelled)
    print(evtDrop.eventName)
```