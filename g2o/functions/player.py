import sqg2o

def addBan(info : dict) -> bool:
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
    def addBan(info : dict) -> bool
    ```
    ## Parameters
    `dict {serial, mac, ip, name, reason, timestamp, meta={..}}` **info**: the ban properties.
    `int` **host_id**: the player host identifier.
    ## Returns
    `bool`: `true` if ban was added, otherwise `false`.
    """
    return sqg2o.addBan(info)

def applyPlayerOverlay(id : int, overlayId : int) -> bool:
    """
    This function will apply animation overlay on player for all players.
    Original: [applyPlayerOverlay](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/applyPlayerOverlay/)
    
    ## Declaration
    ```python
    def applyPlayerOverlay(id : int, overlayId : int) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **overlayId**: the overlay id from `mds.xml` file, e.g: `Mds.id("HUMANS_MILITIA.MDS")`
    ## Returns
    `bool`: `true` if animation overlay was successfully applied on player, otherwise `false`.
    """
    return sqg2o.applyPlayerOverlay(id, overlayId)

def ban(id : int, minutes : int, reason : str):
    """
    !!! note
        The reason string can't be longer than 255 characters.
    This function will ban the player on the server.
    Original: [ban](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/ban/)
    
    ## Declaration
    ```python
    def ban(id : int, minutes : int, reason : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **minutes**: the time how long ban will take in minutes. Passing `0` will cause the player to have permanent ban.
    `str` **reason**: the reason why player was banned.
    """
    return sqg2o.ban(id, minutes, reason)

def drawWeapon(id : int, weaponMode : int):
    """
    This function will cause player to draw a weapon. If hero/npc doesn't have equipped weapon assosiated with the preffered weapon mode, then it will try to draw melee weapon, otherwise `WEAPONMODE_FIST` will be used instead.
    Original: [drawWeapon](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/drawWeapon/)
    
    ## Declaration
    ```python
    def drawWeapon(id : int, weaponMode : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **weaponMode**: the preffered weapon mode. For more information see [Weapon mode constants](../../constants/weapon-mode.md).
    """
    return sqg2o.drawWeapon(id, weaponMode)


def equipItem(id : int, instance : str, slotId : int = -1):
    """
    !!! note
        If you want to equip weapon/shield, first make sure that player is in `WEAPONMODE_NONE`.
    This function is used to equip item on player for all players.
    Original: [equipItem](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/equipItem/)
    
    ## Declaration
    ```python
    def equipItem(id : int, instance : str, slotId : int = -1)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **instance**: the item instance from Daedalus scripts.
    `int` **slotId**: the slot id in which you want to equip item on player, e.g scrolls, runes, rings, by default the item will be equipped on the first free slot.
    """
    return sqg2o.equipItem(id, instance, slotId)

def getPlayerAmulet(id : int) -> str:
    """
    This function will get the equipped player amulet.
    Original: [getPlayerAmulet](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerAmulet/)
    
    ## Declaration
    ```python
    getPlayerAmulet(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    return sqg2o.getPlayerAmulet(id)

def getPlayerAngle(id : int) -> float:
    """
    This function will get the player facing rotation on y axis.
    Original: [getPlayerAngle](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerAngle/)
    
    ## Declaration
    ```python
    def getPlayerAngle(id : int) -> float
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `float`: the facing rotation on y axis.
    """
    return sqg2o.getPlayerAngle(id)

def getPlayerAni(id : int) -> str:
    """
    This function will get the player facing rotation on y axis.
    Original: [getPlayerAni](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerAni/)
    
    ## Declaration
    ```python
    def getPlayerAni(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the ani name, e.g: `"S_RUN"`.
    """
    return sqg2o.getPlayerAni(id)

def getPlayerArmor(id : int) -> str:
    """
    This function will get the equipped player armor.
    Original: [getPlayerArmor](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerArmor/)
    
    ## Declaration
    ```python
    def getPlayerArmor(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    return sqg2o.getPlayerArmor(id)

def getPlayerAtVector(id : int) -> dict:
    """
    This function will get player at vector.
    Original: [getPlayerAtVector](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerAtVector/)
    
    ## Declaration
    ```python
    getPlayerAtVector(id : int) -> dict
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `dict {x, y, z}`: the player at vector.
    """
    return sqg2o.getPlayerAtVector(id)

def getPlayerBelt(id : int) -> str:
    """
    This function will get the equipped player belt.
    Original: [getPlayerBelt](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerBelt/)
    
    ## Declaration
    ```python
    def getPlayerBelt(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    return sqg2o.getPlayerBelt(id)

def getPlayerCameraPosition(id : int) -> dict:
    """
    This function will get the player camera position in world.
    Original: [getPlayerCameraPosition](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerCameraPosition/)
    
    ## Declaration
    ```python
    getPlayerCameraPosition(id : int) -> dict
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `dict {x, y, z}`: the dictionary that represents camera position.
    """
    return sqg2o.getPlayerCameraPosition(id)

def getPlayerCollision(id : int) -> bool:
    """
    This function will get the player collision.
    Original: [getPlayerCollision](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerCollision/)
    
    ## Declaration
    ```python
    def getPlayerCollision(id : int) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `bool`: `true` if collision is enabled, otherwise `false`.
    """
    return sqg2o.getPlayerCollision(id)

def getPlayerColor(id : int) -> dict:
    """
    This function will get the player nickname color.
    Original: [getPlayerColor](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerColor/)
    
    ## Declaration
    ```python
    def getPlayerColor(id : int) -> dict
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `dict {r, g, b}`: the player nickname color.
    """
    return sqg2o.getPlayerColor(id)

def getPlayerContext(id : int, type : int) -> int:
    """
    This function is used to get player script context. For more information see [this article](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/multiplayer/script-context/).
    Original: [getPlayerContext](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerContext/)
    
    ## Declaration
    ```python
    def getPlayerContext(id : int, type : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the value stored within selected context.
    """
    return sqg2o.getPlayerContext(id, type)

def getPlayerDexterity(id : int) -> int:
    """
    This function will get the player dexterity points.
    Original: [getPlayerDexterity](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerDexterity/)
    
    ## Declaration
    ```python
    def getPlayerDexterity(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the dexterity points amount.
    """
    return sqg2o.getPlayerDexterity(id)

def getPlayerFaceAnis(id : int) -> list:
    """
    This function will get the player dexterity points.
    Original: [getPlayerFaceAnis](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerFaceAnis/)
    
    ## Declaration
    ```python
    def getPlayerFaceAnis(id : int) -> list
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `list [{aniName, layer}]`: the list of objects describing face animation.
    """
    return sqg2o.getPlayerFaceAnis(id)

def getPlayerFatness(id : int) -> float:
    """
    This function will get the player fatness factor.
    Original: [getPlayerFatness](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerFatness/)
    
    ## Declaration
    ```python
    def getPlayerFatness(id : int) -> float
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `float`: the fatness ratio.
    """
    return sqg2o.getPlayerFatness(id)

def getPlayerFocus(id : int) -> int:
    """
    This function is used to get current focused player by other player.
    Original: [getPlayerFocus](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerFocus/)
    
    ## Declaration
    ```python
    def getPlayerFocus(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the current focused player id. In case were there is no focus returns `-1`.
    """
    return sqg2o.getPlayerFocus(id)

def getPlayerHealth(id : int) -> int:
    """
    This function will get the player health points.
    Original: [getPlayerHealth](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerHealth/)
    
    ## Declaration
    ```python
    def getPlayerHealth(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the health points amount.
    """
    return sqg2o.getPlayerHealth(id)

def getPlayerHelmet(id : int) -> str:
    """
    This function will get the equipped player helmet.
    Original: [getPlayerHelmet](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerHelmet/)
    
    ## Declaration
    ```python
    def getPlayerHelmet(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    return sqg2o.getPlayerHelmet(id)

def getPlayerIP(id : int) -> str:
    """
    This function will get the player ipv4 ip address.
    Original: [getPlayerIP](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerIP/)
    
    ## Declaration
    ```python
    def getPlayerIP(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the player ip address, e.g `"127.0.0.1"`.
    """
    return sqg2o.getPlayerIP(id)

def getPlayerInstance(id : int) -> str:
    """
    This function will get the player instance.
    Original: [getPlayerInstance](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerInstance/)
    
    ## Declaration
    ```python
    def getPlayerInstance(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the player instance.
    """
    return sqg2o.getPlayerInstance(id)

def getPlayerInvisible(id : int) -> bool:
    """
    This function will get the player invisiblity for all players.
    Original: [getPlayerInvisible](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerInvisible/)
    
    ## Declaration
    ```python
    def getPlayerInvisible(id : int) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `bool`: `true` when player is invisible for all players, otherwise `false`.
    """
    return sqg2o.getPlayerInvisible(id)

def getPlayerMacAddr(id : int) -> str:
    """
    !!! note
        The function can return null if player isn't connected.
    This function will get the player MAC address.
    MAC is used to uniquely idientify each player,
    however it can be changed/spoofed by more advance users.
    Original: [getPlayerMacAddr](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerMacAddr/)
    
    ## Declaration
    ```python
    def getPlayerMacAddr(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the player mac address, e.g `"00-1b-44-11-3a-b7"`.
    """
    return sqg2o.getPlayerMacAddr(id)

def getPlayerMana(id : int) -> int:
    """
    This function will get the player mana points.
    Original: [getPlayerMana](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerMana/)
    
    ## Declaration
    ```python
    def getPlayerMana(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the mana points amount.
    """
    return sqg2o.getPlayerMana(id)

def getPlayerMaxHealth(id : int) -> int:
    """
    This function will get the player max health points.
    Original: [getPlayerMaxHealth](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerMaxHealth/)
    
    ## Declaration
    ```python
    def getPlayerMaxHealth(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the max health points amount.
    """
    return sqg2o.getPlayerMaxHealth(id)

def getPlayerMaxMana(id : int) -> int:
    """
    This function will get the player max mana points.
    Original: [getPlayerMaxMana](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerMaxMana/)
    
    ## Declaration
    ```python
    def getPlayerMaxMana(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the max mana points amount.
    """
    return sqg2o.getPlayerMaxMana(id)

def getPlayerMeleeWeapon(id : int) -> str:
    """
    This function will get the equipped player melee weapon.
    Original: [getPlayerMeleeWeapon](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerMeleeWeapon/)
    
    ## Declaration
    ```python
    def getPlayerMeleeWeapon(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    return sqg2o.getPlayerMeleeWeapon(id)

def getPlayerName(id : int) -> str:
    """
    This function will get the player nickname.
    Original: [getPlayerName](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerName/)
    
    ## Declaration
    ```python
    def getPlayerName(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the player nickname.
    """
    return sqg2o.getPlayerName(id)

def getPlayerPing(id : int) -> int:
    """
    !!! note
        The function can return `-1` if player isn't connected.
    This function will get the player ping. Ping gets updated after each 2500 miliseconds.
    Original: [getPlayerPing](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerPing/)
    
    ## Declaration
    ```python
    def getPlayerPing(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the current player ping.
    """
    return sqg2o.getPlayerPing(id)

def getPlayerPosition(id : int) -> dict:
    """
    This function will get the player world position.
    Original: [getPlayerPosition](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerPosition/)
    
    ## Declaration
    ```python
    def getPlayerPosition(id : int) -> dict
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `dict {x, y, z}`: the player world position.
    """
    return sqg2o.getPlayerPosition(id)

def getPlayerRangedWeapon(id : int) -> str:
    """
    This function will get the equipped player ranged weapon.
    Original: [getPlayerRangedWeapon](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerRangedWeapon/)
    
    ## Declaration
    ```python
    def getPlayerRangedWeapon(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    return sqg2o.getPlayerRangedWeapon(id)

def getPlayerRespawnTime(id : int) -> int:
    """
    This function will get the player time to respawn after death.
    Original: [getPlayerRespawnTime](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerRespawnTime/)
    
    ## Declaration
    ```python
    def getPlayerRespawnTime(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the player respawn time.
    """
    return sqg2o.getPlayerRespawnTime(id)

def getPlayerRing(id : int, handId : int) -> str:
    """
    This function will get the equipped player ring.
    Original: [getPlayerRing](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerRing/)
    
    ## Declaration
    ```python
    ddef getPlayerRing(id : int, handId : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **handId**: the handId. For more information see [Hand constants](../../constants/hand.md).
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    return sqg2o.getPlayerRing(id, handId)

def getPlayerScale(id : int) -> dict:
    """
    This function will get the player scale.
    Original: [getPlayerScale](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerScale/)
    
    ## Declaration
    ```python
    def getPlayerScale(id : int) -> dict
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `dict {x, y, z}`: the player scale.
    """
    return sqg2o.getPlayerScale(id)

def getPlayerSerial(id : int) -> str:
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
    def getPlayerSerial(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the player serial.
    """
    return sqg2o.getPlayerSerial(id)

def getPlayerShield(id : int) -> str:
    """
    This function will get the equipped player shield.
    Original: [getPlayerShield](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerShield/)
    
    ## Declaration
    ```python
    def getPlayerShield(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    return sqg2o.getPlayerShield(id)

def getPlayerSkillWeapon(id : int, skillId : int) -> int:
    """
    This function will get the player skill weapon.
    Original: [getPlayerSkillWeapon](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerSkillWeapon/)
    
    ## Declaration
    ```python
    def getPlayerSkillWeapon(id : int, skillId : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **skillId**: For more information see [Skill weapon constants](../../constants/skill-weapon.md).
    ## Returns
    `int`: the percentage value in range <0, 100>.
    """
    return sqg2o.getPlayerSkillWeapon(id, skillId)

def getPlayerSpell(id : int, slotId : int) -> str:
    """
    This function will get the equipped player spell.
    Original: [getPlayerSpell](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerSpell/)
    
    ## Declaration
    ```python
    ddef getPlayerSpell(id : int, slotId : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **slotId**: the equipped slotId in range <0, 6>.
    ## Returns
    `str`: the item instance from Daedalus scripts.
    """
    return sqg2o.getPlayerSpell(id, slotId)

def getPlayerStrength(id : int) -> int:
    """
    This function will get the player strength points.
    Original: [getPlayerStrength](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerStrength/)
    
    ## Declaration
    ```python
    def getPlayerStrength(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the strength points amount.
    """
    return sqg2o.getPlayerStrength(id)

def getPlayerTalent(id : int, talentId : int) -> int:
    """
    This function will get the player talent.
    Original: [getPlayerTalent](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerTalent/)
    
    ## Declaration
    ```python
    def getPlayerTalent(id : int, talentId : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **talentId**: the talent id. For more information see [Talent constants](../../constants/talent.md).
    ## Returns
    `int`: the current talent value for specific talent id.
    """
    return sqg2o.getPlayerTalent(id, talentId)

def getPlayerVirtualWorld(id : int) -> int:
    """
    This function will get the player virtual world.
    Original: [getPlayerVirtualWorld](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerVirtualWorld/)
    
    ## Declaration
    ```python
    def getPlayerVirtualWorld(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the player virtual world id.
    """
    return sqg2o.getPlayerVirtualWorld(id)

def getPlayerVisual(id : int) -> dict:
    """
    This function will get the player visual.
    Original: [getPlayerVisual](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerVisual/)
    
    ## Declaration
    ```python
    def getPlayerVisual(id : int) -> dict
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `dict {bodyModel, bodyTxt, headModel, headTxt}`: player visual.
    """
    return sqg2o.getPlayerVisual(id)

def getPlayerWeaponMode(id : int) -> int:
    """
    This function will get the player weapon mode.
    Original: [getPlayerWeaponMode](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerWeaponMode/)
    
    ## Declaration
    ```python
    def getPlayerWeaponMode(id : int) -> int
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `int`: the player weaponMode, for more information see [Weapon mode constants](../../constants/weapon-mode.md).
    """
    return sqg2o.getPlayerWeaponMode(id)

def getPlayerWorld(id : int) -> str:
    """
    This function will get the player world.
    Original: [getPlayerWorld](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/getPlayerWorld/)
    
    ## Declaration
    ```python
    def getPlayerWorld(id : int) -> str
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `str`: the player world.
    """
    return sqg2o.getPlayerWorld(id)

def giveItem(id : int, instance : str, amount : int):
    """
    This function is used to give item for player.
    Original: [giveItem](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/giveItem/)
    
    ## Declaration
    ```python
    def giveItem(id : int, instance : str, amount : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **instance**: the item instance from Daedalus scripts.
    `int` **amount**: the amount of item, e.g: `1000` gold coins.
    """
    return sqg2o.giveItem(id, instance, amount)

def hitPlayer(id : int, target_id : int) -> bool:
    """
    This function is used to simulate hit between attacker and victim. It will only work with if killer or victim is a real player. The victim will receive damage calculated damage by the game.
    Original: [hitPlayer](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/hitPlayer/)
    
    ## Declaration
    ```python
    def hitPlayer(id : int, target_id : int) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **target_id**: the victim id.
    ## Returns
    `bool`: `true` if hit was successfully simulated, otherwise `false`.
    """
    return sqg2o.hitPlayer(id, target_id)

def isPlayerConnected(id : int) -> bool:
    """
    The function is used to check whether player is connected to the server.
    Original: [isPlayerConnected](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/isPlayerConnected/)
    
    ## Declaration
    ```python
    def isPlayerConnected(id : int) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `bool`: `true` when player is connected, otherwise `false`.
    """
    return sqg2o.isPlayerConnected(id)

def isPlayerDead(id : int) -> bool:
    """
    The function is used to check whether player is dead.
    Original: [isPlayerDead](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/isPlayerDead/)
    
    ## Declaration
    ```python
    def isPlayerDead(id : int) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `bool`: `true` when player is dead, otherwise `false`.
    """
    return sqg2o.isPlayerDead(id)

def isPlayerSpawned(id : int) -> bool:
    """
    The function is used to check whether player is spawned.
    Original: [isPlayerSpawned](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/isPlayerSpawned/)
    
    ## Declaration
    ```python
    def isPlayerSpawned(id : int) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `bool`: `true` when player is spawned, otherwise `false`.
    """
    return sqg2o.isPlayerSpawned(id)

def isPlayerUnconscious(id : int) -> bool:
    """
    The function is used to check whether player is in unconscious state. The player will be unconscious, when it gets beaten up, but not killed.
    Original: [isPlayerUnconscious](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/isPlayerUnconscious/)
    
    ## Declaration
    ```python
    def isPlayerUnconscious(id : int) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    ## Returns
    `bool`: `true` when player is unconscious, otherwise `false`.
    """
    return sqg2o.isPlayerUnconscious(id)

def kick(id : int, reason : str):
    """
    !!! note
        The reason string can't be longer than 255 characters.
    This function will kick the player from the server.
    Original: [kick](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/kick/)
    
    ## Declaration
    ```python
    def kick(id : int, reason : str)
    ```
    ## Parameters
    `int` **id**: the reason why player was kicked.
    `str` **reason**: the reason why player was kicked.
    """
    return sqg2o.kick(id, reason)

def playAni(id : int, aniName : str):
    """
    This function is used to play animation on player for all players.
    Original: [playAni](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/playAni/)
    
    ## Declaration
    ```python
    def playAni(id : int, aniName : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **aniName**: the name of the animation, e.g: `"T_STAND_2_SIT"`.
    """
    return sqg2o.playAni(id, aniName)

def playFaceAni(id : int, aniName : str):
    """
    This function is used to play face animation on player.
    Original: [playFaceAni](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/playFaceAni/)
    
    ## Declaration
    ```python
    def playFaceAni(id : int, aniName : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **aniName**: the name of the animation, e.g: `"S_FRIENDLY"`.
    """
    return sqg2o.playFaceAni(id, aniName)

def readySpell(id : int, slotId : int, manaInvested : int):
    """
    This function will cause player to ready equipped spell.
    Original: [readySpell](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/readySpell/)
    
    ## Declaration
    ```python
    def readySpell(id : int, slotId : int, manaInvested : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **slotId**: the equipped spell slotId in range <0, 6>.
    `int` **manaInvested**: the spell cast cost in mana points.
    """
    return sqg2o.readySpell(id, slotId, manaInvested)

def removeItem(id : int, instance : str, amount : int):
    """
    This function is used to remove item from player.
    Original: [removeItem](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/removeItem/)
    
    ## Declaration
    ```python
    def removeItem(id : int, instance : str, amount : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **instance**: the item instance from Daedalus scripts.
    `int` **amount**: the amount of item, e.g: `1000` gold coins.
    """
    return sqg2o.removeItem(id, instance, amount)

def removePlayerOverlay(id : int, overlayId : int) -> bool:
    """
    This function will remove animation overlay from player for all players.
    Original: [removePlayerOverlay](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/removePlayerOverlay/)
    
    ## Declaration
    ```python
    def removePlayerOverlay(id : int, overlayId : int) -> bool
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **overlayId**: the overlay id from `mds.xml` file, e.g: `Mds.id("HUMANS_MILITIA.MDS")`
    ## Returns
    `bool`: `true` if animation overlay was successfully removed from player, otherwise `false`.
    """
    return sqg2o.removePlayerOverlay(id, overlayId)

def removeWeapon(id : int):
    """
    This function will cause player to hide a weapon.
    Original: [removeWeapon](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/removeWeapon/)
    
    ## Declaration
    ```python
    def removeWeapon(id : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    """
    return sqg2o.removeWeapon(id)

def setPlayerAngle(id : int, angle : float):
    """
    This function will set the player facing rotation on y axis for all players.
    Original: [setPlayerAngle](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerAngle/)
    
    ## Declaration
    ```python
    def setPlayerAngle(id : int, angle : float)
    ```
    ## Parameters
    `int` **id**: the player id.
    `float` **angle**: the facing rotation on y axis.
    """
    return sqg2o.setPlayerAngle(id, angle)

def setPlayerCollision(id : int, collision : bool):
    """
    This function will set the player collision.
    Original: [setPlayerCollision](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerCollision/)
    
    ## Declaration
    ```python
    def setPlayerCollision(id : int, collision : bool)
    ```
    ## Parameters
    `int` **id**: the player id.
    `bool` **collision**: `true` if want to enable collision, otherwise `false`.
    """
    return sqg2o.setPlayerCollision(id, collision)

def setPlayerColor(id : int, r : int, g : int, b : int):
    """
    This function will set the player nickname color for all players.
    Original: [setPlayerColor](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerColor/)
    
    ## Declaration
    ```python
    def setPlayerColor(id : int, r : int, g : int, b : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **r**: the red color component in RGB model.
    `int` **g**: the green color component in RGB model.
    `int` **b**: the blue color component in RGB model.
    """
    return sqg2o.setPlayerColor(id, r, g, b)

def setPlayerContext(id : int, type : int, value : int):
    """
    This function is used to set player script context. For more information see [this article](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/multiplayer/script-context/).
    Original: [setPlayerContext](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerContext/)
    
    ## Declaration
    ```python
    def setPlayerContext(id : int, type : int, value : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **type**: the type of modified context.
    `int` **value**: the new value written into context.
    """
    return sqg2o.setPlayerContext(id, type, value)

def setPlayerDexterity(id : int, dexterity : int):
    """
    This function will set the player dexterity points for all players.
    Original: [setPlayerDexterity](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerDexterity/)
    
    ## Declaration
    ```python
    def setPlayerDexterity(id : int, dexterity : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **dexterity**: the dexterity points amount.
    """
    return sqg2o.setPlayerDexterity(id, dexterity)

def setPlayerFatness(id : int, fatness : float):
    """
    This function will set the player fatness factor for all players.
    Original: [setPlayerFatness](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerFatness/)
    
    ## Declaration
    ```python
    def setPlayerFatness(id : int, fatness : float)
    ```
    ## Parameters
    `int` **id**: the player id.
    `float` **fatness**: ratio of how much you want to make player fatter, `0.0` is default fatness (none).
    """
    return sqg2o.setPlayerFatness(id, fatness)

def setPlayerHealth(id : int, health : int):
    """
    This function will set the player health points for all players.
    Original: [setPlayerHealth](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerHealth/)
    
    ## Declaration
    ```python
    def setPlayerHealth(id : int, health : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **health**: health points amount.
    """
    return sqg2o.setPlayerHealth(id, health)

def setPlayerInstance(id : int, instance : str):
    """
    This function will set the player instance for all players. Instance describes the player attributes, like visual, stats, and more.. You can find more information about npc instances in daedalus scripts.
    Original: [setPlayerInstance](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerInstance/)
    
    ## Declaration
    ```python
    def setPlayerInstance(id : int, instance : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **instance**: the new player instance.
    """
    return sqg2o.setPlayerInstance(id, instance)

def setPlayerInvisible(id : int, toggle : bool):
    """
    This function will toggle the player invisiblity for all players.
    The invisible player will still see other visible players.
    Original: [setPlayerInvisible](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerInvisible/)
    
    ## Declaration
    ```python
    def setPlayerInvisible(id : int, toggle : bool)
    ```
    ## Parameters
    `int` **id**: the player id.
    `bool` **toggle**: `true` if the player should be invisible for all players, otherwise `false`.
    """
    return sqg2o.setPlayerInvisible(id, toggle)

def setPlayerMana(id : int, mana : int):
    """
    This function will set the player mana points for all players.
    Original: [setPlayerMana](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerMana/)
    
    ## Declaration
    ```python
    def setPlayerMana(id : int, Mana : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **mana**: mana points amount.
    """
    return sqg2o.setPlayerMana(id, mana)

def setPlayerMaxHealth(id : int, maxHealth : int):
    """
    This function will set the player max health points for all players.
    Original: [setPlayerMaxHealth](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerMaxHealth/)
    
    ## Declaration
    ```python
    def setPlayerMaxHealth(id : int, maxHealth : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **maxHealth**: max health points amount.
    """
    return sqg2o.setPlayerMaxHealth(id, maxHealth)

def setPlayerMaxMana(id : int, maxMana : int):
    """
    This function will set the player max mana points for all players.
    Original: [setPlayerMaxMana](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerMaxMana/)
    
    ## Declaration
    ```python
    def setPlayerMaxMana(id : int, maxMana : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **maxMana**: max mana points amount.
    """
    return sqg2o.setPlayerMaxMana(id, maxMana)

def setPlayerName(id : int, name : str) -> bool:
    """
    !!! note
        The name string can't be longer than 18 characters, and must be unique for each player.
    This function will set the player unique nickname for all players.
    Original: [setPlayerName](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerName/)
    
    ## Declaration
    ```python
    def setPlayerName(id : int, name : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **instance**: the new unique player name.
    ## Returns
    `bool`: `true` when unique player name was set, otherwise `false`.
    """
    return sqg2o.setPlayerName(id, name)

def setPlayerPosition(id : int, x : float, y : float, z : float):
    """
    This function will set the player world position for all players.
    Original: [setPlayerPosition](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerPosition/)
    
    ## Declaration
    ```python
    def setPlayerPosition(id : int, x : float, y : float, z : float)
    ```
    ## Parameters
    `int` **id**: the player id.
    `float` **x**: the position in the world on the x axis.
    `float` **y**: the position in the world on the y axis.
    `float` **z**: the position in the world on the z axis.
    """
    return sqg2o.setPlayerPosition(id, x, y, z)

def setPlayerRespawnTime(id : int, respawnTime : int):
    """
    !!! note
        The respawnTime can't be smaller than 1001 miliseconds.
    This function will set the player time to respawn after death. If set to 0, respawn is disabled for selected player.
    Original: [setPlayerRespawnTime](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerRespawnTime/)
    
    ## Declaration
    ```python
    def setPlayerRespawnTime(id : int, respawnTime : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **respawnTime**: the new respawn time in miliseconds.
    """
    return sqg2o.setPlayerRespawnTime(id, respawnTime)

def setPlayerScale(id : int, x : float, y : float, z : float):
    """
    This function will set the player scale for all players.
    Original: [setPlayerScale](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerScale/)
    
    ## Declaration
    ```python
    def setPlayerScale(id : int, x : float, y : float, z : float)
    ```
    ## Parameters
    `int` **id**: the player id.
    `float` **x**: the scale factor on x axis.
    `float` **y**: the scale factor on y axis.
    `float` **z**: the scale factor on z axis.
    """
    return sqg2o.setPlayerScale(id, x, y, z)

def setPlayerSkillWeapon(id : int, skillId : int, percentage : int):
    """
    This function will set the player skill weapon for all players.
    Original: [setPlayerSkillWeapon](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerSkillWeapon/)
    
    ## Declaration
    ```python
    def setPlayerSkillWeapon(id : int, skillId : int, percentage : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **skillId**: For more information see [Skill weapon constants](../../constants/skill-weapon.md).
    `int` **percentage**: the percentage in range <0, 100>.
    """
    return sqg2o.setPlayerSkillWeapon(id, skillId, percentage)

def setPlayerStrength(id : int, strength : int):
    """
    This function will set the player strength points for all players.
    Original: [setPlayerStrength](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerStrength/)
    
    ## Declaration
    ```python
    def setPlayerStrength(id : int, strength : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **strength**: strength points amount.
    """
    return sqg2o.setPlayerStrength(id, strength)

def setPlayerTalent(id : int, talentId : int, talentValue : int):
    """
    This function will toggle the player talent for all players.
    Original: [setPlayerTalent](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerTalent/)
    
    ## Declaration
    ```python
    def setPlayerTalent(id : int, talentId : int, talentValue : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **talentId**: the talent id. For more information see [Talent constants](../../constants/talent.md).
    `int` **talentValue**: the new talent value.
    """
    return sqg2o.setPlayerTalent(id, talentId, talentValue)

def setPlayerVirtualWorld(id : int, virtualWorld : int):
    """
    This function will set the player virtual world for all players.
    Virtual worlds are separate logical worlds on the same physical world.
    Original: [setPlayerVirtualWorld](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerVirtualWorld/)
    
    ## Declaration
    ```python
    def setPlayerVirtualWorld(id : int, virtualWorld : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **virtualWorld**: the virtual world id in range <0, 65535>.
    """
    return sqg2o.setPlayerVirtualWorld(id, virtualWorld)

def setPlayerVisual(id : int, bodyModel : str, bodyTxt : int, headModel : str, headTxt : int):
    """
    This function will set the player visual for all players.
    Original: [setPlayerVisual](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerVisual/)
    
    ## Declaration
    ```python
    def setPlayerVisual(id : int, bodyModel : str, bodyTxt : int, headModel : str, headTxt : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **bodyModel**: the name of the body model (ASC), e.g: `HUM_BODY_NAKED0`.
    `int` **bodyTxt**: the numeric id of body texture file. Texture id can be read from V(number) filename part, for example, in this file: `HUM_BODY_NAKED_V8_C0-C.TEX` id is 8.
    `str` **headModel**: the name of the head model (MMS), e.g: `HUM_HEAD_PONY`.
    `int` **headTxt**: the numeric id of head texture file. Texture id can be read from V(number) filename part, for example, in this file: `HUM_HEAD_V18_C0-C.TEX` id is 18.
    """
    return sqg2o.setPlayerVisual(id, bodyModel, bodyTxt, headModel, headTxt)

def setPlayerWeaponMode(id : int, weaponMode : int):
    """
    This function will set the player weapon mode for all players.
    Original: [setPlayerWeaponMode](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerWeaponMode/)
    
    ## Declaration
    ```python
    def setPlayerWeaponMode(id : int, weaponMode : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `int` **weaponMode**: For more information see [Weapon mode constants](../../constants/weapon-mode.md).
    """
    return sqg2o.setPlayerWeaponMode(id, weaponMode)

def setPlayerWorld(id : int, world : str, startPointName : str = ""):
    """
    This function will set the player world for all players.
    Original: [setPlayerWorld](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/setPlayerWorld/)
    
    ## Declaration
    ```python
    def setPlayerWorld(id : int, world : str, startPointName : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **world**: the path to the target world (.ZEN). World path is relative to directory `_Work/Data/Worlds`.
    `str` **startPointName**: the name of the vob to which the player will be moved. If passed empty string, player will be placed at world start point. If vob with specified name doesn't exists or world doesn't have start point, player will be placed at {0, 150, 0} coordinates.
    """
    return sqg2o.setPlayerWorld(id, world, startPointName)

def spawnPlayer(id : int):
    """
    !!! note
        Unspawned players can't see other players, items, etc. and are invisible for others.
    This function will spawn the player.
    Players are always in unspawned state after joining to server or after respawning.
    Original: [spawnPlayer](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/spawnPlayer/)
    
    ## Declaration
    ```python
    def spawnPlayer(id : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    """
    return sqg2o.spawnPlayer(id)

def stopAni(id : int, aniName : str = ""):
    """
    This function is used to stop played animation on player for all players.
    Original: [stopAni](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/stopAni/)
    
    ## Declaration
    ```python
    def stopAni(id : int, aniName : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **aniName**: the name of the animation that you want to stop. The default value is \"\" which means that the first active ani will be stopped.
    """
    return sqg2o.stopAni(id, aniName)

def stopFaceAni(id : int, aniName : str = ""):
    """
    This function is used to stop played face animation on player.
    Original: [stopFaceAni](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/stopFaceAni/)
    
    ## Declaration
    ```python
    def stopFaceAni(id : int, aniName : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **aniName**: the name of the animation that you want to stop. The default value is \"\" which means that the first active ani will be stopped.
    """
    return sqg2o.stopFaceAni(id, aniName)

def unequipItem(id : int, instance : str):
    """
    !!! note
        If you want to unequip weapon/shield, first make sure that player is in `WEAPONMODE_NONE`.
    This function is used to unequip item from player for all players.
    Original: [unequipItem](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/unequipItem/)
    
    ## Declaration
    ```python
    def unequipItem(id : int, instance : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **instance**: the item instance from Daedalus scripts.
    """
    return sqg2o.unequipItem(id, instance)

def unreadySpell(id : int):
    """
    This function will cause player to unready active spell. It works almost the same as [removeWeapon](removeWeapon.md), but also stops hero if he's moving before hiding the active spell.
    Original: [unreadySpell](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/unreadySpell/)
    
    ## Declaration
    ```python
    def unreadySpell(id : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    """
    return sqg2o.unreadySpell(id)

def unspawnPlayer(id : int):
    """
    !!! note
        Unspawned players can't see other players, items, etc. and are invisible for others.
    This function will unspawn the player.
    Original: [unspawnPlayer](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/unspawnPlayer/)
    
    ## Declaration
    ```python
    def unspawnPlayer(id : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    """
    return sqg2o.unspawnPlayer(id)

def useItem(id : int, instance : str):
    """
    This function will try to use, interact, open item by player.
    Original: [useItem](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/useItem/)
    
    ## Declaration
    ```python
    def useItem(id : int, instance : str)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **instance**: the item instance from Daedalus scripts.
    """
    return sqg2o.useItem(id, instance)

def useItemToState(id : int, instance : str, state : int):
    """
    This function will try to use, interact, open item in specific state by player.
    Original: [useItemToState](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/player/useItemToState/)
    
    ## Declaration
    ```python
    def useItemToState(id : int, instance : str, state : int)
    ```
    ## Parameters
    `int` **id**: the player id.
    `str` **instance**: the item instance from Daedalus scripts.
    `int` **state**: the state that you'll start from interacting with item.
    """
    return sqg2o.useItemToState(id, instance, state)