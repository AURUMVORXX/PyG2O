from ..server import PythonWebsocketServer
from ..call_repr import get_call_repr

async def clearNpcActions(npc_id : int):
    """
    This function clears remote NPC actions queue. Remote NPCs uses actions queue to execute thier tasks.
    Original: [clearNpcActions](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/clearNpcActions/)
    
    ## Declaration
    ```python
    async def clearNpcActions(npc_id : int)
    ```
    ## Parameters
    `int` **npc_id**: the npc identifier.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def createNpc(name : str, instance : str = 'PC_HERO') -> int:
    """
    !!! note
        By default npcs won't be added to world. In order to do that, you have to call [spawnPlayer](../player/spawnPlayer.md).
    !!! note
        Remote NPC id will always begins from max slots value.
    This function creates remote NPC.
    Original: [createNpc](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/createNpc/)
    
    ## Declaration
    ```python
    async def createNpc(name : str, instance : str = 'PC_HERO') -> int
    ```
    ## Parameters
    `str` **name**: the displayed name of the npc.
    `str` **instance**: the instance name of for the npc.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def destroyNpc(npc_id : int) -> bool:
    """
    This function destroys remote NPC.
    Original: [destroyNpc](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/destroyNpc/)
    
    ## Declaration
    ```python
    async def destroyNpc(npc_id : int) -> bool
    ```
    ## Parameters
    `int` **npc_id**: the identifier of npc.
    ## Returns
    `bool`: `true` when npc was successfully destroyed, otherwise false`.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getNpcAction(npc_id : int, index : int) -> dict:
    """
    This function gets information about element on specified index in NPC action queue.
    Original: [getNpcAction](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/getNpcAction/)
    
    ## Declaration
    ```python
    async def getNpcAction(npc_id : int, index : int) -> dict
    ```
    ## Parameters
    `int` **npc_id**: the identifier of npc.
    `int` **index**: the index of element in the queue.
    ## Returns
    `dict {type, id, status}`: The table containing information about selected element.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getNpcActions(npc_id : int) -> list:
    """
    This function gets informations about elements in NPC action queue.
    Original: [getNpcActions](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/getNpcActions/)
    
    ## Declaration
    ```python
    async def getNpcActions(npc_id : int) -> list
    ```
    ## Parameters
    `int` **npc_id**: the identifier of npc.
    ## Returns
    `list [{type, id}]`: The array containing information about queue elements.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getNpcActionsCount(npc_id : int) -> int:
    """
    This function gets elements count in NPC action queue.
    Original: [getNpcActionsCount](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/getNpcActionsCount/)
    
    ## Declaration
    ```python
    async def getNpcActionsCount(npc_id : int) -> int
    ```
    ## Parameters
    `int` **npc_id**: the identifier of npc.
    ## Returns
    `int`: The count of elements inside queue, otherwise `-1`.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getNpcHostPlayer(npc_id : int) -> int:
    """
    This function gets NPC host player id.
    Original: [getNpcHostPlayer](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/getNpcHostPlayer/)
    
    ## Declaration
    ```python
    async def getNpcHostPlayer(npc_id : int) -> int
    ```
    ## Parameters
    `int` **npc_id**: the identifier of npc.
    ## Returns
    `int`: the host player identifier. If there is no host player `-1` is returned instead.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def getNpcLastActionId(npc_id : int) -> int:
    """
    This function gets last action identifier, that was enqued to the NPC action queue. Every action in queue has associated unique id, by which can be identified.
    Original: [getNpcLastActionId](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/getNpcLastActionId/)
    
    ## Declaration
    ```python
    async def getNpcLastActionId(npc_id : int) -> int
    ```
    ## Parameters
    `int` **npc_id**: the identifier of npc.
    ## Returns
    `int`: The last finished action identifier, otherwise `-1`.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def isNpc(npc_id : int) -> bool:
    """
    This function checks whether id related to given object is remote NPC.
    Original: [isNpc](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/isNpc/)
    
    ## Declaration
    ```python
    async def isNpc(npc_id : int) -> bool
    ```
    ## Parameters
    `int` **npc_id**: the identifier of npc.
    ## Returns
    `bool`: `true` when object is NPC, otherwise `false`.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def isNpcActionFinished(npc_id : int, action_id : int) -> bool:
    """
    This function checks whether specified NPC action was finished.
    Original: [isNpcActionFinished](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/isNpcActionFinished/)
    
    ## Declaration
    ```python
    async def isNpcActionFinished(npc_id : int, action_id : int) -> bool
    ```
    ## Parameters
    `int` **npc_id**: the identifier of npc.
    `int` **action_id**: the unique action identifier.
    ## Returns
    `bool`: `true` if specified action identifier was already finished, otherwise `false`.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def npcAttackMelee(attacker_id : int, enemy_id : int, attack_type : int, combo : int):
    """
    !!! note
        Combo is internal Gothic value. Its behaviour can be sometimes undefined. For example -1 value doesn't work for not humanoid NPCs.
        
    This function enqueues attack melee action to the remote NPC action queue.
    Original: [npcAttackMelee](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/npcAttackMelee/)
    
    ## Declaration
    ```python
    async def npcAttackMelee(attacker_id : int, enemy_id : int, attack_type : int, combo : int)
    ```
    ## Parameters
    `int` **attacker_id**: the remote npc id.
    `int` **enemy_id**: the remote npc or player id.
    `int` **attack_type**: the type of attack.
    `int` **combol**: the combo sequence. For `-1` execute next command immediately.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def npcAttackRanged(attacker_id : int, enemy_id : int):
    """
    This function enqueues attack ranged action to the remote NPC action queue.
    Original: [npcAttackRanged](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/npcAttackRanged/)
    
    ## Declaration
    ```python
    async def npcAttackRanged(attacker_id : int, enemy_id : int)
    ```
    ## Parameters
    `int` **attacker_id**: the remote npc id.
    `int` **enemy_id**: the remote npc or player id.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def npcSpellCast(attacker_id : int, enemy_id : int):
    """
    This function enqueues spell cast action to the remote NPC action queue.
    Original: [npcSpellCast](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/npcSpellCast/)
    
    ## Declaration
    ```python
    async def npcSpellCast(attacker_id : int, enemy_id : int)
    ```
    ## Parameters
    `int` **attacker_id**: the remote npc id.
    `int` **enemy_id**: the remote npc or player id.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def npcUseClosestMob(npc_id : int, sceme : str, target_state : int):
    """
    This function enqueues use closest mob action to the remote NPC action queue.
    Original: [npcUseClosestMob](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/npcUseClosestMob/)
    
    ## Declaration
    ```python
    async def npcUseClosestMob(npc_id : int, sceme : str, target_state : int)
    ```
    ## Parameters
    `int` **npc_id**: the npc identifier.
    `str` **sceme**: the animation sceme name, e.g: `"BENCH"` when you want to interact with bench.
    `int` **target_state**: the target state, use `1` if you want to start interaction and `-1` to end it.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result

async def setNpcHostPlayer(npc_id : int, host_id : int) -> bool:
    """
    This function sets new NPC host player.
    Original: [setNpcHostPlayer](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/setNpcHostPlayer/)
    
    ## Declaration
    ```python
    async def setNpcHostPlayer(npc_id : int, host_id : int) -> bool
    ```
    ## Parameters
    `int` **npc_id**: the npc identifier.
    `int` **host_id**: the player host identifier.
    ## Returns
    `bool`: `true` if host was successfully changed, otherwise `false`.
    """
    data = f'return {get_call_repr()}'
    
    server = await PythonWebsocketServer.get_server()
    result = await server.make_request(data)
    return result