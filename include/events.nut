
addEventHandler("onPlayerUseCheat", function(playerid, type)
{
    local data = {
        event = "onPlayerUseCheat",
        playerid = playerid,
        type = type
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onBan", function(banInfo)
{
    local data = {
        event = "onBan",
        ban = {
            mac = "mac" in banInfo ? banInfo["mac"] : "-1",
            ip = "ip" in banInfo ? banInfo["ip"] : "-1",
            serial = "serial" in banInfo ? banInfo["serial"] : "-1",
            name = "name" in banInfo ? banInfo["name"] : "-1",
            timestamp = "timestamp" in banInfo ? banInfo["timestamp"] : -1
        }
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onExit", function()
{
    local data = {
        event = "onExit"
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onTick", function()
{
    local data = {
        event = "onTick"
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onTime", function(day, hour, min)
{
    local data = {
        event = "onTime",
        day = day,
        hour = hour,
        min = min
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onUnban", function(banInfo)
{
    local data = {
        event = "onUnban",
        ban = {
            mac = "mac" in banInfo ? banInfo["mac"] : "-1",
            ip = "ip" in banInfo ? banInfo["ip"] : "-1",
            serial = "serial" in banInfo ? banInfo["serial"] : "-1",
            name = "name" in banInfo ? banInfo["name"] : "-1",
            timestamp = "timestamp" in banInfo ? banInfo["timestamp"] : -1
        }
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onNpcActionFinished", function(npc_id, action_type, action_id, result)
{
    local data = {
        event = "onNpcActionFinished",
        npc_id = npc_id,
        action_type = action_type,
        action_id = action_id,
        result = result
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onNpcActionSent", function(npc_id, action_type, action_id)
{
    local data = {
        event = "onNpcActionSent",
        npc_id = npc_id,
        action_type = action_type,
        action_id = action_id,
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onNpcChangeHostPlayer", function(npc_id, current_id, previous_id)
{
    local data = {
        event = "onNpcChangeHostPlayer",
        npc_id = npc_id,
        current_id = current_id,
        previous_id = previous_id
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onNpcCreated", function(npc_id)
{
    local data = {
        event = "onNpcCreated",
        npc_id = npc_id
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onNpcDestroyed", function(npc_id)
{
    local data = {
        event = "onNpcCreated",
        npc_id = npc_id
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerChangeColor", function(playerid, r, g, b)
{
    local data = {
        event = "onPlayerChangeColor",
        playerid = playerid,
        r = r,
        g = g,
        b = b
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerChangeFocus", function(playerid, oldFocusId, newFocusId)
{
    local data = {
        event = "onPlayerChangeFocus",
        playerid = playerid,
        oldFocusId = oldFocusId,
        newFocusId = newFocusId
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerChangeHealth", function(playerid, previous, current)
{
    local data = {
        event = "onPlayerChangeHealth",
        playerid = playerid,
        previous = previous,
        current = current
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerChangeMana", function(playerid, previous, current)
{
    local data = {
        event = "onPlayerChangeMana",
        playerid = playerid,
        previous = previous,
        current = current
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerChangeMaxHealth", function(playerid, previous, current)
{
    local data = {
        event = "onPlayerChangeMaxHealth",
        playerid = playerid,
        previous = previous,
        current = current
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerChangeMaxMana", function(playerid, previous, current)
{
    local data = {
        event = "onPlayerChangeMaxMana",
        playerid = playerid,
        previous = previous,
        current = current
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerChangeWeaponMode", function(playerid, previous, current)
{
    local data = {
        event = "onPlayerChangeWeaponMode",
        playerid = playerid,
        previous = previous,
        current = current
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerChangeWorld", function(playerid, previous, current)
{
    local data = {
        event = "onPlayerChangeWorld",
        playerid = playerid,
        previous = previous,
        current = current
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerCommand", function(playerid, command, params)
{
    local data = {
        event = "onPlayerCommand",
        playerid = playerid,
        command = command,
        params = params
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerDamage", function(playerid, killerid, description)
{
    local data = {
        event = "onPlayerDamage",
        playerid = playerid,
        killerid = killerid,
        desc = {
            obj_name = "DamageDescription",
            obj_data = _globalInstance._serializeObject(description)
        }
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerDead", function(playerid, killerid)
{
    local data = {
        event = "onPlayerDead",
        playerid = playerid,
        killerid = killerid
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerDisconnect", function(playerid, reason)
{
    local data = {
        event = "onPlayerDisconnect",
        playerid = playerid,
        reason = reason
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerDropItem", function(playerid, itemGround)
{
    local data = {
        event = "onPlayerDropItem",
        playerid = playerid,
        itemGround = {
            obj_name = "ItemGround",
            obj_data = _globalInstance._serializeObject(itemGround)
        }
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerEnterWorld", function(playerid, world)
{
    local data = {
        event = "onPlayerEnterWorld",
        playerid = playerid,
        world = world
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerEquipAmulet", function(playerid, instance)
{
    local data = {
        event = "onPlayerEquipAmulet",
        playerid = playerid,
        instance = instance
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerEquipArmor", function(playerid, instance)
{
    local data = {
        event = "onPlayerEquipArmor",
        playerid = playerid,
        instance = instance
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerEquipBelt", function(playerid, instance)
{
    local data = {
        event = "onPlayerEquipBelt",
        playerid = playerid,
        instance = instance
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerEquipHandItem", function(playerid, hand, instance)
{
    local data = {
        event = "onPlayerEquipHandItem",
        playerid = playerid,
        hand = hand,
        instance = instance
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerEquipHelmet", function(playerid, instance)
{
    local data = {
        event = "onPlayerEquipHelmet",
        playerid = playerid,
        instance = instance
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerEquipMeleeWeapon", function(playerid, instance)
{
    local data = {
        event = "onPlayerEquipMeleeWeapon",
        playerid = playerid,
        instance = instance
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerEquipRangedWeapon", function(playerid, instance)
{
    local data = {
        event = "onPlayerEquipRangedWeapon",
        playerid = playerid,
        instance = instance
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerEquipRing", function(playerid, handId, instance)
{
    local data = {
        event = "onPlayerEquipRing",
        playerid = playerid,
        handId = handId,
        instance = instance
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerEquipShield", function(playerid, instance)
{
    local data = {
        event = "onPlayerEquipShield",
        playerid = playerid,
        instance = instance
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerEquipSpell", function(playerid, slotId, instance)
{
    local data = {
        event = "onPlayerEquipSpell",
        playerid = playerid,
        slotId = slotId,
        instance = instance
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerJoin", function(playerid)
{
    local data = {
        event = "onPlayerJoin",
        playerid = playerid
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerMessage", function(playerid, message)
{
    local data = {
        event = "onPlayerMessage",
        playerid = playerid,
        message = message
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerMobInteract", function(playerid, from, to)
{
    local data = {
        event = "onPlayerMobInteract",
        playerid = playerid,
        from = from,
        to = to
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerRespawn", function(playerid)
{
    local data = {
        event = "onPlayerRespawn",
        playerid = playerid
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerShoot", function(playerid, munition)
{
    local data = {
        event = "onPlayerShoot",
        playerid = playerid,
        munition = munition
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerSpellCast", function(playerid, instance, spellLevel)
{
    local data = {
        event = "onPlayerSpellCast",
        playerid = playerid,
        instance = instance,
        spellLevel = spellLevel
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerSpellSetup", function(playerid, instance)
{
    local data = {
        event = "onPlayerSpellSetup",
        playerid = playerid,
        instance = instance
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerTakeItem", function(playerid, itemGround)
{
    local data = {
        event = "onPlayerTakeItem",
        playerid = playerid,
        itemGround = {
            obj_name = "ItemGround",
            obj_data = _globalInstance._serializeObject(itemGround)
        }
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerTeleport", function(playerid, vobName)
{
    local data = {
        event = "onPlayerTeleport",
        playerid = playerid,
        vobName = vobName
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerToggleFaceAni", function(playerid, aniName, toggle)
{
    local data = {
        event = "onPlayerToggleFaceAni",
        playerid = playerid,
        aniName = aniName,
        toggle = toggle
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerSpawnForPlayer", function(playerid, spawnid)
{
    local data = {
        event = "onPlayerSpawnForPlayer",
        playerid = playerid,
        spawnid = spawnid
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerUnspawnForPlayer", function(playerid, spawnid)
{
    local data = {
        event = "onPlayerUnspawnForPlayer",
        playerid = playerid,
        spawnid = spawnid
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});

addEventHandler("onPlayerChangeChunk", function(playerid, chunk_index)
{
    local data = {
        event = "onPlayerChangeChunk",
        playerid = playerid,
        chunk_index = chunk_index
    }

    if (_globalInstance != -1)
        _globalInstance._send("event", data);
});
