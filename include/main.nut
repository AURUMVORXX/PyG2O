
local _pyg2o_server_connection = -1;
local _silent = false;
local _url = -1
local _reconnect = false;

function PyG2O_Start(url, reconnect = false, silent = false)
{
    _silent = silent;
    _url = url;
    _reconnect = reconnect;

    _pyg2o_server_connection = WebsocketClient();
    _pyg2o_server_connection.silent = true;
    _pyg2o_server_connection.setUrl(url);
    _pyg2o_server_connection.start();

    if (!_silent)
        print("[PyG2O] Initializing connection on " + url)
}

function _PyG2O_Send(data)
{
    if (_pyg2o_server_connection == -1)
        return;

    _pyg2o_server_connection.send(JSON.dump_ansi(data));
}

function _PyG2O_InitializeConstants()
{
    local const_data = {
        "type": "const_init",
        "args": getconsttable()
    };

    _PyG2O_Send(const_data);
}

function _PyG2O_GetClassName(object)
{
    if (object instanceof DamageDescription)
        return "DamageDescription";
    else if (object instanceof ItemGround)
        return "ItemGround";

    return null;
}

function _PyG2O_Serialize(object)
{
    local cls = object.getclass();
    local tab = {};

    if (object instanceof DamageDescription)
    {
        tab["_flags"] <- object.flags;
        tab["_damage"] <- object.damage;
        tab["_item_instance"] <- object.item_instance;
        tab["_distance"] <- object.distance;
        tab["_spell_id"] <- object.spell_id;
        tab["_spell_level"] <- object.spell_level;
        tab["_node"] <- object.node;
    }
    else if (object instanceof ItemGround)
    {
        tab["_id"] <- object.id;
        tab["_instance"] <- object.instance;
        tab["_amount"] <- object.amount;
        tab["_world"] <- object.world;
        tab["_virtualWorld"] <- object.virtualWorld;
        tab["_position"] <- object.getPosition();
        tab["_rotation"] <- object.getRotation();
    }

    return tab;
}

addEventHandler("onWebsocketConnect", function(socket, url)
{
    if (socket != _pyg2o_server_connection)
        return;

    if (!_silent)
    {
        print("[PyG2O] Successfully connected to " + url);
        _PyG2O_InitializeConstants();
    }
});

addEventHandler("onWebsocketDisconnect", function(socket, url)
{
    if (socket != _pyg2o_server_connection || _reconnect)
        return;

    _pyg2o_server_connection = -1;
});

addEventHandler("onWebsocketMessage", function(socket, url, message)
{
    if (socket != _pyg2o_server_connection)
        return;

    local request = JSON.parse_ansi(message);
    if ("uuid" in request)
    {
        local result = compilestring(request["args"])();
        local className = _PyG2O_GetClassName(result);
        if (className != null)
        {
            className = format("obj_%s", className)

            request["args"] = {};
            request["args"].rawset(className, {});
            local objTab = request["args"].rawget(className);
            objTab["name"] <- "result";
            objTab["data"] <- _PyG2O_Serialize(result);
        }
        else
        {
            request["args"] =
            {
                "result": result
            };
        }
        _pyg2o_server_connection.send(JSON.dump_ansi(request, 2));
    }
});
