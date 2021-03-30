from World import World
import json

class DAO :
    def __init__ (self) :
        "Constcteur"
        self.type = None
        self.action = None
        self.characters = []
        self.world = World ()

    
    def serialize (self) :
        """
        @do :       Serialise l'objet python au format JSON
        @args :     None
        @return :   String -> l'objet au format JSON
        """

        world = self.world
        self.world = self.world.get_dict ()
        json_str = json.dumps (self.__dict__, indent=2)
        self.world = world

        return json_str

    
    def deserialize (self, json_dao) :
        """    
        @do :       Deserialise la string au format JSON 
                    et stoque les informations dans cet objet
        @args :     String json_dao -> objet au format json
        @return :   DAO -> L'objet est retourne
        """

        data = json.loads (json_dao)
        if "type" in data.keys () : self.type = data["type"]
        if "action" in data.keys () : self.action = data["action"]
        if "characters" in data.keys () : self.characters = data['characters']
        if "world" in data.keys () : 
            self.world.id = data["world"]["id"]
            if "regions" in data["world"] : self.world.regions = data["world"]["regions"]

        return self
