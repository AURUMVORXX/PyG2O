import websockets
import asyncio
import logging
import json
import uuid
from typing import Optional
from .constants import Constant
from .functions.event import callEvent
from .serialize import _deserialize

class PythonWebsocketServer:
    
    _current_server = None
    
    def __init__(self, host: str, port: int, whitelist: list[str], ping_interval: int = 30, silent: bool = False, logger: logging.Logger = None):    
        self.host: str = host
        self.port: int = port
        self.ping_interval: int = ping_interval
        self.whitelist = whitelist
        self.silent = silent
        self.logger = logger if logger is not None else logging.root
        
        self.requests_list: dict[str, asyncio.Future] = dict()
        self._stop_event: asyncio.Event = asyncio.Event()
        self.connected_socket: Optional[websockets.ClientConnection] = None
        
    @classmethod
    async def get_server(cls):
        return cls._current_server
        
    async def start(self):
        async with websockets.serve(
            self.handle_connection,
            host=self.host,
            port=self.port,
            ping_interval=self.ping_interval,
        ):
            self.logger.info(f'[PyG2O] Server is started at ws://{self.host}:{self.port}')
            PythonWebsocketServer._current_server = self
            asyncio.create_task(callEvent('onInit', **{}))
            await self._stop_event.wait()
            
    async def stop(self):
        PythonWebsocketServer._current_server = None
        self.connected_socket = None
        self._stop_event.set()
            
    async def make_request(self, data: str):
        if (self.connected_socket is None):
            return None
        
        request_id = str(uuid.uuid4())
        self.requests_list[request_id] = asyncio.get_running_loop().create_future()
        request = {
            'uuid': request_id,
            'args': data,
        }
        request = json.dumps(request)
        
        formatted_request = request.replace("'", '\\"')
        formatted_request = formatted_request.replace("False", 'false')
        formatted_request = formatted_request.replace("True", 'true')
        
        await self.connected_socket.send(formatted_request)
        result = await asyncio.wait_for(
            self.requests_list[request_id],
            timeout=30
        )
        return result
        
    
    async def handle_connection(self, websocket: websockets.ClientConnection):
        
        if (websocket.remote_address[0] not in self.whitelist or self.connected_socket is not None):
            await websocket.close(4000, 'Connection denied')
            return
        
        self.connected_socket = websocket
        self.is_connected = websocket
        if (not self.silent):
            self.logger.info(f'Client connected: {websocket.remote_address}')
            
        asyncio.create_task(callEvent('onWebsocketConnect', **{}))
        
        try:
            async for message in websocket:
                
                message_json = json.loads(message)
                
                # Deserializing objects
                if ('args' in message_json):
                    formatted_args = dict()
                    for key, value in message_json['args'].items():
                        if not key.startswith('obj_'):
                            formatted_args[key] = value
                            continue
                        
                        formatted_args[value['name']] = _deserialize(key, value['data'])
                    message_json['args'] = formatted_args
                
                # Processing events
                if ('event' in message_json):
                    asyncio.create_task(callEvent(message_json['event'], **formatted_args))
                    continue
                
                # Processing requests from Squirrel side
                if ('type' in message_json):
                    Constant._update(message_json['args'])
                    continue
                
                # Processing made requests
                if (    
                    'uuid' in message_json and
                    message_json['uuid'] in self.requests_list.keys()
                ):
                    self.requests_list[message_json['uuid']].set_result(next(iter(message_json['args'].values())))
                        
                        
        except json.JSONDecodeError as e:
            self.logger.exception(f'[PyG2O] JSON Exception: {e}')
        except Exception as e:
            self.logger.exception(f'[PyG2O] Exception: {e}')
        finally:
            if (not self.silent):
                self.logger.info('Client disconnected')
            self.is_connected = None
            self.connected_socket = None
            asyncio.create_task(callEvent('onWebsocketDisconnect', **{}))