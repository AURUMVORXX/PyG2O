
class DamageDescription():
    """
    This class represents damage information.
    Original: [DamageDescription](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-classes/item/DamageDescription//)
    
    ## `int` flags
    Represents the damage flags.

    ## `int` damage
    Represents the total damage taken.
    
    ## `str` item_instance *(read-only)*
    !!! note
        Can be empty if there is no weapon.
    Represents the weapon instance used to deal damage.
    
    ## `int` distance
    Represents the total distance, calculated from origin point to target.
    
    ## `int` spell_id
    Represents the spell id.
    
    ## `int` spell_level
    Represents the level of chargeable spells.
    
    ## `str` node
    !!! note
        Can be empty if there was no projectile.
    Represents the name of the node hit by a point projectile.
    """
    def __init__(self):
        self._flags : int = 0
        self._damage : int = 0
        self._item_instance : str = ''
        self._distance : int = 0
        self._spell_id : int = 0
        self._spell_level : int = 0
        self._node : str = 0
    
    def _initialize(self, **kwargs):
        self.__dict__.update(kwargs)
        
    @property
    def flags(self) -> int:
        return self._flags
    
    @flags.setter
    def flags(self, value):
        self._flags = value
        
    @property
    def damage(self) -> int:
        return self._damage
    
    @damage.setter
    def damage(self, value):
        self._damage = value
        
    @property
    def item_instance(self) -> str:
        return self._item_instance
    
    @property
    def distance(self) -> int:
        return self._distance
    
    @distance.setter
    def distance(self, value):
        self._distance = value
        
    @property
    def spell_id(self) -> int:
        return self._spell_id
    
    @spell_id.setter
    def spell_id(self, value):
        self._spell_id = value
        
    @property
    def spell_level(self) -> int:
        return self._spell_level
    
    @spell_level.setter
    def spell_level(self, value):
        self._spell_level = value
        
    @property
    def node(self) -> str:
        return self._node
    
    @node.setter
    def node(self, value):
        self._node = value