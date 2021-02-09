from socket import *

# Initialise la connexion avec le client Unity
# -> Retourne la socket du client
def init_connexion () :
    sock = socket (AF_INET, SOCK_STREAM)
    sock.bind (('localhost', 81))  # Choix du port arbitraire
    sock.listen (1)                # Ecoute d'1 seul client
    client_socket, client_address = sock.accept ()

    return client_socket

# -> Retourne le message reçu du client au format string
def rcv_message (client_socket) :
    return client_socket.recv (1024).decode ()

# Ferme la connexion avec le client
def close_connexion (client_socket) :
    client_socket.close ()
    print ("sock : connexion closed.")