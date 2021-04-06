from DAO import DAO

def recv_handler (dao, listOfCharacters, listOfRegions) :
    """
    @do :       Interprete les messages recus 
    @args :     DAO dao -> Message recu
                String[] list_of_characters 
                    -> liste de IA disponibles
                String[] list_of_regions 
                    -> liste des regions disponibles
    @return :   String -> l'action a realiser s'il y en a une
    """
    
    if dao.type == "info" :
        if dao.action == "add_characters" :
            listOfCharacters.extend (dao.characters)
        
        elif dao.action == "add_regions" :
            listOfRegions.extend (dao.world.regions)
    
    elif dao.type == "sys" :
        if dao.action == "exit" :
            return "exit"

    else :
        return "error"