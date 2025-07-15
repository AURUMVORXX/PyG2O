import websockets
import asyncio
import json
import uuid
from typing import Optional
from .constants import Constant
from .functions.event import callEvent
from .serialize import _deserialize
from loguru import logger

class PythonWebsocketServer:
    
    _current_server = None
    
    def __init__(self, host: str, port: int, whitelist: list[str], ping_interval: int = 30):    
        self.host: str = host
        self.port: int = port
        self.ping_interval: int = ping_interval
        self.whitelist = whitelist
        
        self._messageHandlers: dict[str, callable] = dict()
        self._requests_list: dict[str, asyncio.Future] = dict()
        self._stop_event: asyncio.Event = asyncio.Event()
        self._connected_socket: Optional[websockets.ClientConnection] = None
        
        self._registerMessage('event', self._message_event)
        self._registerMessage('init_constants', self._message_init_constants)
        self._registerMessage('result', self._message_call_result)
        
    @classmethod
    async def get_server(cls):
        return cls._current_server
    
    def _registerMessage(self, type: str, handler: callable):
        if type in self._messageHandlers:
            return
        
        self._messageHandlers[type] = handler
        
    async def _callMessage(self, type: str, data: dict):
        if type not in self._messageHandlers:
            return
        
        await self._messageHandlers[type](data)
    
    async def start(self):
        async with websockets.serve(
            self.handle_connection,
            host=self.host,
            port=self.port,
            ping_interval=self.ping_interval,
        ):
            logger.success(f'Server is started at ws://{self.host}:{self.port}')
            PythonWebsocketServer._current_server = self
            asyncio.create_task(callEvent('onInit', **{}))
            await self._stop_event.wait()
            
    async def stop(self):
        PythonWebsocketServer._current_server = None
        self._connected_socket = None
        self._stop_event.set()
            
    async def make_request(self, data: str):
        if (self._connected_socket is None):
            return None
        
        request_id = str(uuid.uuid4())
        self._requests_list[request_id] = asyncio.get_running_loop().create_future()
        request = {
            'type': 'call',
            'uuid': request_id,
            'data': data,
        }
        request = json.dumps(request)
        request = request.replace("'", '\\"')
        request = request.replace('True', 'true')
        request = request.replace('False', 'false')
        
        await self._connected_socket.send(request)
        result = await asyncio.wait_for(
            self._requests_list[request_id],
            timeout=30
        )
        return result
    
    async def _message_event(self, data: dict):
        if (not isinstance(data['data'], dict) or
            'event' not in data['data']):
            return
        
        eventName = data['data']['event']
        del data['data']['event']
        
        if 'desc' in data['data']:
            obj_name = data['data']['desc']['obj_name']
            obj_data = data['data']['desc']['obj_data']
            data['data']['desc'] = _deserialize(obj_name, obj_data)
        elif 'itemGround' in data['data']:
            obj_name = data['data']['itemGround']['obj_name']
            obj_data = data['data']['itemGround']['obj_data']
            data['data']['itemGround'] = _deserialize(obj_name, obj_data)
        
        asyncio.create_task(callEvent(eventName, **data['data']))
        
    async def _message_init_constants(self, data: dict):
        if data['data'] is not dict:
            return
        
        Constant._update(data['data'])
        
    async def _message_call_result(self, data: dict):
        if data['uuid'] not in self._requests_list:
            return
        
        result = data['data']
        if (isinstance(data['data'], dict) and
            'obj_name' in data['data'] and
            'obj_data' in data['data']):
            result = _deserialize(result['obj_name'], result['obj_data'])
            
        self._requests_list[data['uuid']].set_result(result)
        del self._requests_list[data['uuid']]
    
    async def handle_connection(self, websocket: websockets.ClientConnection):
        
        if len(self.whitelist) != 0 and websocket.remote_address[0] not in self.whitelist:
            await websocket.close(4000, 'Connection denied (whitelist)')
            return
        
        if self._connected_socket is not None:
            await websocket.close(4000, 'Connection denied (already_connected)')
            return
        
        self._connected_socket = websocket
        self.is_connected = websocket
        logger.info(f'Client connected: {websocket.remote_address}')
            
        asyncio.create_task(callEvent('onWebsocketConnect', **{}))
        
        try:
            async for message in websocket:
                try:
                    message_json = json.loads(message)
                    if not all(key in message_json for key in ('type', 'uuid', 'data')):
                        logger.error(f'Expected message with (type, uuid, data) fields, got: {message_json}')
                        continue
                    
                    await self._callMessage(message_json['type'], message_json)
                        
                except json.JSONDecodeError as e:
                    logger.exception(f'JSON Exception: {e}')
                    continue
                except Exception as e:
                    logger.exception(f'Exception: {e}')
                    continue
        except websockets.exceptions.ConnectionClosedError:
            pass
        finally:
            logger.info('Client disconnected')
            self.is_connected = None
            self._connected_socket = None
            asyncio.create_task(callEvent('onWebsocketDisconnect', **{}))