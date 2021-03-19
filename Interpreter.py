import DAO

def command_interpreter(message, characters, regions): #fonction qui détecte les commandes et appelle la fonction build_msg avec le paramètre correspondant
    words=message.split(' ')
    listOfCharacters = characters   # Liste des personnages
    listOfRegions = regions         # Liste des régions

    msg = build_msg (words, listOfCharacters, listOfRegions)  
    return msg   


def build_msg(words, listOfCharacters, listOfRegions):
    msg = DAO.DAO ()
    msg.type = words[0]

    if len(words) > 1 :
        if msg.type == "cmd" :
            return cmd_handler (words[1:], listOfCharacters, listOfRegions, msg)

        elif msg.type == "sys":
            return sys_handler (words[1:], msg)

        else :
            print ("ERR > Veuillez renseigner un type d'action valide")

    else :
        print ("ERR > Veuillez renseigner une action valide")


# GESTION DES COMMANDES

def cmd_handler (cmd, listOfCharacters, listOfRegions, msg) :
    msg.action = cmd[0]

    if msg.action == "deplacer" :
        return cmd_deplacer (cmd[1:], listOfCharacters, listOfRegions, msg)
        
    elif msg.action == "discuter" :
        return cmd_discuter (cmd[1:], listOfCharacters, msg)

    print ("ERR > " + cmd[0] + " n'est pas une commande \"cmd\" valide")

def sys_handler (sys, msg) :
    msg.action = sys[0]

    if msg.action == "exit" :
        return msg

    print ("ERR > " + sys[0] + " n'est pas une commande \"sys\" valide")

# GESTIONS : TYPE CMD

def cmd_deplacer (cmd, listOfCharacters, listOfRegions, msg) :
    if len (cmd) != 2 :
        print ("ERR > Usage : cmd deplacer <IA1> <IA2>")
    else :
        if cmd[0] in listOfCharacters :
            msg.characters.append(cmd[0])

            if cmd[1] in listOfCharacters :
                msg.characters.append(cmd[1])

                return msg

            elif cmd[1] in listOfRegions :
                msg.world.regions.append (cmd[1])

                return msg
            else :
                msg.world.regions.append (cmd[1])
                print ("ERR > Destination non valide")
    
        else : 
            print ("ERR > Usage : cmd deplacer <IA1> <IA2>")

def cmd_discuter (cmd, listOfCharacters, msg) :
    if len (cmd) != 2 :
        print ("ERR > Usage : cmd discuter <IA1> <IA2>")
    else :
        if cmd[0] in listOfCharacters :
            msg.characters.append(cmd[0])

            if cmd[1] in listOfCharacters :
                msg.characters.append(cmd[1])

                return msg
            else :
                print ("ERR > " + cmd[1] + " n'est pas un identifiant d'IA valide")
    
        else : 
            print ("ERR > " + cmd[0] + " n'est pas un identifiant d'IA valide")


# GESTION : TYPE SYS

# (Rien ici pour le moment)