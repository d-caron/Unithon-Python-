from DAO import DAO

ERROR = "/!\\ "


def command_interpreter(message, characters, regions): 
    """
    @do :       L'interpreteur de commande deconstruit le message pour
                le transformer en objet de type DAO
    @args :     String message -> commande a interpreter
                String[] characters -> liste de IA disponibles
                String[] regions -> liste des regions disponibles
    @return :   DAO -> commande interprete au format DAO si correcte
                None -> si incorrecte
    """
    
    list_of_characters = characters
    list_of_regions = regions
    
    words = message.split(' ')
    msg = build_msg (words, list_of_characters, list_of_regions)

    return msg


def build_msg(words, list_of_characters, list_of_regions):
    """
    @do :       Construit le message DAO
    @args :     String[] words -> liste des termes de la commande
                String[] characters -> liste de IA disponibles
                String[] regions -> liste des regions disponibles
    @return :   DAO -> message DAO si la commande est correcte
                None -> si incorrecte
    """

    msg = DAO ()
    msg.type = words[0]

    if len(words) > 1 :
        if msg.type == "cmd" :
            return cmd_handler (words[1:], list_of_characters, list_of_regions, msg)

        elif msg.type == "sys" :
            return sys_handler (words[1:], msg)

        elif msg.type == "info" :
            info_handler (words[1:], list_of_characters, list_of_regions)

        elif msg.type == "help" :
            if words[1] == "type" :
                show_help_type ()
            elif words[1] == "cmd" :
                show_help_cmd ()
            elif words[1] == "sys" :
                show_help_sys ()
            elif words[1] == "info" :
                show_help_info ()

        else :
            print (ERROR + "ERR > " + words[0] + " : Type invalide.")
            print (ERROR + "Tapez \"help\" pour plus d'information")

    else :
        if msg.type == "help" :
            show_help ()
                
        else :
            print (ERROR + "ERR > Pas d'action renseignee")
            print (ERROR + "Tapez \"help\" pour plus d'information")


# GESTION DES COMMANDES

def cmd_handler (cmd, list_of_characters, list_of_regions, msg) :

    msg.action = cmd[0]

    if msg.action == "deplacer" :
        return cmd_deplacer (cmd[1:], list_of_characters, list_of_regions, msg)
        
    elif msg.action == "discuter" :
        return cmd_discuter (cmd[1:], list_of_characters, msg)

    print (ERROR + "ERR > " + cmd[0] + " : Action invalide")
    print (ERROR + "Tapez \"help\" pour plus d'information")

def sys_handler (sys, msg) :
    msg.action = sys[0]

    if msg.action == "exit" :
        return msg

    print (ERROR + "ERR > " + sys[0] + " : Action invalide")
    print (ERROR + "Tapez \"help\" pour plus d'information")

def info_handler (info, list_of_characters, list_of_regions) :
    if info[0] == "IA" :
        print (list_of_characters)
    
    elif info[0] == "regions" :
        print (list_of_regions)

    else : 
        print (ERROR + "ERR > " + info[0] + " : Action invalide")
        print (ERROR + "Tapez \"help\" pour plus d'information")

# GESTIONS : TYPE CMD

def cmd_deplacer (cmd, list_of_characters, list_of_regions, msg) :
    if len (cmd) != 2 :
        print (ERROR + "ERR > Usage : cmd deplacer <IA1> <IA2>|<region>")
    else :
        if cmd[0] in list_of_characters :
            msg.characters.append(cmd[0])

            if cmd[1] in list_of_characters :
                msg.characters.append(cmd[1])

                return msg

            elif cmd[1] in list_of_regions :
                msg.world.regions.append (cmd[1])

                return msg
            else :
                print (ERROR + "ERR > " + cmd[1] + " : Destination non valide")
                print (ERROR + "Tapez \"info IA\" ou \"info regions\" pour obtenir les liste des destinations disponibles")
    
        else : 
            print (ERROR + "ERR > " + cmd[0] + " : IA non valide")
            print (ERROR + "Tapez \"info IA\" pour obtenir les liste des IA disponibles")

def cmd_discuter (cmd, list_of_characters, msg) :
    if len (cmd) != 2 :
        print (ERROR + "ERR > Usage : cmd discuter <IA1> <IA2>")
    else :
        if cmd[0] in list_of_characters :
            msg.characters.append(cmd[0])

            if cmd[1] in list_of_characters :
                msg.characters.append(cmd[1])

                return msg
            else :
                print (ERROR + "ERR > " + cmd[1] + " : IA non valide")
                print (ERROR + "Tapez \"info IA\" pour obtenir les liste des IA disponibles")
    
        else : 
            print (ERROR + "ERR > " + cmd[0] + " : IA non valide")
            print (ERROR + "Tapez \"info IA\" pour obtenir les liste des IA disponibles")

# GESTIONS : TYPE CMD

def show_help () :
    print ("\nUNITHON - help : ")
    print ("USAGE : TYPE ACTION [PARAM_1 PARAM_2]")

    show_help_type ()
    show_help_cmd ()
    show_help_sys ()
    show_help_info ()


def show_help_type () :
    print ("\n1. LES TYPES (help type) :")
    print (" - cmd permet d'envoyer une commande a une IA")
    print (" - sys permet d'utiliser une commande systeme")
    print (" - info permet d'obtenir des informations sur l'etat du monde")


def show_help_cmd () :
    print ("\n2. CMD (help cmd) :")
    print (" - Pour deplacer une IA vers une autre IA")
    print (" > cmd deplacer IA1 IA2")
    print (" - Pour deplacer une IA vers une region")
    print (" > cmd deplacer IA region")
    print (" - Pour faire discuter deux IA entre elles")
    print (" > cmd discuter IA1 IA2")


def show_help_sys () :
    print ("\n3. SYS (help sys) :")
    print (" - Pour sortir de l'application")
    print (" > sys exit")


def show_help_info () :
    print ("\n4. INFO (help info) :")
    print (" - Pour obtenir la liste des IA disponibles")
    print (" > info IA")
    print (" - Pour obtenir la liste des regions disponibles")
    print (" > info regions")