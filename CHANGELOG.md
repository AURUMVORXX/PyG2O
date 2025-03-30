## Changelog

- All event functions, called events and some other functions now have built-in exception handler
- Added new function: ``set_default_logger`` for redirect all built-in exception messages to your custom logger
- Added new decorator: ``handle_exception`` for convinient exception handling
- Changed function ``setTime``: now all arguments are optional, so you can partially change time, and you can pass negative values to subtract them from current time.
- Changed function ``getDistance2d``: now accepts old variant ``(x1, y1, x2, y2)`` OR ``({x: value1, y: value1}, {x: value2, y: value2})``
- Changed function ``getDistance3d``: now accepts old variant ``(x1, y1, z1, x2, y2, z2)`` OR ``({x: value1, y: value1, z: value1}, {x: value2, y: value2, z: value2})``
- Changed function ``getVectorAngle``: now accepts old variant ``(x1, y1, z1, x2, y2, z2)`` OR ``({x: value1, y: value1, z: value1}, {x: value2, y: value2, z: value2})``
- Changed function ``setPlayerPosition``: now accepts old variant ``(playerid, x, y, z)`` OR ``(playerid, {x: value, y: value, z: value})``
- Changed function ``setPlayerScale``: now accepts old variant ``(playerid, x, y, z)`` OR ``(playerid, {x: value, y: value, z: value})``
- Added function ``setPlayerAttributes`` (module-specific function)
- Added function ``setPlayerTalents`` (module-specific function)