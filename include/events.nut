
addEventHandler("onPlayerUseCheat", function(playerid, type)
{
    local data = {
        event = "onPlayerUseCheat",
        args = {
            playerid = playerid,
            type = type
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onBan", function(banInfo)
{
    local data = {
        event = "onBan",
        args = {
            ban = {
                mac = "mac" in banInfo ? banInfo["mac"] : "-1",
                ip = "ip" in banInfo ? banInfo["ip"] : "-1",
                serial = "serial" in banInfo ? banInfo["serial"] : "-1",
                name = "name" in banInfo ? banInfo["name"] : "-1",
                timestamp = "timestamp" in banInfo ? banInfo["timestamp"] : -1
            }
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onExit", function()
{
    local data = {
        event = "onExit",
        args = {}
    }

    _PyG2O_Send(data);
});

addEventHandler("onTick", function()
{
    local data = {
        event = "onTick",
        args = {}
    }

    _PyG2O_Send(data);
});

addEventHandler("onTime", function(day, hour, min)
{
    local data = {
        event = "onTime",
        args = {
            day = day,
            hour = hour,
            min = min,
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onUnban", function(banInfo)
{
    local data = {
        event = "onUnban",
        args = {
            ban = {
                mac = "mac" in banInfo ? banInfo["mac"] : "-1",
                ip = "ip" in banInfo ? banInfo["ip"] : "-1",
                serial = "serial" in banInfo ? banInfo["serial"] : "-1",
                name = "name" in banInfo ? banInfo["name"] : "-1",
                timestamp = "timestamp" in banInfo ? banInfo["timestamp"] : -1
            }
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onNpcActionFinished", function(npc_id, action_type, action_id, result)
{
    local data = {
        event = "onNpcActionFinished",
        args = {
            npc_id = npc_id,
            action_type = action_type,
            action_id = action_id,
            result = result
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onNpcActionSent", function(npc_id, action_type, action_id)
{
    local data = {
        event = "onNpcActionSent",
        args = {
            npc_id = npc_id,
            action_type = action_type,
            action_id = action_id,
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onNpcChangeHostPlayer", function(npc_id, current_id, previous_id)
{
    local data = {
        event = "onNpcChangeHostPlayer",
        args = {
            npc_id = npc_id,
            current_id = current_id,
            previous_id = previous_id
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onNpcCreated", function(npc_id)
{
    local data = {
        event = "onNpcCreated",
        args = {
            npc_id = npc_id
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onNpcDestroyed", function(npc_id)
{
    local data = {
        event = "onNpcDestroyed",
        args = {
            npc_id = npc_id
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerChangeColor", function(playerid, r, g, b)
{
    local data = {
        event = "onPlayerChangeColor",
        args = {
            playerid = playerid,
            r = r,
            g = g,
            b = b
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerChangeFocus", function(playerid, oldFocusId, newFocusId)
{
    local data = {
        event = "onPlayerChangeFocus",
        args = {
            playerid = playerid,
            oldFocusId = oldFocusId,
            newFocusId = newFocusId
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerChangeHealth", function(playerid, previous, current)
{
    local data = {
        event = "onPlayerChangeHealth",
        args = {
            playerid = playerid,
            previous = previous,
            current = current
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerChangeMana", function(playerid, previous, current)
{
    local data = {
        event = "onPlayerChangeMana",
        args = {
            playerid = playerid,
            previous = previous,
            current = current
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerChangeMaxHealth", function(playerid, previous, current)
{
    local data = {
        event = "onPlayerChangeMaxHealth",
        args = {
            playerid = playerid,
            previous = previous,
            current = current
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerChangeMaxMana", function(playerid, previous, current)
{
    local data = {
        event = "onPlayerChangeMaxMana",
        args = {
            playerid = playerid,
            previous = previous,
            current = current
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerChangeWeaponMode", function(playerid, previous, current)
{
    local data = {
        event = "onPlayerChangeWeaponMode",
        args = {
            playerid = playerid,
            previous = previous,
            current = current
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerChangeWorld", function(playerid, previous, current)
{
    local data = {
        event = "onPlayerChangeWorld",
        args = {
            playerid = playerid,
            previous = previous,
            current = current
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerCommand", function(playerid, command, params)
{
    local data = {
        event = "onPlayerCommand",
        args = {
            playerid = playerid,
            command = command,
            params = params
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerDamage", function(playerid, killerid, description)
{
    local data = {
        event = "onPlayerDamage",
        args = {
            playerid = playerid,
            killerid = killerid,
            obj_DamageDescription = {
                name = "desc",
                data = _PyG2O_Serialize(description)
            }
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerDead", function(playerid, killerid)
{
    local data = {
        event = "onPlayerDead",
        args = {
            playerid = playerid,
            killerid = killerid
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerDisconnect", function(playerid, reason)
{
    local data = {
        event = "onPlayerDisconnect",
        args = {
            playerid = playerid,
            reason = reason
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerDropItem", function(playerid, itemGround)
{
    local data = {
        event = "onPlayerDropItem",
        args = {
            playerid = playerid,
            obj_ItemGround = {
                name = "itemGround",
                data = _PyG2O_Serialize(itemGround)
            }
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerEnterWorld", function(playerid, world)
{
    local data = {
        event = "onPlayerEnterWorld",
        args = {
            playerid = playerid,
            world = world
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerEquipAmulet", function(playerid, instance)
{
    local data = {
        event = "onPlayerEquipAmulet",
        args = {
            playerid = playerid,
            instance = instance
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerEquipArmor", function(playerid, instance)
{
    local data = {
        event = "onPlayerEquipArmor",
        args = {
            playerid = playerid,
            instance = instance
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerEquipBelt", function(playerid, instance)
{
    local data = {
        event = "onPlayerEquipBelt",
        args = {
            playerid = playerid,
            instance = instance
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerEquipHandItem", function(playerid, hand, instance)
{
    local data = {
        event = "onPlayerEquipHandItem",
        args = {
            playerid = playerid,
            hand = hand,
            instance = instance
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerEquipHelmet", function(playerid, instance)
{
    local data = {
        event = "onPlayerEquipHelmet",
        args = {
            playerid = playerid,
            instance = instance
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerEquipMeleeWeapon", function(playerid, instance)
{
    local data = {
        event = "onPlayerEquipMeleeWeapon",
        args = {
            playerid = playerid,
            instance = instance
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerEquipRangedWeapon", function(playerid, instance)
{
    local data = {
        event = "onPlayerEquipRangedWeapon",
        args = {
            playerid = playerid,
            instance = instance
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerEquipRing", function(playerid, handId, instance)
{
    local data = {
        event = "onPlayerEquipRing",
        args = {
            playerid = playerid,
            handId = handId,
            instance = instance
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerEquipShield", function(playerid, instance)
{
    local data = {
        event = "onPlayerEquipShield",
        args = {
            playerid = playerid,
            instance = instance
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerEquipSpell", function(playerid, slotId, instance)
{
    local data = {
        event = "onPlayerEquipSpell",
        args = {
            playerid = playerid,
            slotId = slotId,
            instance = instance
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerJoin", function(playerid)
{
    local data = {
        event = "onPlayerJoin",
        args = {
            playerid = playerid
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerMessage", function(playerid, message)
{
    local data = {
        event = "onPlayerMessage",
        args = {
            playerid = playerid,
            message = message
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerMobInteract", function(playerid, from, to)
{
    local data = {
        event = "onPlayerMobInteract",
        args = {
            playerid = playerid,
            from = from,
            to = to
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerRespawn", function(playerid)
{
    local data = {
        event = "onPlayerRespawn",
        args = {
            playerid = playerid
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerShoot", function(playerid, munition)
{
    local data = {
        event = "onPlayerShoot",
        args = {
            playerid = playerid,
            munition = munition
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerSpellCast", function(playerid, instance, spellLevel)
{
    local data = {
        event = "onPlayerSpellCast",
        args = {
            playerid = playerid,
            instance = instance,
            spellLevel = spellLevel
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerSpellSetup", function(playerid, instance)
{
    local data = {
        event = "onPlayerSpellSetup",
        args = {
            playerid = playerid,
            instance = instance
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerTakeItem", function(playerid, itemGround)
{
    local data = {
        event = "onPlayerTakeItem",
        args = {
            playerid = playerid,
            obj_ItemGround = {
                name = "itemGround",
                data = _PyG2O_Serialize(itemGround)
            }
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerTeleport", function(playerid, vobName)
{
    local data = {
        event = "onPlayerTeleport",
        args = {
            playerid = playerid,
            vobName = vobName
        }
    }

    _PyG2O_Send(data);
});

addEventHandler("onPlayerToggleFaceAni", function(playerid, aniName, toggle)
{
    local data = {
        event = "onPlayerToggleFaceAni",
        args = {
            playerid = playerid,
            aniName = aniName,
            toggle = toggle
        }
    }

    _PyG2O_Send(data);
});