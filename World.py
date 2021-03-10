import json

class World :
    def __init__ (self) :
        self.id = None
        self.regions = []

    def get_dict (self) :
        return self.__dict__