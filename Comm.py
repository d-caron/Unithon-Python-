from socket import *

import sys
# Initialise la connexion avec le client Unity
# -> Retourne la socket du client

def init_connexion () :

    sock = socket (AF_INET, SOCK_STREAM)
    sock.bind (('localhost', 1024))  # Choix du port arbitraire
    sock.listen (1)                # Ecoute d'1 seul client
    client_socket, client_address = sock.accept ()

    return client_socket

# -> Retourne le message reçu du client au format "string"
def rcv_message (client_socket) :
    try:
        msg = client_socket.recv (1024).decode ()
        print(msg)
        return msg
    except:
        print("Close_Unity")
        return "Close_Unity"


# <- message : au format string
# Envois un message au client au format "bytes"
def send_message (client_socket, message) :
    client_socket.send (bytes(message, "utf-8"))

# Ferme la connexion avec le client
def close_connexion (client_socket) :
    client_socket.close ()
    
    # Force la fermeture du script
    sys.exit(0)