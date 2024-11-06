import sqg2o

class Daedalus:
    
    @staticmethod
    def index(value : str) -> int:
        return sqg2o.Daedalus.index(value)
    
    @staticmethod
    def symbol(value : str) -> dict:
        return sqg2o.Daedalus.symbol(value)
    
    @staticmethod
    def instance(value : str) -> dict:
        return sqg2o.Daedalus.instance(value)