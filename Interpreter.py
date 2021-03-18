import DAO

def command_interpreter(message): #fonction qui détecte les commandes et appelle la fonction build_msg avec le paramètre correspondant
    words=message.split(' ') #on sépare les mots
    listOfCharacters = ["Michel","Ugo"] #recevoir la liste complète des IA et tester si le paramètre IA2 est une IA. Si ce n'est pas une IA, alors c'est un lieu

    msg = build_msg (words, listOfCharacters)  
    return msg   


def build_msg(words, listOfCharacters):
    msg = DAO.DAO ()
    msg.type = words[0]

    if len(words) > 1 :
        if msg.type == "cmd" :
            return cmd_handler (words[1:], listOfCharacters, msg)

        elif msg.type == "sys":
            return sys_handler (words[1:], msg)

        else :
            print ("ERR > Veuillez renseigner un type d'action valide")

    else :
        print ("ERR > Veuillez renseigner une action valide")


# GESTION DES COMMANDES

def cmd_handler (cmd, listOfCharacters, msg) :
    msg.action = cmd[0]

    if msg.action == "deplacer" :
        return cmd_deplacer (cmd[1:], listOfCharacters, msg)
        
    elif msg.action == "discuter" :
        return cmd_discuter (cmd[1:], listOfCharacters, msg)

    print ("ERR > " + cmd[0] + " n'est pas une commande \"cmd\" valide")

def sys_handler (sys, msg) :
    msg.action = sys[0]

    if msg.action == "exit" :
        return msg

    print ("ERR > " + sys[0] + " n'est pas une commande \"sys\" valide")


# GESTIONS : TYPE CMD

def cmd_deplacer (cmd, listOfCharacters, msg) :
    if len (cmd) != 2 :
        print ("ERR > Usage : cmd deplacer <IA1> <IA2>")
    else :
        if cmd[0] in listOfCharacters :
            msg.characters.append(cmd[0])

            if cmd[1] in listOfCharacters :
                msg.characters.append(cmd[1])

                return msg
            else :
                print ("ERR > Le déplacement vers un objet autre qu'un personnage n'est pas encore possible (Coming soon !)")
    
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