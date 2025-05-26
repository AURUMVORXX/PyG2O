
function _message_call(data)
{
    local compile_string = "try { " + data["data"] + " } catch(id) { print(\"[PyG2O] Error white executing the code: \" + id + \"\\nCode: " + data["data"] + "\"); return null; }";
    local result = compilestring(compile_string)();
    local className = _getClassName(result);
    if (className == "Vec3")
    {
        data["data"] = {};
        data["data"]["x"] <- result.x;
        data["data"]["y"] <- result.y;
        data["data"]["z"] <- result.z;
    }
    else if (className != null)
    {
        data["data"] = {};
        data["data"]["obj_name"] <- className;
        data["data"]["obj_data"] <- _serializeObject(result);
    }
    else
        data["data"] = result;

    _send("result", data["data"], data["uuid"]);
}