
eventList = {}

def callEvent(name, **args):
    if name in eventList:
        for event in eventList[name]:
            event['function'](**args)
        
def addEvent(name):
    if not name in eventList:
        eventList[name] = []
        
def event(name, priority = 9999):
    def inlineEvt(func):
        if not name in eventList:
            pass
        
        eventList[name].append({'function': func, 'priority': priority})
        eventList[name].sort(key = lambda x: x['priority'])
        return func
    return inlineEvt
    
def removeEventHandler(name, func):
    if not name in eventList:
        pass
    
    for index, item in enumerate(eventList[name]):
        if item['function'] == func:
            del eventList[name][index]

## registering all the events

addEvent('onInit')
addEvent('onExit')
addEvent('onTick')
addEvent('onTime')