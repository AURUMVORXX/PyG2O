import sqg2o

class Mds:
    
    @staticmethod
    def id(mdsName : str) -> int:
        return sqg2o.Mds.id(mdsName)
    
    @staticmethod
    def name(mdsId : id) -> str:
        return sqg2o.Mds.name(mdsId)