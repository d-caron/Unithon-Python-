import threading

import Comm

def wait_msg () :
    # 1 - Initialitsation de la connexion
    connexion = Comm.init_connexion ()

    # 2 - Attente du 1er message
    msg = Comm.rcv_message (connexion)
    
    # 3 - Affichage du message reçu
    print ("Unity sent >> " + msg)

    # 4 - Fermeture de la connexion
    Comm.close_connexion (connexion)
        

def launch_server () :
    threading.Thread (target=wait_msg).start()
    print ("I'm waiting a message from Unity client but I can write here while I'm waiting !")

if __name__ == "__main__" :
    launch_server ()