
def _deserialize(className, data):
    from .classes.damage import DamageDescription
    from .classes.items import ItemGround
    
    className = className[4:]
    new_cls = None
    if className == 'DamageDescription':
        new_cls = DamageDescription()
    elif className == 'ItemGround':
        new_cls = ItemGround()
    
    new_cls._initialize(**data)    
    return new_cls