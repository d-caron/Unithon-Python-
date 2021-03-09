import json


def command_interpreter(message): #fonction qui détecte les commandes et appelle la fonction build_json avec le paramètre correspondant
    
    type = -1
    words=message.split(' ') #on sépare les mots 
    jsonMessage = None

    if(words[0] == "deplacer" ): #rajouter les conditions pour les autres action ici ex: words[0] == "déplacer" or words[0] == "manger"...
        
        if(len(words) != 3):
            
            print("Usage : deplacer <IA1> <IA2>")
        
        else:
            type = 1
            jsonMessage = build_json(type,words)
            

    return jsonMessage        


def build_json(type,words):
    
    if(type == 1):
        
        Message = {
            "Message":{
                "type" : type,
                "action" : words[0],
                "id_personnages" : words[1:],
                "monde" : None
            }
    
        }
    

        return Message    




