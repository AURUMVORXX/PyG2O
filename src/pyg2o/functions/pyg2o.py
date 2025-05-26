from ..server import PythonWebsocketServer

async def call_squirrel_function(function_name: str, *args):
    
    arg_list = ', '.join(args)
    data = f'return {function_name}({arg_list})'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result