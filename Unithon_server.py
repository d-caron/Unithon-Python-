import threading
import Comm
import sys, os
import time
import Interpreter
import json
import DAO
import Msg_manager

listOfCharacters = []
listOfRegions = []

def wait_msg (connexion) :

    socketIsOpen = True

    while socketIsOpen :

        # Attente d'un message
        dao = Comm.rcv_message (connexion)
        action = Msg_manager.recv_handler (dao, listOfCharacters, listOfRegions)
        print ("characters")
        print (listOfCharacters)


        # ACTION : Fermeture de l'application
        if (action == "exit"):
            print ("Fermeture du serveur\n", flush=True)
            socketIsOpen = False
            Comm.close_connexion(connexion)

            # Fermeture de l'application (thread + main) de façon brutal
            os._exit(1)

        # ACTION : Plantage de l'application
        elif (action == "error"):
            print("Fermeture du serveur pour cause de plantage Unity\n", flush=True)
            socketIsOpen = False
            Comm.close_connexion(connexion)

            # Fermeture de l'application (thread + main) de façon brutal
            os._exit(1)
                

        # Affichage du message reçu
        print ("\nUnity envoie >> " + dao.serialize ())

        # Proposer de répondre
        print ("Entrez votre message ici : ", end='', flush=True)
            

def launch_server () :
    print ("Lancement du serveur Python", flush=True)
    print ("Vous pouvez ecrire \"exit\" pour quitter le serveur", flush=True)
    
    # Variable qui indique si le programme doit continuer ou non
    keepRunning = True

    # Initialitsation de la connexion
    connexion = Comm.init_connexion ()
    threading.Thread (target=wait_msg, args=(connexion,)).start()
    
    

    print ("En attente d'un message de Unity")
    print ("Pendant ce temps, vous pouvez envoyer un message a Unity")

    while (keepRunning) :
        # try pour savoir si la socket est toujours open sinon on quitte le script
        
        msg = input ("Entrez votre message ici : ")

        # Si on tappe "reset" on relance la connexion et le thread 
        # if (msg == "reset") :
        #     connexion = Comm.init_connexion ()
        #     threading.Thread (target=wait_msg, args=(connexion,)).start()

        dao = Interpreter.command_interpreter(msg, listOfCharacters, listOfRegions)
        if dao != None :
            dao_str = dao.serialize ()
            print (dao_str)
            Comm.send_message (connexion, dao_str)        

if __name__ == "__main__" :
    launch_server ()
    