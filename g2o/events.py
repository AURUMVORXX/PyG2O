
eventList = {}

def callEvent(evtName : str, **kwargs : dict):
    """
    This function will notify (call) every handler bound to specified event.
    Original: [callEvent](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/event/callEvent/)
    
    ## Declaration
    ```python
    def callEvent(evtName : str, **kwargs : dict)
    ```
    
    ## Parameters
    * `str` **name**: the name of the event
    * `**dict` **kwargs**: the variable number of arguments.
    
    ## Usage
    ```python
    import g2o
    
    g2o.addEvent('testEvt')
    
    @g2o.event('testEvt')
    def onTestEvent(**kwargs):
        print(f'{kwargs['name']} called my beautiful test event')
        
    g2o.callEvent('testEvt', name = 'Diego')
    ```
    """
    if evtName in eventList:
        for event in eventList[evtName]:
            event['function'](**kwargs)
        
def addEvent(name):
    """
    This function will register a new event with specified name.
    Events can be used to notify function(s) when something will happen, like player joins the server, etc.
    Original: [addEvent](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/event/addEvent/)
    
    ## Declaration
    ```python
    def addEvent(name)
    ```
    
    ## Parameters
    * `str` **name**: the name of the event
    
    ## Usage
    ```python
    import g2o
    
    g2o.addEvent('testEvt')
    ```
    """
    if not name in eventList:
        eventList[name] = []
        
def event(name : str, priority : int = 9999):
    """
    This function will bind function to specified event.
    Original: [addEventHandler](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/event/addEventHandler/)
    
    ## Declaration
    ```python
    def event(name : str, priority : int = 9999)
    ```
    
    ## Parameters
    * `str` **name**: the name of the event
    * `int` **priority**: the function priority. The lower the value, the sooner the function/handler will be called.
    
    ## Usage
    ```python
    import g2o
    
    @g2o.event('onInit')
    def onInitEventHandler(**kwargs):
        print('Called onInit event')
    ```
    """
    def inlineEvt(func):
        if not name in eventList:
            pass
        
        eventList[name].append({'function': func, 'priority': priority})
        eventList[name].sort(key = lambda x: x['priority'])
        return func
    return inlineEvt
    
def removeEventHandler(name : str, func : function):
    """
    This function will unbind function from specified event.
    Original: [removeEventHandler](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/event/removeEventHandler/)
    
    ## Declaration
    ```python
    def removeEventHandler(name : str, func : function)
    ```
    
    ## Parameters
    * `str` **name**: the name of the event
    * `function` **func**: the reference to a function which is currently bound to specified event.
    
    ## Usage
    ```python
    import g2o
    
    @g2o.event('onTime')
    def onTimeEvt(**kwargs):
        print('Calling only once')
        g2o.removeEventHandler('onTime', onTimeEvt)
    ```
    """
    if not name in eventList:
        pass
    
    for index, item in enumerate(eventList[name]):
        if item['function'] == func:
            del eventList[name][index]

## registering default events

addEvent('onInit')
addEvent('onExit')
addEvent('onTick')
addEvent('onTime')
addEvent('onBan')
addEvent('onUnban')

addEvent('onPlayerChangeColor')
addEvent('onPlayerChangeFocus')
addEvent('onPlayerChangeHealth')
addEvent('onPlayerChangeMana')
addEvent('onPlayerChangeMaxHealth')
addEvent('onPlayerChangeMaxMana')
addEvent('onPlayerChangeWeaponMode')
addEvent('onPlayerChangeWorld')