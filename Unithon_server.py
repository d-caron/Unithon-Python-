import threading
import Comm
import sys, os
import time
import Interpreter
import json
import Msg_manager

list_of_characters = []
list_of_regions = []
list_of_worlds = []


def wait_msg (connexion) :
    """
    @do :       Attend un message en boucle sur la connexion passe en 
                parametre et l'envoi au gestionnaire de message. 
                Gere aussi l'extinction du serveur si elle est demande 
                ou s'il y a une erreur.
    @args :     connexion -> Connection qu'il faut ecouter
    @return :   None
    """

    socket_is_open = True

    while socket_is_open :

        # Attente d'un message
        dao = Comm.rcv_message (connexion)
        action = Msg_manager.recv_handler (dao, list_of_characters, list_of_regions, list_of_worlds)

        # ACTION : Fermeture de l'application
        if (action == "exit"):
            print ("Demande d'extinction du server\n", flush=True)
            socket_is_open = False
            Comm.close_connexion(connexion)

            os._exit(1)

        # ACTION : Plantage de l'application
        elif (action == "error"):
            print("Erreur : Fermeture du serveur\n", flush=True)
            socket_is_open = False
            Comm.close_connexion(connexion)

            os._exit(1)
           

def launch_server () :
    """
    @do :       Lance le serveur python Unithon et envoi les commandes
                saisies par l'utilisateur a l'interpreteur de commande
                puis au client Unity, si elles sont correctes.
    @args :     None
    @return :   None
    """

    # Message d'ouverture du serveur
    print ("Lancement du serveur Unithon.", flush=True)
    print ("Tentative de connection au client...", flush=True)
    
    # Variable qui indique si le programme doit continuer ou non
    keep_running = True

    # Initialitsation de la connexion
    connexion = Comm.init_connexion ()
    threading.Thread (target=wait_msg, args=(connexion,)).start()

    print ("Connexion reussie, bienvenue sur UNITHON !", flush=True)
    print ("Pour obtenir de l'aide a propos de l'utilisation de ce service, tapez : \"help\".", flush=True)
    print ("Pour fermer le serveur, tapez : \"sys exit\".", flush=True)

    # Tant que le programme tourne
    while (keep_running) :        
        msg = input ("\nEntrez votre commande ici : ")

        dao = Interpreter.command_interpreter(msg, list_of_characters, list_of_regions, list_of_worlds)
        if dao != None :
            dao_str = dao.serialize ()
            Comm.send_message (connexion, dao_str)
            print (">>> Commande envoyée avec succes ! :)")        


if __name__ == "__main__" :
    launch_server ()