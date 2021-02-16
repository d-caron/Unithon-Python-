import threading
import Comm
import sys, os

def wait_msg (connexion) :

    socketIsOpen = True

    # Tant que la socket est ouverte on l'écoute
    while socketIsOpen :

        # 1 - Attente du 1er message
        msg = Comm.rcv_message (connexion)

        # Si le message contient "Close_Unity", c'est que Unity c'est fermé alors on peut arrêter le serveur
        if (msg == "Close_Unity"):
            print ("Fermeture du serveur")
            socketIsOpen = False
            Comm.close_connexion(connexion)

            # Fermeture de l'application (thread + main) de façon brutal
            os._exit(1)

        else :

            # 2 - Affichage du message reçu
            print ("\nUnity sent >> " + msg)

            # 3 - Proposer de répondre
            print ("Please, type your message: ", end='', flush=True)
            

def launch_server () :
    print ("Lancement du serveur Python")
    
    # Variable qui indique si le programme doit continuer ou non
    keepRunning = True

    # Initialitsation de la connexion
    connexion = Comm.init_connexion ()
    threading.Thread (target=wait_msg, args=(connexion,)).start()
    
    print ("I'm waiting a message from Unity client")
    print ("During this time, you can send a message to the Unity client")

    while (keepRunning) :
        # try pour savoir si la socket est toujours open sinon on quitte le script
        
        msg = input ("Please, type your message: ")

        # Si on tappe "reset" on relance la connexion et le thread 
        if (msg == "reset") :
            connexion = Comm.init_connexion ()
            threading.Thread (target=wait_msg, args=(connexion,)).start()

        # Si on tappe "exit" on ferme le programme
        elif (msg == "exit") :
            print("Sortie de l'application ")

            if (keepRunning) :
                keepRunning = False
                try :
                    Comm.send_message (connexion, "Close_Python")
                    Comm.close_connexion(connexion)
                except :
                    print ("Erreur : la socket n'est plus ouverte, taper \"reset\" si vous voulez la redemarrer ou \"exit\" pour quitter")
            sys.exit(0)


        # Sinon on envoie le message
        else :
            try :
                Comm.send_message (connexion, msg)
            except :
                print ("Erreur : la socket n'est plus ouverte, taper \"reset\" si vous voulez la redemarrer ou \"exit\" pour quitter")

        

if __name__ == "__main__" :
    launch_server ()