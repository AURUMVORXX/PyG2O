
_globalInstance <- -1;

class PyG2O
{
    _connection = -1;
    _silent = false;
    _url = -1;
    _reconnect_attempts = 0;
    _max_reconnect_attempts = 0;

    _constantsInitialized = false;
    _messageHandlers = null;

    constructor(url, silent = false, max_reconnect_attempts = 0)
    {
        _url = url;
        _max_reconnect_attempts = max_reconnect_attempts;
        _silent = silent;
        _messageHandlers = {};

        _connection = WebsocketClient();
        _connection.silent = _silent;
        _connection.setUrl(_url);

        _connection.onOpen = _onOpen.bindenv(this);
        _connection.onClose = _onClose.bindenv(this);
        _connection.onMessage = _onMessage.bindenv(this);

        _registerMessage("call", _message_call.bindenv(this));

        if (_globalInstance == -1)
            _globalInstance = this;
    }

    function start()
    {
        _connection.start();
        if (_connection.running)
            print("[PyG2O] Initializing connection on " + _url);
    }

    function stop()
    {
        _connection.stop();
        if (!_connection.running)
            print("[PyG2O] Stopped connection");
    }

    function _registerMessage(type, handler)
    {
        if (type in _messageHandlers)
            return;

        _messageHandlers[type] <- handler;
    }

    function _callMessage(type, data)
    {
        if(!(type in _messageHandlers))
            return;

        _messageHandlers[type](data);
    }

    function _send(type, data, uuid = "none")
    {
        local sendData = {
            "type": type,
            "data": data,
            "uuid": uuid
        }

        _connection.send(JSON.dump_ansi(sendData, 2));
    }

    function _initializeConstants()
    {
        if (_constantsInitialized)
            return;

        _send("init_constants", getconsttable());
    }

    function _getClassName(object)
    {
        if (object instanceof DamageDescription)
            return "DamageDescription";
        else if (object instanceof ItemGround)
            return "ItemGround";
        else if (object instanceof Vec3)
            return "Vec3";
        else if (object instanceof Vec2i)
            return "Vec2i";

        return null;
    }

    function _serializeObject(object)
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

    function _onOpen(url)
    {
        _initializeConstants();
        if (!_silent)
            print("[PyG2O] Successfully connected to " + url);
    }

    function _onClose(url, message)
    {
        if (_max_reconnect_attempts == 0)
            return;

        _reconnect_attempts += 1;
        if (_reconnect_attempts < _max_reconnect_attempts)
            return;

        _connection.stop();
    }

    function _onMessage(url, message)
    {
        local request = JSON.parse_ansi(message);
        if (!("type" in request) ||
            !("uuid" in request) ||
            !("data" in request))
            return;

        _callMessage(request["type"], request);
    }
}
