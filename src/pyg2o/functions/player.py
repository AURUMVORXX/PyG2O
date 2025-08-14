from ..server import PythonWebsocketServer
from ..call_repr import get_call_repr
from typing import Optional

async def addBan(info : dict) -> bool:
    """
    !!! note
        All properties should be of primitive types and are optional, but you still need to provide at least one of them.
    !!! note
        The reason string can't be longer than 255 characters.
    !!! note
        The meta table is used for storing custom data.
    This function will add a new ban on the server.
    Original: [addBan](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/addBan/)
    
    ## Declaration
    ```python
    async def addBan(info : dict) -> bool
    ```
    ## Parameters
    `dict {serial, mac, ip, name, reason, timestamp, meta={..}}` **info**: the ban properties.
    `int` **host_id**: the player host identifier.
    ## Returns
    `bool`: `true` if ban was added, otherwise `false`.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def applyPlayerOverlay(id : int, overlay : str) -> bool:
    """
    This function will apply animation overlay on player for all players.
    Original: [applyPlayerOverlay](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/applyPlayerOverlay/)
    
    ## Declaration
    ```python
    async def applyPlayerOverlay(id : int, overlay : str) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **overlay**: the overlay Mds name, e.g. 'HUMANS_MILITIA.MDS'
    ## Returns
    `bool`: `true` if animation overlay was successfully applied on player, otherwise `false`.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def ban(id : int, minutes : int, reason : str):
    """
    !!! note
        The reason string can't be longer than 255 characters.
    This function will ban the player on the server.
    Original: [ban](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/ban/)
    
    ## Declaration
    ```python
    async def ban(id : int, minutes : int, reason : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **minutes**: the time how long ban will take in minutes. Passing `0` will cause the player to have permanent ban.
    `str` **reason**: the reason why player was banned.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def drawWeapon(id : int, weaponMode : int):
    """
    This function will cause player to draw a weapon. If hero/npc doesn't have equipped weapon assosiated with the preffered weapon mode, then it will try to draw melee weapon, otherwise `WEAPONMODE_FIST` will be used instead.
    Original: [drawWeapon](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/drawWeapon/)
    
    ## Declaration
    ```python
    async def drawWeapon(id : int, weaponMode : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **weaponMode**: the preffered weapon mode. For more information see [Weapon mode constants](../../constants/weapon-mode.md).
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def equipItem(id : int, instance : str, slotId : int = -1):
    """
    !!! note
        If you want to equip weapon/shield, first make sure that player is in `WEAPONMODE_NONE`.
    This function is used to equip item on player for all players.
    Original: [equipItem](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/equipItem/)
    
    ## Declaration
    ```python
    async def equipItem(id : int, instance : str, slotId : int = -1)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **instance**: the item instance from Daedalus scripts.
    `int` **slotId**: the slot id in which you want to equip item on player, e.g scrolls, runes, rings, by default the item will be equipped on the first free slot.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerAmulet(id : int) -> str:
    """
    This function will get the equipped player amulet.
    Original: [getPlayerAmulet](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerAmulet/)
    
    ## Declaration
    ```python
    async def getPlayerAmulet(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerAngle(id : int) -> float:
    """
    This function will get the player facing rotation on y axis.
    Original: [getPlayerAngle](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerAngle/)
    
    ## Declaration
    ```python
    async def getPlayerAngle(id : int) -> float
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `float`: the facing rotation on y axis.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerAni(id : int) -> str:
    """
    This function will get the player facing rotation on y axis.
    Original: [getPlayerAni](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerAni/)
    
    ## Declaration
    ```python
    async def getPlayerAni(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the ani name, e.g: `"S_RUN"`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerOverlays(id : int) -> list[str]:
    """
    This function will get the player/npc active animations overlays.
    
    ## Declaration
    ```python
    async def getPlayerAni(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `list[str]`: the list of animation overlays as strings or ``None`` if player isn't created.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerArmor(id : int) -> str:
    """
    This function will get the equipped player armor.
    Original: [getPlayerArmor](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerArmor/)
    
    ## Declaration
    ```python
    async def getPlayerArmor(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerAtVector(id : int) -> Optional[tuple]:
    """
    This function will get player at vector.
    Original: [getPlayerAtVector](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerAtVector/)
    
    ## Declaration
    ```python
    getPlayerAtVector(id : int) -> Optional[tuple]
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `tuple (x, y, z)`: the player at vector.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return (result['x'], result['y'], result['z']) if result is not None else (None, None, None)

async def getPlayerBelt(id : int) -> str:
    """
    This function will get the equipped player belt.
    Original: [getPlayerBelt](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerBelt/)
    
    ## Declaration
    ```python
    async def getPlayerBelt(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerCameraPosition(id : int) -> Optional[tuple]:
    """
    This function will get the player camera position in world.
    Original: [getPlayerCameraPosition](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerCameraPosition/)
    
    ## Declaration
    ```python
    getPlayerCameraPosition(id : int) -> Optional[tuple]
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `tuple (x, y, z)`: the dictionary that represents camera position.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return (result['x'], result['y'], result['z']) if result is not None else (None, None, None)

async def getPlayerChunk(id: int):
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return (result['x'], result['y']) if result is not None else (None, None)

async def getPlayerCollision(id : int) -> bool:
    """
    This function will get the player collision.
    Original: [getPlayerCollision](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerCollision/)
    
    ## Declaration
    ```python
    async def getPlayerCollision(id : int) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `bool`: `true` if collision is enabled, otherwise `false`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerColor(id : int) -> Optional[tuple]:
    """
    This function will get the player nickname color.
    Original: [getPlayerColor](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerColor/)
    
    ## Declaration
    ```python
    async def getPlayerColor(id : int) -> Optional[tuple]
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `tuple (r, g, b)`: the player nickname color.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return (result['r'], result['g'], result['b']) if result is not None else (None, None, None)

async def getPlayerContext(id : int, type : int) -> int:
    """
    This function is used to get player script context. For more information see [this article](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/multiplayer/script-context/).
    Original: [getPlayerContext](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerContext/)
    
    ## Declaration
    ```python
    async def getPlayerContext(id : int, type : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the value stored within selected context.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerDexterity(id : int) -> int:
    """
    This function will get the player dexterity points.
    Original: [getPlayerDexterity](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerDexterity/)
    
    ## Declaration
    ```python
    async def getPlayerDexterity(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the dexterity points amount.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerFaceAnis(id : int) -> list:
    """
    This function will get the player dexterity points.
    Original: [getPlayerFaceAnis](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerFaceAnis/)
    
    ## Declaration
    ```python
    async def getPlayerFaceAnis(id : int) -> list
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `list [{aniName, layer}]`: the list of objects describing face animation.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerFatness(id : int) -> float:
    """
    This function will get the player fatness factor.
    Original: [getPlayerFatness](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerFatness/)
    
    ## Declaration
    ```python
    async def getPlayerFatness(id : int) -> float
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `float`: the fatness ratio.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerFocus(id : int) -> int:
    """
    This function is used to get current focused player by other player.
    Original: [getPlayerFocus](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerFocus/)
    
    ## Declaration
    ```python
    async def getPlayerFocus(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the current focused player id. In case were there is no focus returns `-1`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerHealth(id : int) -> int:
    """
    This function will get the player health points.
    Original: [getPlayerHealth](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerHealth/)
    
    ## Declaration
    ```python
    async def getPlayerHealth(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the health points amount.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerHelmet(id : int) -> str:
    """
    This function will get the equipped player helmet.
    Original: [getPlayerHelmet](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerHelmet/)
    
    ## Declaration
    ```python
    async def getPlayerHelmet(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerIP(id : int) -> str:
    """
    This function will get the player ipv4 ip address.
    Original: [getPlayerIP](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerIP/)
    
    ## Declaration
    ```python
    async def getPlayerIP(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the player ip address, e.g `"127.0.0.1"`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerInstance(id : int) -> str:
    """
    This function will get the player instance.
    Original: [getPlayerInstance](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerInstance/)
    
    ## Declaration
    ```python
    async def getPlayerInstance(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the player instance.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerInvisible(id : int) -> bool:
    """
    This function will get the player invisiblity for all players.
    Original: [getPlayerInvisible](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerInvisible/)
    
    ## Declaration
    ```python
    async def getPlayerInvisible(id : int) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `bool`: `true` when player is invisible for all players, otherwise `false`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerMacAddr(id : int) -> str:
    """
    !!! note
        The function can return null if player isn't connected.
    This function will get the player MAC address.
    MAC is used to uniquely idientify each player,
    however it can be changed/spoofed by more advance users.
    Original: [getPlayerMacAddr](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerMacAddr/)
    
    ## Declaration
    ```python
    async def getPlayerMacAddr(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the player mac address, e.g `"00-1b-44-11-3a-b7"`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerMana(id : int) -> int:
    """
    This function will get the player mana points.
    Original: [getPlayerMana](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerMana/)
    
    ## Declaration
    ```python
    async def getPlayerMana(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the mana points amount.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerMaxHealth(id : int) -> int:
    """
    This function will get the player max health points.
    Original: [getPlayerMaxHealth](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerMaxHealth/)
    
    ## Declaration
    ```python
    async def getPlayerMaxHealth(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the max health points amount.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerMaxMana(id : int) -> int:
    """
    This function will get the player max mana points.
    Original: [getPlayerMaxMana](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerMaxMana/)
    
    ## Declaration
    ```python
    async def getPlayerMaxMana(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the max mana points amount.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerMeleeWeapon(id : int) -> str:
    """
    This function will get the equipped player melee weapon.
    Original: [getPlayerMeleeWeapon](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerMeleeWeapon/)
    
    ## Declaration
    ```python
    async def getPlayerMeleeWeapon(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerName(id : int) -> str:
    """
    This function will get the player nickname.
    Original: [getPlayerName](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerName/)
    
    ## Declaration
    ```python
    async def getPlayerName(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the player nickname.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerPing(id : int) -> int:
    """
    !!! note
        The function can return `-1` if player isn't connected.
    This function will get the player ping. Ping gets updated after each 2500 miliseconds.
    Original: [getPlayerPing](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerPing/)
    
    ## Declaration
    ```python
    async def getPlayerPing(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the current player ping.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerPosition(id : int) -> Optional[tuple]:
    """
    This function will get the player world position.
    Original: [getPlayerPosition](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerPosition/)
    
    ## Declaration
    ```python
    async def getPlayerPosition(id : int) -> Optional[tuple]
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `tuple (x, y, z)`: the player world position.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return (result['x'], result['y'], result['z']) if result is not None else (None, None, None)

async def getPlayerRangedWeapon(id : int) -> str:
    """
    This function will get the equipped player ranged weapon.
    Original: [getPlayerRangedWeapon](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerRangedWeapon/)
    
    ## Declaration
    ```python
    async def getPlayerRangedWeapon(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerRespawnTime(id : int) -> int:
    """
    This function will get the player time to respawn after death.
    Original: [getPlayerRespawnTime](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerRespawnTime/)
    
    ## Declaration
    ```python
    async def getPlayerRespawnTime(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the player respawn time.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerRing(id : int, handId : int) -> str:
    """
    This function will get the equipped player ring.
    Original: [getPlayerRing](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerRing/)
    
    ## Declaration
    ```python
    dasync def getPlayerRing(id : int, handId : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **handId**: the handId. For more information see [Hand constants](../../constants/hand.md).
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerScale(id : int) -> Optional[tuple]:
    """
    This function will get the player scale.
    Original: [getPlayerScale](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerScale/)
    
    ## Declaration
    ```python
    async def getPlayerScale(id : int) -> Optional[tuple]
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `tuple (x, y, z)`: the player scale.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return (result['x'], result['y'], result['z']) if result is not None else (None, None, None)

async def getPlayerSerial(id : int) -> str:
    """
    !!! note
        The function can return `null` if player isn't connected.
    !!! note
        For some players (e.g: that are playing on linux using WINE) this function might return empty string.
    This function will get the player serial.
    Serial is used to uniquely idientify each player.
    Original: [getPlayerSerial](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerSerial/)
    
    ## Declaration
    ```python
    async def getPlayerSerial(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the player serial.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerShield(id : int) -> str:
    """
    This function will get the equipped player shield.
    Original: [getPlayerShield](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerShield/)
    
    ## Declaration
    ```python
    async def getPlayerShield(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerSkillWeapon(id : int, skillId : int) -> int:
    """
    This function will get the player skill weapon.
    Original: [getPlayerSkillWeapon](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerSkillWeapon/)
    
    ## Declaration
    ```python
    async def getPlayerSkillWeapon(id : int, skillId : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **skillId**: For more information see [Skill weapon constants](../../constants/skill-weapon.md).
    ## Returns
    `int`: the percentage value in range <0, 100>.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerSpell(id : int, slotId : int) -> str:
    """
    This function will get the equipped player spell.
    Original: [getPlayerSpell](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerSpell/)
    
    ## Declaration
    ```python
    dasync def getPlayerSpell(id : int, slotId : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **slotId**: the equipped slotId in range <0, 6>.
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerStrength(id : int) -> int:
    """
    This function will get the player strength points.
    Original: [getPlayerStrength](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerStrength/)
    
    ## Declaration
    ```python
    async def getPlayerStrength(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the strength points amount.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerTalent(id : int, talentId : int) -> int:
    """
    This function will get the player talent.
    Original: [getPlayerTalent](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerTalent/)
    
    ## Declaration
    ```python
    async def getPlayerTalent(id : int, talentId : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **talentId**: the talent id. For more information see [Talent constants](../../constants/talent.md).
    ## Returns
    `int`: the current talent value for specific talent id.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result
    
async def getPlayerUID(id : int) -> str:
    """
    This function will get the player pc unique identifier.
    Original: [getPlayerUID](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerUID/)
    
    ## Declaration
    ```python
    async def getPlayerUID(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the player UID.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerVirtualWorld(id : int) -> int:
    """
    This function will get the player virtual world.
    Original: [getPlayerVirtualWorld](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerVirtualWorld/)
    
    ## Declaration
    ```python
    async def getPlayerVirtualWorld(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the player virtual world id.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerVisual(id : int) -> Optional[tuple]:
    """
    This function will get the player visual.
    Original: [getPlayerVisual](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerVisual/)
    
    ## Declaration
    ```python
    async def getPlayerVisual(id : int) -> Optional[tuple]
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `tuple (bodyModel, bodyTxt, headModel, headTxt)`: player visual.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return (result['bodyModel'], result['bodyTxt'], result['headModel'], result['headTxt']) if result is not None else (None, None, None, None)

async def getPlayerWeaponMode(id : int) -> int:
    """
    This function will get the player weapon mode.
    Original: [getPlayerWeaponMode](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerWeaponMode/)
    
    ## Declaration
    ```python
    async def getPlayerWeaponMode(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the player weaponMode, for more information see [Weapon mode constants](../../constants/weapon-mode.md).
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getPlayerWorld(id : int) -> str:
    """
    This function will get the player world.
    Original: [getPlayerWorld](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerWorld/)
    
    ## Declaration
    ```python
    async def getPlayerWorld(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the player world.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def giveItem(id : int, instance : str, amount : int):
    """
    This function is used to give item for player.
    Original: [giveItem](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/giveItem/)
    
    ## Declaration
    ```python
    async def giveItem(id : int, instance : str, amount : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **instance**: the item instance from Daedalus scripts.
    `int` **amount**: the amount of item, e.g: `1000` gold coins.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def hitPlayer(id : int, target_id : int) -> bool:
    """
    This function is used to simulate hit between attacker and victim. It will only work with if killer or victim is a real player. The victim will receive damage calculated damage by the game.
    Original: [hitPlayer](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/hitPlayer/)
    
    ## Declaration
    ```python
    async def hitPlayer(id : int, target_id : int) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **target_id**: the victim id.
    ## Returns
    `bool`: `true` if hit was successfully simulated, otherwise `false`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def isPlayerConnected(id : int) -> bool:
    """
    The function is used to check whether player is connected to the server.
    Original: [isPlayerConnected](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/isPlayerConnected/)
    
    ## Declaration
    ```python
    async def isPlayerConnected(id : int) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `bool`: `true` when player is connected, otherwise `false`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def isPlayerDead(id : int) -> bool:
    """
    The function is used to check whether player is dead.
    Original: [isPlayerDead](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/isPlayerDead/)
    
    ## Declaration
    ```python
    async def isPlayerDead(id : int) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `bool`: `true` when player is dead, otherwise `false`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def isPlayerSpawned(id : int) -> bool:
    """
    The function is used to check whether player is spawned.
    Original: [isPlayerSpawned](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/isPlayerSpawned/)
    
    ## Declaration
    ```python
    async def isPlayerSpawned(id : int) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `bool`: `true` when player is spawned, otherwise `false`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def isPlayerUnconscious(id : int) -> bool:
    """
    The function is used to check whether player is in unconscious state. The player will be unconscious, when it gets beaten up, but not killed.
    Original: [isPlayerUnconscious](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/isPlayerUnconscious/)
    
    ## Declaration
    ```python
    async def isPlayerUnconscious(id : int) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `bool`: `true` when player is unconscious, otherwise `false`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def kick(id : int, reason : str):
    """
    !!! note
        The reason string can't be longer than 255 characters.
    This function will kick the player from the server.
    Original: [kick](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/kick/)
    
    ## Declaration
    ```python
    async def kick(id : int, reason : str)
    ```
    ## Parameters
    `int` **id**: the reason why player was kicked.
    `str` **reason**: the reason why player was kicked.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def playAni(id : int, aniName : str):
    """
    This function is used to play animation on player for all players.
    Original: [playAni](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/playAni/)
    
    ## Declaration
    ```python
    async def playAni(id : int, aniName : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **aniName**: the name of the animation, e.g: `"T_STAND_2_SIT"`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def playFaceAni(id : int, aniName : str):
    """
    This function is used to play face animation on player.
    Original: [playFaceAni](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/playFaceAni/)
    
    ## Declaration
    ```python
    async def playFaceAni(id : int, aniName : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **aniName**: the name of the animation, e.g: `"S_FRIENDLY"`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def fadeOutAni(id : int, aniName : str):
    """
    This function is used to gracefully stop played animation on player/npc for all players.
    
    ## Declaration
    ```python
    async def playFaceAni(id : int, aniName : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **aniName**: the name of the animation that you want to stop. The default value is empty string, which means that the first active ani will be stopped.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def readySpell(id : int, slotId : int, manaInvested : int):
    """
    This function will cause player to ready equipped spell.
    Original: [readySpell](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/readySpell/)
    
    ## Declaration
    ```python
    async def readySpell(id : int, slotId : int, manaInvested : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **slotId**: the equipped spell slotId in range <0, 6>.
    `int` **manaInvested**: the spell cast cost in mana points.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def removeItem(id : int, instance : str, amount : int):
    """
    This function is used to remove item from player.
    Original: [removeItem](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/removeItem/)
    
    ## Declaration
    ```python
    async def removeItem(id : int, instance : str, amount : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **instance**: the item instance from Daedalus scripts.
    `int` **amount**: the amount of item, e.g: `1000` gold coins.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def removePlayerOverlay(id : int, overlay : str) -> bool:
    """
    This function will remove animation overlay from player for all players.
    Original: [removePlayerOverlay](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/removePlayerOverlay/)
    
    ## Declaration
    ```python
    async def removePlayerOverlay(id : int, overlay : str) -> bool:
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **overlay**: the overlay Mds name, e.g. 'HUMANS_MILITIA.MDS'
    ## Returns
    `bool`: `true` if animation overlay was successfully removed from player, otherwise `false`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def removeWeapon(id : int):
    """
    This function will cause player to hide a weapon.
    Original: [removeWeapon](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/removeWeapon/)
    
    ## Declaration
    ```python
    async def removeWeapon(id : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerAngle(id : int, angle : float):
    """
    This function will set the player facing rotation on y axis for all players.
    Original: [setPlayerAngle](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerAngle/)
    
    ## Declaration
    ```python
    async def setPlayerAngle(id : int, angle : float)
    ```
    ## Parameters
    `int` **id**: the player id.
    `float` **angle**: the facing rotation on y axis.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerCollision(id : int, collision : bool):
    """
    This function will set the player collision.
    Original: [setPlayerCollision](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerCollision/)
    
    ## Declaration
    ```python
    async def setPlayerCollision(id : int, collision : bool)
    ```
    ## Parameters
    `int` **id**: the player id.
    `bool` **collision**: `true` if want to enable collision, otherwise `false`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerColor(id : int, r : int, g : int, b : int):
    """
    This function will set the player nickname color for all players.
    Original: [setPlayerColor](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerColor/)
    
    ## Declaration
    ```python
    async def setPlayerColor(id : int, r : int, g : int, b : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **r**: the red color component in RGB model.
    `int` **g**: the green color component in RGB model.
    `int` **b**: the blue color component in RGB model.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerContext(id : int, type : int, value : int):
    """
    This function is used to set player script context. For more information see [this article](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/multiplayer/script-context/).
    Original: [setPlayerContext](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerContext/)
    
    ## Declaration
    ```python
    async def setPlayerContext(id : int, type : int, value : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **type**: the type of modified context.
    `int` **value**: the new value written into context.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerDexterity(id : int, dexterity : int):
    """
    This function will set the player dexterity points for all players.
    Original: [setPlayerDexterity](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerDexterity/)
    
    ## Declaration
    ```python
    async def setPlayerDexterity(id : int, dexterity : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **dexterity**: the dexterity points amount.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerFatness(id : int, fatness : float):
    """
    This function will set the player fatness factor for all players.
    Original: [setPlayerFatness](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerFatness/)
    
    ## Declaration
    ```python
    async def setPlayerFatness(id : int, fatness : float)
    ```
    ## Parameters
    `int` **id**: the player id.
    `float` **fatness**: ratio of how much you want to make player fatter, `0.0` is default fatness (none).
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerHealth(id : int, health : int):
    """
    This function will set the player health points for all players.
    Original: [setPlayerHealth](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerHealth/)
    
    ## Declaration
    ```python
    async def setPlayerHealth(id : int, health : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **health**: health points amount.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerInstance(id : int, instance : str):
    """
    This function will set the player instance for all players. Instance describes the player attributes, like visual, stats, and more.. You can find more information about npc instances in daedalus scripts.
    Original: [setPlayerInstance](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerInstance/)
    
    ## Declaration
    ```python
    async def setPlayerInstance(id : int, instance : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **instance**: the new player instance.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerInvisible(id : int, toggle : bool):
    """
    This function will toggle the player invisiblity for all players.
    The invisible player will still see other visible players.
    Original: [setPlayerInvisible](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerInvisible/)
    
    ## Declaration
    ```python
    async def setPlayerInvisible(id : int, toggle : bool)
    ```
    ## Parameters
    `int` **id**: the player id.
    `bool` **toggle**: `true` if the player should be invisible for all players, otherwise `false`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerMana(id : int, mana : int):
    """
    This function will set the player mana points for all players.
    Original: [setPlayerMana](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerMana/)
    
    ## Declaration
    ```python
    async def setPlayerMana(id : int, Mana : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **mana**: mana points amount.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerMaxHealth(id : int, maxHealth : int):
    """
    This function will set the player max health points for all players.
    Original: [setPlayerMaxHealth](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerMaxHealth/)
    
    ## Declaration
    ```python
    async def setPlayerMaxHealth(id : int, maxHealth : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **maxHealth**: max health points amount.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerMaxMana(id : int, maxMana : int):
    """
    This function will set the player max mana points for all players.
    Original: [setPlayerMaxMana](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerMaxMana/)
    
    ## Declaration
    ```python
    async def setPlayerMaxMana(id : int, maxMana : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **maxMana**: max mana points amount.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerName(id : int, name : str) -> bool:
    """
    !!! note
        The name string can't be longer than 18 characters, and must be unique for each player.
    This function will set the player unique nickname for all players.
    Original: [setPlayerName](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerName/)
    
    ## Declaration
    ```python
    async def setPlayerName(id : int, name : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **instance**: the new unique player name.
    ## Returns
    `bool`: `true` when unique player name was set, otherwise `false`.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerPosition(id : int, x : float, y : float, z : float) -> Optional[tuple]:
    """
    !!! note
        This functions supports ``pass_exception: bool`` optional argument for manual handling exceptions.
    This function will set the player world position for all players.
    Original: [setPlayerPosition](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerPosition/)
    
    ## Declaration
    ```python
    async def setPlayerPosition(id : int, x : float, y : float, z : float) -> Optional[tuple]
    ```
    ## Parameters
    `int` **id**: the player id.
    `float` **x**: the position in the world on the x axis.
    `float` **y**: the position in the world on the y axis.
    `float` **z**: the position in the world on the z axis.
    OR
    `tuple(x, y, z)` **pos**: the position in the world on the XYZ axis.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return (result['x'], result['y'], result['z']) if result is not None else (None, None, None)

async def setPlayerRespawnTime(id : int, respawnTime : int):
    """
    !!! note
        The respawnTime can't be smaller than 1001 miliseconds.
    This function will set the player time to respawn after death. If set to 0, respawn is disabled for selected player.
    Original: [setPlayerRespawnTime](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerRespawnTime/)
    
    ## Declaration
    ```python
    async def setPlayerRespawnTime(id : int, respawnTime : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **respawnTime**: the new respawn time in miliseconds.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerScale(id : int, x : float, y : float, z : float) -> Optional[tuple]:
    """
    !!! note
        This functions supports ``pass_exception: bool`` optional argument for manual handling exceptions.
    This function will set the player scale for all players.
    Original: [setPlayerScale](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerScale/)
    
    ## Declaration
    ```python
    async def setPlayerScale(id : int, x : float, y : float, z : float) -> Optional[tuple]
    ```
    ## Parameters
    `int` **id**: the player id.
    `float` **x**: the scale factor on x axis.
    `float` **y**: the scale factor on y axis.
    `float` **z**: the scale factor on z axis.
    OR
    `tuple(x, y, z)` **pos**: the scale factor on the XYZ axis.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return (result['x'], result['y'], result['z']) if result is not None else (None, None, None)

async def setPlayerSkillWeapon(id : int, skillId : int, percentage : int):
    """
    This function will set the player skill weapon for all players.
    Original: [setPlayerSkillWeapon](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerSkillWeapon/)
    
    ## Declaration
    ```python
    async def setPlayerSkillWeapon(id : int, skillId : int, percentage : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **skillId**: For more information see [Skill weapon constants](../../constants/skill-weapon.md).
    `int` **percentage**: the percentage in range <0, 100>.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerStrength(id : int, strength : int):
    """
    This function will set the player strength points for all players.
    Original: [setPlayerStrength](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerStrength/)
    
    ## Declaration
    ```python
    async def setPlayerStrength(id : int, strength : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **strength**: strength points amount.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerTalent(id : int, talentId : int, talentValue : int):
    """
    This function will toggle the player talent for all players.
    Original: [setPlayerTalent](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerTalent/)
    
    ## Declaration
    ```python
    async def setPlayerTalent(id : int, talentId : int, talentValue : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **talentId**: the talent id. For more information see [Talent constants](../../constants/talent.md).
    `int` **talentValue**: the new talent value.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerVirtualWorld(id : int, virtualWorld : int):
    """
    This function will set the player virtual world for all players.
    Virtual worlds are separate logical worlds on the same physical world.
    Original: [setPlayerVirtualWorld](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerVirtualWorld/)
    
    ## Declaration
    ```python
    async def setPlayerVirtualWorld(id : int, virtualWorld : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **virtualWorld**: the virtual world id in range <0, 65535>.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerVisual(id : int, bodyModel : str, bodyTxt : int, headModel : str, headTxt : int):
    """
    This function will set the player visual for all players.
    Original: [setPlayerVisual](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerVisual/)
    
    ## Declaration
    ```python
    async def setPlayerVisual(id : int, bodyModel : str, bodyTxt : int, headModel : str, headTxt : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **bodyModel**: the name of the body model (ASC), e.g: `HUM_BODY_NAKED0`.
    `int` **bodyTxt**: the numeric id of body texture file. Texture id can be read from V(number) filename part, for example, in this file: `HUM_BODY_NAKED_V8_C0-C.TEX` id is 8.
    `str` **headModel**: the name of the head model (MMS), e.g: `HUM_HEAD_PONY`.
    `int` **headTxt**: the numeric id of head texture file. Texture id can be read from V(number) filename part, for example, in this file: `HUM_HEAD_V18_C0-C.TEX` id is 18.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerWeaponMode(id : int, weaponMode : int):
    """
    This function will set the player weapon mode for all players.
    Original: [setPlayerWeaponMode](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerWeaponMode/)
    
    ## Declaration
    ```python
    async def setPlayerWeaponMode(id : int, weaponMode : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **weaponMode**: For more information see [Weapon mode constants](../../constants/weapon-mode.md).
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setPlayerWorld(id : int, world : str, startPointName : str = ""):
    """
    This function will set the player world for all players.
    Original: [setPlayerWorld](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerWorld/)
    
    ## Declaration
    ```python
    async def setPlayerWorld(id : int, world : str, startPointName : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **world**: the path to the target world (.ZEN). World path is relative to directory `_Work/Data/Worlds`.
    `str` **startPointName**: the name of the vob to which the player will be moved. If passed empty string, player will be placed at world start point. If vob with specified name doesn't exists or world doesn't have start point, player will be placed at {0, 150, 0} coordinates.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def spawnPlayer(id : int):
    """
    !!! note
        Unspawned players can't see other players, items, etc. and are invisible for others.
    This function will spawn the player.
    Players are always in unspawned state after joining to server or after respawning.
    Original: [spawnPlayer](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/spawnPlayer/)
    
    ## Declaration
    ```python
    async def spawnPlayer(id : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def stopAni(id : int, aniName : str = ""):
    """
    This function is used to stop played animation on player for all players.
    Original: [stopAni](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/stopAni/)
    
    ## Declaration
    ```python
    async def stopAni(id : int, aniName : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **aniName**: the name of the animation that you want to stop. The default value is \"\" which means that the first active ani will be stopped.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def stopFaceAni(id : int, aniName : str = ""):
    """
    This function is used to stop played face animation on player.
    Original: [stopFaceAni](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/stopFaceAni/)
    
    ## Declaration
    ```python
    async def stopFaceAni(id : int, aniName : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **aniName**: the name of the animation that you want to stop. The default value is \"\" which means that the first active ani will be stopped.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def unequipItem(id : int, instance : str):
    """
    !!! note
        If you want to unequip weapon/shield, first make sure that player is in `WEAPONMODE_NONE`.
    This function is used to unequip item from player for all players.
    Original: [unequipItem](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/unequipItem/)
    
    ## Declaration
    ```python
    async def unequipItem(id : int, instance : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **instance**: the item instance from Daedalus scripts.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def unreadySpell(id : int):
    """
    This function will cause player to unready active spell. It works almost the same as [removeWeapon](removeWeapon.md), but also stops hero if he's moving before hiding the active spell.
    Original: [unreadySpell](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/unreadySpell/)
    
    ## Declaration
    ```python
    async def unreadySpell(id : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def unspawnPlayer(id : int):
    """
    !!! note
        Unspawned players can't see other players, items, etc. and are invisible for others.
    This function will unspawn the player.
    Original: [unspawnPlayer](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/unspawnPlayer/)
    
    ## Declaration
    ```python
    async def unspawnPlayer(id : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def useItem(id : int, instance : str):
    """
    This function will try to use, interact, open item by player.
    Original: [useItem](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/useItem/)
    
    ## Declaration
    ```python
    async def useItem(id : int, instance : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **instance**: the item instance from Daedalus scripts.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def useItemToState(id : int, instance : str, state : int):
    """
    This function will try to use, interact, open item in specific state by player.
    Original: [useItemToState](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/useItemToState/)
    
    ## Declaration
    ```python
    async def useItemToState(id : int, instance : str, state : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **instance**: the item instance from Daedalus scripts.
    `int` **state**: the state that you'll start from interacting with item.
    """
    data = f'return {get_call_repr()}'

    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result
