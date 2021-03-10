from World import World
import json

class DAO :
    def __init__ (self) :
        self.type = None
        self.action = None
        self.characters = []
        self.world = World ()

    """ serialize

    Sérialise l'objet python au format JSON
    
    retour : Une String représentant l'objet au format JSON
    """
    def serialize (self) :
        self.world = self.world.get_dict ()
        return json.dumps (self.__dict__, indent=2)

    """ deserialize
    
    Désérialise la string au format JSON 
    et stoque les informations dens cet objet
    
    retour : L'objet est retourné
    """
    def deserialize (self, json_dao) :
        data = json.loads (json_dao)
        if "type" in data.keys () : self.type = data["type"]
        if "action" in data.keys () : self.action = data["action"]
        if "characters" in data.keys () : self.characters = data['characters']
        if "world" in data.keys () : 
            self.world.id = data["world"]["id"]
            if "regions" in data["world"] : self.world.regions = data["world"]["regions"]

        return self
