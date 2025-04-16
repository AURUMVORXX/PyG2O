
from typing import Literal, overload
from functools import wraps
from ..serialize import _deserialize

eventList           = {}
disabledEventList   = []

async def callEvent(evtName : str, **kwargs : list):
    """
    This function will notify (call) every handler bound to specified event.
    Original: [callEvent](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/event/callEvent/)
    
    ## Declaration
    ```python
    def callEvent(evtName : str, **kwargs : list)
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
    isEventCancelled = False
    
    if evtName in eventList and evtName not in disabledEventList:
        for event in eventList[evtName]:
            
            event['function'].eventName = evtName
            event['function'].cancelled = isEventCancelled
            result = await event['function'](**kwargs)
            
            if result != None:
                isEventCancelled = not result
                
    return isEventCancelled
        
def addEvent(name : str):
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


@overload
def event(event_name: Literal['onPlayerUseCheat'], priority: int = 9999) -> None:
    '''
    !!! note
        Detecting some type of forbidden tools may take, even a few minutes. Server need time to analyze player data.
        
    ## Parameters:
    * **playerid**: str - the id of the player who used some type of trainer/cheat.
    * **type**: int - the type of used trainer/cheat. For more information see AntiCheat constants.
    '''
    ...
    
@overload
def event(event_name: Literal['onBan'], priority: int = 9999) -> None:
    '''
    !!! note
        If serial/mac/ip/name indexes doesn't exist, then the parameters has not been specified when ban was added.
    
    This event is triggered when new ban is being added. 
    ## Parameters:
    * **banInfo**: dict
        * **mac**: str - MAC address of the banned player.
        * **ip**: str - IP address of the banned player.
        * **serial**: str - serial of the banned player.
        * **name**: str - nickname of the banned player.
        * **timestamp**: int - timestamp when the ban expires.
    '''
    ...
    
@overload
def event(event_name: Literal['onExit'], priority: int = 9999) -> None:
    '''
    This event is triggered when server is going to shut down.
    You can use it, to save some data before closing up, or do something else.
    ## Parameters:
    No parameters.
    '''
    ...
    
@overload
def event(event_name: Literal['onInit'], priority: int = 9999) -> None:
    '''
    This event is triggered when server successfully starts up.
    ## Parameters:
    No parameters.
    '''
    ...
    
@overload
def event(event_name: Literal['onTick'], priority: int = 9999) -> None:
    '''
    This event is triggered in every server main loop iteration.
    ## Parameters:
    No parameters.
    '''
    ...
    
@overload
def event(event_name: Literal['onTime'], priority: int = 9999) -> None:
    '''
    This event is triggered each time when game time minute passes.
    ## Parameters:
    * **day**: int - the current ingame day.
    * **hour**: int - the current ingame hour.
    * **min**: int - the current ingame minutes.
    '''
    ...
    
@overload
def event(event_name: Literal['onUnban'], priority: int = 9999) -> None:
    '''
    !!! note
        If serial/mac/ip/name indexes doesn't exist, then the parameters has not been specified when ban was added.
    
    This event is triggered when ban with specified info is being removed.
    ## Parameters:
    * **banInfo**: dict
        * **mac**: str - MAC address of the banned player.
        * **ip**: str - IP address of the banned player.
        * **serial**: str - serial of the banned player.
        * **name**: str - nickname of the banned player.
        * **timestamp**: int - timestamp when the ban expires.
    '''
    ...
    
@overload
def event(event_name: Literal['onNpcActionFinished'], priority: int = 9999) -> None:
    '''
    This event is triggered when NPC action was finished.
    ## Parameters:
    * **npc_id**: int - the npc identifier.
    * **action_type**: int - the action type.
    * **action_id**: int - the unique action identifier.
    * **result**: bool - the result of finished action.
    '''
    ...
    
@overload
def event(event_name: Literal['onNpcActionSent'], priority: int = 9999) -> None:
    '''
    This event is triggered when server sends NPC action to streamed players.
    ## Parameters:
    * **npc_id**: int - the npc identifier.
    * **action_type**: int - the action type.
    * **action_id**: int - the unique action identifier.
    '''
    ...
    
@overload
def event(event_name: Literal['onNpcChangeHostPlayer'], priority: int = 9999) -> None:
    '''
    This event is triggered when NPC host is changed. Every remote NPC is hosted by one of spawned players in order to get valid position of NPC.
    ## Parameters:
    * **npc_id**: int - the npc identifier.
    * **current_id**: int - the id of the current host, can be -1 if there is no current host.
    * **previous_id**: int - the id of the previous host, can be -1 if there was no previous host.
    '''
    ...
    
@overload
def event(event_name: Literal['onNpcCreated'], priority: int = 9999) -> None:
    '''
    This event is triggered when remote NPC is created.
    ## Parameters:
    * **npc_id**: int - the id of the newly created remote npc.
    '''
    ...
    
@overload
def event(event_name: Literal['onNpcDestroyed'], priority: int = 9999) -> None:
    '''
    This event is triggered when remote NPC is destroyed.
    ## Parameters:
    * **npc_id**: int - the id of the destroyed remote npc.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerChangeColor'], priority: int = 9999) -> None:
    '''
    This event is triggered when player nickname color was changed for all players.
    ## Parameters:
    * **playerid**: int - the id of the player whose nickname color was changed.
    * **r**: int - the amount of red in the nickname color ``(0 - 255)``.
    * **g**: int - the amount of green in the nickname color ``(0 - 255)``.
    * **b**: int - the amount of blue in the nickname color ``(0 - 255)``.
    '''
    ...

@overload
def event(event_name: Literal['onPlayerChangeFocus'], priority: int = 9999) -> None:
    '''
    This event is triggered when player targets another player.
    ## Parameters:
    * **playerid**: int - the id of the player which changes the focus.
    * **oldFocusId**: int - the old playerid targeted by the player. Can be ``-1`` if player wasn't targeting other player.
    * **newFocusId**: int - the new playerid targeted by the player. Can be ``-1`` if player doesn't target anyone.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerChangeHealth'], priority: int = 9999) -> None:
    '''
    This event is triggered when player health changes.
    ## Parameters:
    * **playerid**: int - the id of the player whose health points gets changed.
    * **previous**: int - the previous health points of the player.
    * **current**: int - the current health points of the player.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerChangeMana'], priority: int = 9999) -> None:
    '''
    This event is triggered when player mana changes.
    ## Parameters:
    * **playerid**: int - the id of the player whose mana points gets changed.
    * **previous**: int - the previous mana points of the player.
    * **current**: int - the current mana points of the player.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerChangeMaxHealth'], priority: int = 9999) -> None:
    '''
    This event is triggered when player maximum health changes.
    ## Parameters:
    * **playerid**: int - the id of the player whose maximum health points gets changed.
    * **previous**: int - the previous maximum health points of the player.
    * **current**: int - the current maximum health points of the player.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerChangeMaxMana'], priority: int = 9999) -> None:
    '''
    This event is triggered when player maximum mana changes.
    ## Parameters:
    * **playerid**: int - the id of the player whose maximum mana points gets changed.
    * **previous**: int - the previous maximum mana points of the player.
    * **current**: int - the current maximum mana points of the player.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerChangeWeaponMode'], priority: int = 9999) -> None:
    '''
    This event is triggered when player changes the weapon mode.
    ## Parameters:
    * **playerid**: int - the id of the player which changes the weapon mode.
    * **previous**: int - the old weapon mode which was used by the player. For more information see Weapon mode constants.
    * **current**: int - the new weapon mode in which player is currently using. For more information see Weapon mode constants.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerChangeWorld'], priority: int = 9999) -> None:
    '''
    This event is triggered when player tries to change his currently played world (ZEN).
    ## Parameters:
    * **playerid**: int - the id of the player who tries to change the played world.
    * **world**: str - a filename name of the world.
    * **waypoint**: str - a name of the waypoint that the player will be teleported to.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerCommand'], priority: int = 9999) -> None:
    '''
    This event is triggered when a player uses command on the chat.
    Command always begins with forward slash ``/``.
    ## Parameters:
    * **playerid**: int - the id of the player who typed the command.
    * **command**: str - used command name on the chat.
    * **params**: str - command parameters divided by space.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerDamage'], priority: int = 9999) -> None:
    '''
    This event is triggered when one player hits another player.
    ## Parameters:
    * **playerid**: int - the id of the player who was hit.
    * **killerid**: int - the id of the killer. If killerid is set to ``-1``, it means that there was no killer. In this particular case damage source can be fall from a tall object or scripts.
    * **description**: DamageDescription - a structure containing damage information. For more information see DamageDescription
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerDead'], priority: int = 9999) -> None:
    '''
    This event is triggered when one player kills another player.
    ## Parameters:
    * **playerid**: int - the id of the player who died.
    * **killerid**: int - the id of the player who killed other player. If killerid is set to -1, it means that there was no killer.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerDisconnect'], priority: int = 9999) -> None:
    '''
    This event is triggered when a player gets disconnected with the server.
    ## Parameters:
    * **playerid**: int - the id of the player who joined the server.
    * **reason**: int - the reason why player got disconnected. For more information see Network constants.
    '''
    ...

# TODO: Отмена ивента    
@overload
def event(event_name: Literal['onPlayerDropItem'], priority: int = 9999) -> None:
    '''
    !!! note
        Cancelling this event will delete the dropped item from the world.
    This event is triggered when player drops an item from his inventory to the ground.
    ## Parameters:
    * **playerid**: int - the id of the player who tries to drop the item on the ground.
    * **itemGround**: ItemGround - the ground item object which represents the dropped item by the player.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerEnterWorld'], priority: int = 9999) -> None:
    '''
    This event is triggered when player entered the world (ZEN) and was successfully spawned in it.
    ## Parameters:
    * **playerid**: int - the id of the player who entered the world.
    * **world**: str - a filename name of the world.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerEquipAmulet'], priority: int = 9999) -> None:
    '''
    This event is triggered when player equips or unequips amulet. When item is unequiped, ``None`` is returned instead.
    ## Parameters:
    * **playerid**: int - the id of the player who equips an amulet.
    * **instance**: str|None - the item instance from Daedalus scripts.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerEquipArmor'], priority: int = 9999) -> None:
    '''
    This event is triggered when player equips or unequips armor. When item is unequiped, ``null`` is returned instead.
    ## Parameters:
    * **playerid**: int - the id of the player who equips an armor.
    * **instance**: str|None - the item instance from Daedalus scripts.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerEquipBelt'], priority: int = 9999) -> None:
    '''
    This event is triggered when player equips or unequips belt. When item is unequiped, ``null`` is returned instead.
    ## Parameters:
    * **playerid**: int - the id of the player who equips a belt.
    * **instance**: str|None - the item instance from Daedalus scripts.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerEquipHandItem'], priority: int = 9999) -> None:
    '''
    This event is triggered when game adds item to player hand, e.g: when player opens or consumes any item. When item is removed from hand, ``null is returned instead.
    ## Parameters:
    * **playerid**: int - the id of the player who equips a hand item.
    * **hand**: int - the id of the hand in which player holds item. For more information see Hand constants.
    * **instance**: str|None - the item instance from Daedalus scripts.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerEquipHelmet'], priority: int = 9999) -> None:
    '''
    This event is triggered when player equips or unequips helmet. When item is unequiped, ``null`` is returned instead.
    ## Parameters:
    * **playerid**: int - the id of the player who equips a helmet.
    * **instance**: str|None - the item instance from Daedalus scripts.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerEquipMeleeWeapon'], priority: int = 9999) -> None:
    '''
    This event is triggered when player equips or unequips melee weapon. When item is unequiped, ``null`` is returned instead.
    ## Parameters:
    * **playerid**: int - the id of the player who equips melee weapon.
    * **instance**: str|None - the item instance from Daedalus scripts.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerEquipRangedWeapon'], priority: int = 9999) -> None:
    '''
    This event is triggered when player equips or unequips ranged weapon. When item is unequiped, ``null`` is returned instead.
    ## Parameters:
    * **playerid**: int - the id of the player who equips ranged weapon.
    * **instance**: str|None - the item instance from Daedalus scripts.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerEquipRing'], priority: int = 9999) -> None:
    '''
    This event is triggered when player equips or unequips ring. When item is unequiped, ``null`` item id is returned instead.
    ## Parameters:
    * **playerid**: int - the id of the player who equips a ring.
    * **handId**: int - the hand id that the player is putting the ring on.
    * **instance**: str|None - the item instance from Daedalus scripts.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerEquipShield'], priority: int = 9999) -> None:
    '''
    This event is triggered when player equips or unequips shield. When item is unequiped, ``null`` is returned instead.
    ## Parameters:
    * **playerid**: int - the id of the player who equips a shield.
    * **instance**: str|None - the item instance from Daedalus scripts.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerEquipSpell'], priority: int = 9999) -> None:
    '''
    This event is triggered when player equips or unequips scroll or rune. When item is unequiped, ``null`` is returned instead.
    ## Parameters:
    * **playerid**: the id of the player who equips a spell.
    * **slotId**: int - the slot id that the player puts the spell on in range <0, 6>.
    * **instance**: str|None - the item instance from Daedalus scripts.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerJoin'], priority: int = 9999) -> None:
    '''
    This event is triggered when a player successfully joined the server.
    ## Parameters:
    * **playerid**: int - the id of the player who joined the server.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerMessage'], priority: int = 9999) -> None:
    '''
    This event is triggered when a player types the message on the chat.
    ## Parameters:
    * **playerid**: int - the id of the player who typed the message.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerMobInteract'], priority: int = 9999) -> None:
    '''
    This event is triggered when player interacts with any kind of mob object in the world. In Gothic, mobs are special vobs on the map, that hero can interact with. For example bed, door, chest etc.
    ## Parameters:
    * **playerid**: int - the id of the player who interacts with mob.
    * **from**: int - represents previous state of mob. If value is ``1``, then mob was used, in any other case value is ``0``.
    * **to**: int - represents current state of mob. If value is ``1``, then mob is used, in any other case value is ``0``.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerRespawn'], priority: int = 9999) -> None:
    '''
    This event is triggered when a player respawns after death.
    ## Parameters:
    * **playerid**: int - the id of the player who respawned after death.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerShoot'], priority: int = 9999) -> None:
    '''
    This event is triggered when player shoot using ranged weapon.
    ## Parameters:
    * **playerid**: int - the id of the player who just shot.
    * **munition**: str|None - the item instance from Daedalus scripts.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerSpellCast'], priority: int = 9999) -> None:
    '''
    !!! note
        Right now transformation and summon spells are not supported, despite this event will be triggered for them. Cancelling this event willl prevent this action to be synced to other players.
    This event is triggered when player is casting some spell.
    ## Parameters:
    * **playerid**: int - the id of the player who casts the spell.
    * **munition**: str|None - the item instance from Daedalus scripts.
    * **spellLevel**: int - the level of charged spell
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerSpellSetup'], priority: int = 9999) -> None:
    '''
    This event is triggered when player prepares the spell.
    ## Parameters:
    * **playerid**: int - the id of the player who prepares the spell.
    * **munition**: str|None - the item instance from Daedalus scripts.
    '''
    ...

# TODO: Отмена ивента    
@overload
def event(event_name: Literal['onPlayerTakeItem'], priority: int = 9999) -> None:
    '''
    !!! note
        Even if this event is triggered it doesn't mean, that player will get item to his inventory. It only means, that the player tried to get the item from the ground. Server is the last decide if the item can be taken from the ground. Canceling this event will prevent the item to be taken from the ground.
    This event is triggered when player takes an item from the ground.
    ## Parameters:
    * **playerid**: int - the id of the player who tries to take the ground item.
    * **itemGround**: ItemGround - the ground item object which player tried to to take.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerTeleport'], priority: int = 9999) -> None:
    '''
    This event is triggered when player gets teleported by the game to the specified vob.
    ## Parameters:
    * **playerid**: int - the id of the player who gets teleported by the game.
    * **vobName**: str - represents the name of the vob that player gets teleported to.
    '''
    ...
    
@overload
def event(event_name: Literal['onPlayerToggleFaceAni'], priority: int = 9999) -> None:
    '''
    This event is triggered when player face animation is toggled (played or stopped), due to eating or other activities.
    ## Parameters:
    * **playerid**: int - the id of the player which toggled face animation.
    * **aniName**: str - the face animation name.
    * **toggle**: bool - ``True`` when player is started playing face animation, otherwise ``False``.
    '''
    ...
    
def event(event_name: str, priority: int = 9999) -> None:
    def inlineEvt(func):
        if event_name not in eventList:
            addEvent(event_name)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        
        eventList[event_name].append({'function': wrapper, 'priority': priority})
        eventList[event_name].sort(key = lambda x: x['priority'])
        return wrapper
    return inlineEvt
    
def removeEventHandler(name : str, func : object):
    """
    This function will unbind function from specified event.
    Original: [removeEventHandler](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/event/removeEventHandler/)
    
    ## Declaration
    ```python
    def removeEventHandler(name : str, func : object)
    ```
    
    ## Parameters
    * `str` **name**: the name of the event
    * `object` **func**: the reference to a function which is currently bound to specified event.
    
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
            
def toggleEvent(name : str, toggle : bool):
    '''
    !!! note
        By default every event is toggled `on` (enabled).
        
    This function will toggle event (enable or disable it globally). By toggling event off, you can completely disable certain event from calling it's handlers.
    Original: [toggleEvent](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/event/toggleEvent/)
    
    ## Declaration
    ```python
    def toggleEvent(name : str, toggle : bool)
    ```
    
    ## Parameters
    * `str` **name**: the name of the event
    * `bool` **toggle**: `false` if you want to disable the event, otherwise true.
    
    ## Usage
    ```python
    import g2o
    
    @g2o.event('onTime')
    def onTimeEvt(**kwargs):
        print('Calling only once')
        g2o.toggleEvent('onTime', false)
    ```
    '''
    if not toggle and name not in disabledEventList:
        disabledEventList.append(name)
    elif toggle and name in disabledEventList:
        disabledEventList.remove(name)
        
def removeEvent(name : str):
    '''
    !!! warning
        Removing an event also cause all event handlers to unregister.
    This function will unregister an event with specified name.
    Original: [removeEvent](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/shared-functions/event/removeEvent/)
    
    ## Declaration
    ```python
    def removeEvent(name : str)
    ```
    
    ## Parameters
    * `str` **name**: the name of the event
    
    ## Usage
    ```python
    import g2o
    
    @g2o.event('onTime')
    def onTimeEvt(**kwargs):
        print('Calling only once')
        g2o.removeEvent('onTime')
    ```
    '''
    if name in eventList:
        eventList.pop(name)

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

addEvent('onPlayerCommand')
addEvent('onPlayerDamage')
addEvent('onPlayerDead')
addEvent('onPlayerDisconnect')
addEvent('onPlayerDropItem')
addEvent('onPlayerEnterWorld')
addEvent('onPlayerJoin')
addEvent('onPlayerMessage')
addEvent('onPlayerMobInteract')
addEvent('onPlayerRespawn')
addEvent('onPlayerShoot')
addEvent('onPlayerSpellCast')
addEvent('onPlayerSpellSetup')
addEvent('onPlayerTakeItem')
addEvent('onPlayerTeleport')
addEvent('onPlayerToggleFaceAni')
    
addEvent('onPlayerEquipAmulet')
addEvent('onPlayerEquipArmor')
addEvent('onPlayerEquipBelt')
addEvent('onPlayerEquipHandItem')
addEvent('onPlayerEquipHelmet')
addEvent('onPlayerEquipMeleeWeapon')
addEvent('onPlayerEquipRangedWeapon')
addEvent('onPlayerEquipRing')
addEvent('onPlayerEquipShield')
addEvent('onPlayerEquipSpell')

addEvent('onPacket')

addEvent('onPlayerUseCheat')

addEvent('onNpcActionFinished')
addEvent('onNpcActionSent')
addEvent('onNpcChangeHostPlayer')
addEvent('onNpcCreated')
addEvent('onNpcDestroyed')

addEvent('onWebsocketConnect')
addEvent('onWebsocketDisconnect')