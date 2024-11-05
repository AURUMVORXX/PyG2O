import sqg2o

class DamageDescription(sqg2o.DamageDescription):
    
    def __init__(self):
        return super().__init__()
    
    @property
    def item_instance(self):
        return super().item_instance
    
    @property
    def flags(self):
        return super().flags
    
    @flags.setter
    def flags(self, value):
        super().flags = value
        
    @property
    def damage(self):
        return super().damage
    
    @damage.setter
    def damage(self, value):
        super().damage = value
        
    @property
    def distance(self):
        return super().distance
    
    @distance.setter
    def distance(self, value):
        super().distance = value
        
    @property
    def spell_id(self):
        return super().spell_id
    
    @spell_id.setter
    def spell_id(self, value):
        super().spell_id = value
        
    @property
    def spell_level(self):
        return super().spell_level
    
    @spell_level.setter
    def spell_level(self, value):
        super().spell_level = value
        
    @property
    def node(self):
        return super().node
    
    @node.setter
    def node(self, value):
        super().node = value