import threading
import Comm
import sys, os
import time
import Interpreter
import json
import DAO

def wait_msg (connexion) :

    socketIsOpen = True

    # Tant que la socket est ouverte on l'écoute
    while socketIsOpen :

        # 1 - Attente du 1er message
        receiveMsg = Comm.rcv_message (connexion)
        dao = DAO.DAO ()
        dao.deserialize (receiveMsg)


        # Si le message contient "Close_Unity", c'est que Unity c'est fermé alors on peut arrêter le serveur
        if (dao.type == "sys" and dao.action == "exit"):
            print ("Fermeture du serveur\n", flush=True)
            socketIsOpen = False
            Comm.close_connexion(connexion)

            # Fermeture de l'application (thread + main) de façon brutal
            os._exit(1)

        else :
            # Quand Unity perd la connexion sans avoir pu envoyer de message, Python boucle en pensant recevoir des chaines vides, si c'est le cas on ferme directement la connection
            if (dao == ""):
                print("Fermeture du serveur pour cause de plantage Unity\n", flush=True)
                socketIsOpen = False
                Comm.close_connexion(connexion)

                # Fermeture de l'application (thread + main) de façon brutal
                os._exit(1)
                
            else :
                # 2 - Affichage du message reçu
                print ("\nUnity envoie >> " + dao.serialize ())

                # 3 - Proposer de répondre
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

        dao = Interpreter.command_interpreter(msg)
        if dao != None :
            dao_str = dao.serialize ()
            print (dao_str)
            Comm.send_message (connexion, dao_str)        

if __name__ == "__main__" :
    launch_server ()
    