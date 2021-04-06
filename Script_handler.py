def script_handler (script_name) :
    """
    @do :       Ouvre le script et renvoi la liste des commandes contenu 
                dans le script
    @args :     String script_name -> Nom du script
    @return :   String -> liste des commandes
    """
    with open (script_name, 'r') as script :
        script.seek (0)
        cmd_list = script.readlines ()
        cmd_list = [cmd.removesuffix ("\n") for cmd in cmd_list if cmd[0] != "#" and cmd[0] != "\n"]
        
    return cmd_list