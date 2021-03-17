import json

def command_interpreter(message): #fonction qui détecte les commandes et appelle la fonction build_json avec le paramètre correspondant
    
    
    words=message.split(' ') #on sépare les mots 
    jsonMessage = None
    listOfCharacters = ["Michel","Ugo"] #recevoir la liste complète des IA et tester si le paramètre IA2 est une IA. Si ce n'est pas une IA, alors c'est un lieu

    if(words[0] == "cmd" ): 
        
        if(len(words) != 4):
            
            print("Usage : cmd action <IA1> <IA2> ou cmd action <IA1> <lieu>")
        
        else:
           
            if(not words[2] in listOfCharacters):
                
                print("Le troisième argument n'est pas un PNJ")
            
            else:
   
                if(not words[3] in listOfCharacters and words[1] == "discuter"): #si la commande est discuter mais que le quatrième argument est autre chose qu'un PNJ
                
                    print("Une personne ne peut pas discuter toute seule !")

                else:

                    jsonMessage = build_json(words,listOfCharacters)

    elif(words[0] == "sys" ):
        
        if (words[1] == "load" and len(words != 3)):

            print("Usage : sys load map")   

        elif(len(words) != 2): #si la comande ne contient pas exactement 2 mots, la commande système n'est pas valide
            
            print("Usage : sys action")
        
        else:
            
            jsonMessage = build_json(words,listOfCharacters)
            
    return jsonMessage        


def build_json(words,listOfCharacters):
    
    if(words[0] == "cmd"):
       
        if (words[2] in listOfCharacters): #si le troisième argument est un PNJ, alors l'attribut monde est null
            
            Message = {
                "Message":{
                    "type" : words[0],
                    "action" : words[1],
                    "id_personnages" : words[2:],
                    "monde" : None
                }
            }

        else: #si le troisième argument n'est pas un PNJ alors c'est un lieu
            
            Message = {
                "Message":{
                    "type" : words[0],
                    "action" : words[1],
                    "id_personnages" : None,
                    "monde" : words[2]
                }
            }

    elif(words[0] == "sys" and words[2] == None):
        
        Message = {
            "Message":{
                "type" : words[0],
                "action" : words[1],
                "id_personnages" : None,
                "monde" : None
                }
        } 
    else: #c'est une commande load donc il y a un argument monde
          Message = {
            "Message":{
                "type" : words[0],
                "action" : words[1],
                "id_personnages" : None,
                "monde" : words[2]
                }
        }

    return Message    




