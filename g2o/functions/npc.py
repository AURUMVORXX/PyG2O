import sqg2o

def clearNpcActions(npc_id : int):
    """
    This function clears remote NPC actions queue. Remote NPCs uses actions queue to execute thier tasks.
    Original: [clearNpcActions](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/clearNpcActions/)
    
    ## Declaration
    ```python
    clearNpcActions(npc_id : int)
    ```
    ## Parameters
    `int` **npc_id**: the npc identifier.
    """
    return sqg2o.clearNpcActions(npc_id)

def createNpc(name : str, instance : str = 'PC_HERO') -> int:
    """
    !!! note
        By default npcs won't be added to world. In order to do that, you have to call [spawnPlayer](../player/spawnPlayer.md).
    !!! note
        Remote NPC id will always begins from max slots value.
    This function creates remote NPC.
    Original: [createNpc](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/createNpc/)
    
    ## Declaration
    ```python
    def createNpc(name : str, instance : str = 'PC_HERO') -> int
    ```
    ## Parameters
    `str` **name**: the displayed name of the npc.
    `str` **instance**: the instance name of for the npc.
    """
    return sqg2o.createNpc(name, instance)

def destroyNpc(npc_id : int) -> bool:
    """
    This function destroys remote NPC.
    Original: [destroyNpc](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/destroyNpc/)
    
    ## Declaration
    ```python
    def destroyNpc(npc_id : int) -> bool
    ```
    ## Parameters
    `int` **npc_id**: the identifier of npc.
    ## Returns
    `bool`: `true` when npc was successfully destroyed, otherwise false`.
    """
    return sqg2o.destroyNpc(npc_id)

def getNpcAction(npc_id : int, index : int) -> dict:
    """
    This function gets information about element on specified index in NPC action queue.
    Original: [getNpcAction](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/getNpcAction/)
    
    ## Declaration
    ```python
    getNpcAction(npc_id : int, index : int) -> dict
    ```
    ## Parameters
    `int` **npc_id**: the identifier of npc.
    `int` **index**: the index of element in the queue.
    ## Returns
    `dict {type, id, status}`: The table containing information about selected element.
    """
    return sqg2o.getNpcAction(npc_id, index)

def getNpcActions(npc_id : int) -> list:
    """
    This function gets informations about elements in NPC action queue.
    Original: [getNpcActions](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/getNpcActions/)
    
    ## Declaration
    ```python
    def getNpcActions(npc_id : int) -> list
    ```
    ## Parameters
    `int` **npc_id**: the identifier of npc.
    ## Returns
    `list [{type, id}]`: The array containing information about queue elements.
    """
    return sqg2o.getNpcActions(npc_id)

def getNpcActionsCount(npc_id : int) -> int:
    """
    This function gets elements count in NPC action queue.
    Original: [getNpcActionsCount](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/getNpcActionsCount/)
    
    ## Declaration
    ```python
    def getNpcActionsCount(npc_id : int) -> int
    ```
    ## Parameters
    `int` **npc_id**: the identifier of npc.
    ## Returns
    `int`: The count of elements inside queue, otherwise `-1`.
    """
    return sqg2o.getNpcActionsCount(npc_id)

def getNpcHostPlayer(npc_id : int) -> int:
    """
    This function gets NPC host player id.
    Original: [getNpcHostPlayer](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/getNpcHostPlayer/)
    
    ## Declaration
    ```python
    getNpcHostPlayer(npc_id : int) -> int
    ```
    ## Parameters
    `int` **npc_id**: the identifier of npc.
    ## Returns
    `int`: the host player identifier. If there is no host player `-1` is returned instead.
    """
    return sqg2o.getNpcHostPlayer(npc_id)

def getNpcLastActionId(npc_id : int) -> int:
    """
    This function gets last action identifier, that was enqued to the NPC action queue. Every action in queue has associated unique id, by which can be identified.
    Original: [getNpcLastActionId](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/getNpcLastActionId/)
    
    ## Declaration
    ```python
    getNpcLastActionId(npc_id : int) -> int
    ```
    ## Parameters
    `int` **npc_id**: the identifier of npc.
    ## Returns
    `int`: The last finished action identifier, otherwise `-1`.
    """
    return sqg2o.getNpcLastActionId(npc_id)

def isNpc(npc_id : int) -> bool:
    """
    This function checks whether id related to given object is remote NPC.
    Original: [isNpc](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/isNpc/)
    
    ## Declaration
    ```python
    def isNpc(npc_id : int) -> bool
    ```
    ## Parameters
    `int` **npc_id**: the identifier of npc.
    ## Returns
    `bool`: `true` when object is NPC, otherwise `false`.
    """
    return sqg2o.isNpc(npc_id)

def isNpcActionFinished(npc_id : int, action_id : int) -> bool:
    """
    This function checks whether specified NPC action was finished.
    Original: [isNpcActionFinished](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/isNpcActionFinished/)
    
    ## Declaration
    ```python
    def isNpcActionFinished(npc_id : int, action_id : int) -> bool
    ```
    ## Parameters
    `int` **npc_id**: the identifier of npc.
    `int` **action_id**: the unique action identifier.
    ## Returns
    `bool`: `true` if specified action identifier was already finished, otherwise `false`.
    """
    return sqg2o.isNpcActionFinished(npc_id, action_id)

def npcAttackMelee(attacker_id : int, enemy_id : int, attack_type : int, combo : int):
    """
    !!! note
        Combo is internal Gothic value. Its behaviour can be sometimes undefined. For example -1 value doesn't work for not humanoid NPCs.
        
    This function enqueues attack melee action to the remote NPC action queue.
    Original: [npcAttackMelee](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/npcAttackMelee/)
    
    ## Declaration
    ```python
    def npcAttackMelee(attacker_id : int, enemy_id : int, attack_type : int, combo : int)
    ```
    ## Parameters
    `int` **attacker_id**: the remote npc id.
    `int` **enemy_id**: the remote npc or player id.
    `int` **attack_type**: the type of attack.
    `int` **combol**: the combo sequence. For `-1` execute next command immediately.
    """
    return sqg2o.npcAttackMelee(attacker_id, enemy_id, attack_type, combo)

def npcAttackRanged(attacker_id : int, enemy_id : int):
    """
    This function enqueues attack ranged action to the remote NPC action queue.
    Original: [npcAttackRanged](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/npcAttackRanged/)
    
    ## Declaration
    ```python
    def npcAttackRanged(attacker_id : int, enemy_id : int)
    ```
    ## Parameters
    `int` **attacker_id**: the remote npc id.
    `int` **enemy_id**: the remote npc or player id.
    """
    return sqg2o.npcAttackRanged(attacker_id, enemy_id)

def npcSpellCast(attacker_id : int, enemy_id : int):
    """
    This function enqueues spell cast action to the remote NPC action queue.
    Original: [npcSpellCast](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/npcSpellCast/)
    
    ## Declaration
    ```python
    def npcSpellCast(attacker_id : int, enemy_id : int)
    ```
    ## Parameters
    `int` **attacker_id**: the remote npc id.
    `int` **enemy_id**: the remote npc or player id.
    """
    return sqg2o.npcSpellCast(attacker_id, enemy_id)

def npcUseClosestMob(npc_id : int, sceme : str, target_state : int):
    """
    This function enqueues use closest mob action to the remote NPC action queue.
    Original: [npcUseClosestMob](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/npcUseClosestMob/)
    
    ## Declaration
    ```python
    def npcUseClosestMob(npc_id : int, sceme : str, target_state : int)
    ```
    ## Parameters
    `int` **npc_id**: the npc identifier.
    `str` **sceme**: the animation sceme name, e.g: `"BENCH"` when you want to interact with bench.
    `int` **target_state**: the target state, use `1` if you want to start interaction and `-1` to end it.
    """
    return sqg2o.npcUseClosestMob(npc_id, sceme, target_state)

def setNpcHostPlayer(npc_id : int, host_id : int) -> bool:
    """
    This function sets new NPC host player.
    Original: [setNpcHostPlayer](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-functions/npc/setNpcHostPlayer/)
    
    ## Declaration
    ```python
    def setNpcHostPlayer(npc_id : int, host_id : int) -> bool
    ```
    ## Parameters
    `int` **npc_id**: the npc identifier.
    `int` **host_id**: the player host identifier.
    ## Returns
    `bool`: `true` if host was successfully changed, otherwise `false`.
    """
    return sqg2o.setNpcHostPlayer(npc_id, host_id)