## How to use
1. Install [G2O WebSocket module](https://github.com/AURUMVORXX/G2O-WebSocket) to your server
1. Download **include/** folder and import the Squirrel part of the library:
```xml
<import src="include/pyg2o.exml" />
```
2. Install python library to your application
```
pip install git+https://github.com/AURUMVORXX/PyG2O.git
```
3. Launch websocket client in your Squirrel scripts
```
// PyG2O_Start(url, reconnect, silent)
// reconnect - auto reconnect if server stopped
// silent - disable information prints

// Start server before any events
PyG2O_Start("ws://localhost:8080", true, false)

addEventHandler("onInit"...
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
        silent=False,
        whitelist=['::1'],
    )
    try:
        await srv.start()
    except asyncio.CancelledError:
        await srv.stop()
        
if __name__ == '__main__':
    asyncio.run(main())
```