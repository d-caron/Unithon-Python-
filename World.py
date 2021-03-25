import json

class World :
    """
    Represente une version simplifie d'un monde pour pouvoir communiquer
    avec le client Unity

    @attr :     String id -> identifiant d'un monde 
                (ou d'une scene unity)
                String[] regions -> liste d'identifiants de regions
                d'un monde (ou partie d'une scene unity)
    """

    def __init__ (self) :
        "Constructeur"

        self.id = None
        self.regions = []

    def get_dict (self) : 
        """
        @do :       Cree un dictionnaire representant l'objet
        @args :     None
        @return :   Dictionnaire representant l'objet
        """

        return self.__dict__