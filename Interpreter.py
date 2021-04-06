from DAO import DAO
from Script_handler import script_handler

ERROR = "/!\\ "


def command_interpreter(message, characters, regions): 
    """
    @do :       L'interpreteur de commande deconstruit le message pour
                l'interpreter et le transformer en DAO si besoin.
    @args :     String message -> commande a interpreter
                String[] characters -> liste de IA disponibles
                String[] regions -> liste des regions disponibles
    @return :   DAO -> commande interprete au format DAO si correcte
                None -> si incorrecte
    """
    
    list_of_characters = characters
    list_of_regions = regions
    
    params = message.split(' ')
    msg = build_msg (params, list_of_characters, list_of_regions)

    return msg


def build_msg(params, list_of_characters, list_of_regions):
    """
    @do :       Interprete la liste de parametre de la commande
    @args :     String[] params -> liste des termes de la commande
                String[] characters -> liste de IA disponibles
                String[] regions -> liste des regions disponibles
    @return :   DAO -> message DAO si la commande est correcte
                None -> si incorrecte ou DAO non necessaire
    """

    msg = DAO ()
    msg.type = params[0]

    if len(params) > 1 :
        if msg.type == "cmd" :
            dao = cmd_handler (params[1:], list_of_characters, list_of_regions, msg)
            return [dao]

        elif msg.type == "sys" :
            dao = sys_handler (params[1:], msg)
            return [dao]

        elif msg.type == "info" :
            info_handler (params[1:], list_of_characters, list_of_regions)
            return None

        elif msg.type == "run" :
            dao_list = run_handler (params[1], list_of_characters, list_of_regions)
            return dao_list

        elif msg.type == "help" :
            if params[1] == "type" :
                show_help_type ()
            elif params[1] == "cmd" :
                show_help_cmd ()
            elif params[1] == "sys" :
                show_help_sys ()
            elif params[1] == "info" :
                show_help_info ()

        else :
            print (ERROR + "ERR > " + params[0] + " : Type invalide.")
            print (ERROR + "Tapez \"help\" pour plus d'information")

    else :
        if msg.type == "help" :
            show_help ()
                
        else :
            print (ERROR + "ERR > Pas d'action renseignee")
            print (ERROR + "Tapez \"help\" pour plus d'information")


# GESTION DES COMMANDES


def cmd_handler (params, list_of_characters, list_of_regions, msg) :
    """
    @do :       Gère les commandes de type CMD
    @args :     String[] params -> liste des termes de la commande
                String[] list_of_characters 
                    -> liste de IA disponibles
                String[] list_of_regions 
                    -> liste des regions disponibles
                DAO msg -> DAO en construction
    @return :   DAO -> message DAO si la commande est correcte
                None -> si incorrecte
    """

    msg.action = params[0]

    if msg.action == "deplacer" :
        return cmd_deplacer (params[1:], list_of_characters, list_of_regions, msg)
        
    elif msg.action == "discuter" :
        return cmd_discuter (params[1:], list_of_characters, msg)

    print (ERROR + "ERR > " + params[0] + " : Action invalide")
    print (ERROR + "Tapez \"help\" pour plus d'information")


def sys_handler (params, msg) :
    """
    @do :       Gère les commandes de type SYS
    @args :     String[] params -> liste des termes de la commande
                DAO msg -> DAO en construction
    @return :   DAO -> message DAO si la commande est correcte
                None -> si incorrecte
    """

    msg.action = params[0]

    if msg.action == "exit" :
        return msg

    print (ERROR + "ERR > " + params[0] + " : Action invalide")
    print (ERROR + "Tapez \"help\" pour plus d'information")


def info_handler (params, list_of_characters, list_of_regions) :
    """
    @do :       Gère les commandes de type INFO
    @args :     String[] params -> liste des termes de la commande
                String[] list_of_characters 
                    -> liste de IA disponibles
                String[] list_of_regions 
                    -> liste des regions disponibles
    @return :   None
    """

    if params[0] == "IA" :
        print (list_of_characters)
    
    elif params[0] == "regions" :
        print (list_of_regions)

    else : 
        print (ERROR + "ERR > " + params[0] + " : Action invalide")
        print (ERROR + "Tapez \"help\" pour plus d'information")


def run_handler (script, list_of_characters, list_of_regions) :
    """
    @do :       Gère les commandes de type RUN
    @args :     String[] script -> nom du script
                String[] list_of_characters 
                    -> liste de IA disponibles
                String[] list_of_regions 
                    -> liste des regions disponibles
    @return :   DAO [] -> Liste des DAO correspondants aux commandes a
                l'interieur du script
    """

    cmd_list = script_handler (script)
    return [
        command_interpreter (cmd, list_of_characters, list_of_regions)[0] 
        for cmd in cmd_list
    ]


# GESTIONS : TYPE CMD


def cmd_deplacer (params, list_of_characters, list_of_regions, msg) :
    """
    @do :       Gère l'action deplacer
    @args :     String[] params -> liste des termes de la commande
                String[] list_of_characters 
                    -> liste de IA disponibles
                String[] list_of_regions 
                    -> liste des regions disponibles
                DAO msg -> DAO en construction
    @return :   DAO -> message DAO si la commande est correcte
                None -> si incorrecte
    """

    if len (params) != 2 :
        print (ERROR + "ERR > Usage : cmd deplacer <IA1> <IA2>|<region>")
    else :
        if params[0] in list_of_characters :
            msg.characters.append(params[0])

            if params[1] in list_of_characters :
                msg.characters.append(params[1])

                return msg

            elif params[1] in list_of_regions :
                msg.world.regions.append (params[1])

                return msg
            else :
                print (ERROR + "ERR > " + params[1] + " : Destination non valide")
                print (ERROR + "Tapez \"info IA\" ou \"info regions\" pour obtenir les liste des destinations disponibles")
    
        else : 
            print (ERROR + "ERR > " + params[0] + " : IA non valide")
            print (ERROR + "Tapez \"info IA\" pour obtenir les liste des IA disponibles")


def cmd_discuter (params, list_of_characters, msg) :
    """
    @do :       Gère l'action discuter
    @args :     String[] params -> liste des termes de la commande
                String[] list_of_characters 
                    -> liste de IA disponibles
                String[] list_of_regions 
                    -> liste des regions disponibles
                DAO msg -> DAO en construction
    @return :   DAO -> message DAO si la commande est correcte
                None -> si incorrecte
    """

    if len (params) != 2 :
        print (ERROR + "ERR > Usage : cmd discuter <IA1> <IA2>")
    else :
        if params[0] in list_of_characters :
            msg.characters.append(params[0])

            if params[1] in list_of_characters :
                msg.characters.append(params[1])

                return msg
            else :
                print (ERROR + "ERR > " + params[1] + " : IA non valide")
                print (ERROR + "Tapez \"info IA\" pour obtenir les liste des IA disponibles")
    
        else : 
            print (ERROR + "ERR > " + params[0] + " : IA non valide")
            print (ERROR + "Tapez \"info IA\" pour obtenir les liste des IA disponibles")


# GESTIONS : TYPE HELP


def show_help () :
    """
    @do :       Affiche l'aide generale
    @args :     None
    @return :   None
    """

    print ("\nUNITHON - help : ")
    print ("USAGE : TYPE ACTION [PARAM_1 PARAM_2]")

    show_help_type ()
    show_help_cmd ()
    show_help_sys ()
    show_help_info ()
    show_help_run ()


def show_help_type () :
    """
    @do :       Affiche la categorie d'aide : TYPE
    @args :     None
    @return :   None
    """

    print ("\n1. LES TYPES (help type) :")
    print (" - cmd permet d'envoyer une commande a une IA")
    print (" - sys permet d'utiliser une commande systeme")
    print (" - info permet d'obtenir des informations sur l'etat du monde")
    print (" - run permet de lire un script de commande")


def show_help_cmd () :
    """
    @do :       Affiche la categorie d'aide : CMD
    @args :     None
    @return :   None
    """

    print ("\n2. CMD (help cmd) :")
    print (" - Pour deplacer une IA vers une autre IA")
    print (" > cmd deplacer <IA1> <IA2>")
    print (" - Pour deplacer une IA vers une region")
    print (" > cmd deplacer <IA> <region>")
    print (" - Pour faire discuter deux IA entre elles")
    print (" > cmd discuter <IA1> <IA2>")


def show_help_sys () :
    """
    @do :       Affiche la categorie d'aide : SYS
    @args :     None
    @return :   None
    """

    print ("\n3. SYS (help sys) :")
    print (" - Pour sortir de l'application")
    print (" > sys exit")


def show_help_info () :
    """
    @do :       Affiche la categorie d'aide : INFO
    @args :     None
    @return :   None
    """

    print ("\n4. INFO (help info) :")
    print (" - Pour obtenir la liste des IA disponibles")
    print (" > info IA")
    print (" - Pour obtenir la liste des regions disponibles")
    print (" > info regions")


def show_help_run () :
    """
    @do :       Affiche la categorie d'aide : RUN
    @args :     None
    @return :   None
    """

    print ("\n5. RUN (help run) :")
    print (" - Pour lancer un script")
    print (" > run <SCRIPT>")