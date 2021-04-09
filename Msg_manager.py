from DAO import DAO

def recv_handler (dao, listOfCharacters, listOfRegions,listOfWorlds) :
    
    if dao.type == "info" :
        if dao.action == "add_characters" :
            listOfCharacters.extend (dao.characters)
        
        elif dao.action == "add_regions" :
            for i in dao.world.regions:
                if i not in listOfRegions:
                    listOfRegions.append(i)
           

        elif dao.action == "add_worlds":
            for i in dao.world.regions:
                if i not in listOfWorlds:
                    listOfWorlds.append(i)
           
    
    elif dao.type == "sys" :
        if dao.action == "exit" :
            return "exit"

    else :
        return "error"