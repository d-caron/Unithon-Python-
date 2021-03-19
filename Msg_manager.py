from DAO import DAO

def recv_handler (dao, listOfCharacters, listOfRegions) :
    
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