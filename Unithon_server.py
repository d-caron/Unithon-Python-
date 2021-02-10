import threading

import Comm

def wait_msg (connexion) :
    # 1 - Attente du 1er message
    msg = Comm.rcv_message (connexion)
    
    # 2 - Affichage du message reçu
    print ("\nUnity sent >> " + msg)
        

def launch_server () :
    # Initialitsation de la connexion
    connexion = Comm.init_connexion ()

    threading.Thread (target=wait_msg, args=(connexion,)).start()
    
    print ("I'm waiting a message from Unity client")
    print ("During this time, you can send a message to the Unity client")
    msg = input ("Please, type your message : ")

    Comm.send_message (connexion, msg)

if __name__ == "__main__" :
    launch_server ()