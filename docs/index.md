## How to use
1. Install [G2O WebSocket module](https://github.com/AURUMVORXX/G2O-WebSocket) to your server
2. Install [JSON module](https://gitlab.com/GothicMultiplayerTeam/modules/json) to your server
3. Download **include/** folder and import the Squirrel part of the library:
```xml
<import src="include/pyg2o.xml" />
```
2. Install python library to your application
```
pip install pyg2o
```
3. Launch websocket client in your Squirrel scripts
```
// PyG2O(url, silent, max_reconnect_attempts)
// silent - disable information prints
// max_reconnect_attempts - maximum reconnect attempts if server will stop the connection (0 - infinite attempts). This value doesn't reset on connection

// Start server
local srv = PyG2O("ws://localhost:8080", false, 15)
srv.start()
// Stop server
srv.stop()
```
4. In your application, launch asyncio event loop and websocket server
```python
import pyg2o
import asyncio

srv = None

async def main():
    global srv
    srv = pyg2o.PythonWebsocketServer(
        host='localhost',
        port=8080,
        ping_interval=30,
        whitelist=['::1'],
    )
    try:
        await srv.start()
    except asyncio.CancelledError:
        await srv.stop()
        
if __name__ == '__main__':
    asyncio.run(main())
```