
function _message_call(data)
{
    local result = compilestring(data["data"])();
    local className = _getClassName(result);
    if (className != null)
    {
        data["data"] = {};
        data["data"]["obj_name"] <- className;
        data["data"]["obj_data"] <- _serializeObject(result);
    }
    else
        data["data"] = result;

    _send("result", data["data"], data["uuid"]);
}