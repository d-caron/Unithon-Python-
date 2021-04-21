ERROR = "/!\\ "

def script_handler (script_name) :
    """
    @do :       Ouvre le script et renvoi la liste des commandes contenu 
                dans le script
    @args :     String script_name -> Nom du script
    @return :   String -> liste des commandes
    """
    try :
        script = open (script_name, 'r')

    except FileNotFoundError :
        print (ERROR + "ERR > le fichier " + script_name + " est introuvable.")

    except :
        print (ERROR + "ERR > Une erreur innatendu s'est produite lors de la lecture de " + script_name)

    else :
        script.seek (0)
        cmd_list = script.readlines ()
        cmd_list = [cmd.removesuffix ("\n") for cmd in cmd_list if cmd[0] != "#" and cmd[0] != "\n"]
        script.close ()

        return cmd_list

    return None   