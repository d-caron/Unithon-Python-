from socket import *
import DAO

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
    dao = DAO.DAO ()

    try:
        return client_socket.recv (1024).decode ()
        return dao.deserialize (msg)
    except:
        # Si on a une erreur, c'est problablement parce que la socket est fermé, alors on simule la reception du message "Close_Unity"
        dao.type = "system"
        dao.action = "close"
        return dao


# <- message : au format string
# Envois un message au client au format "bytes"
def send_message (client_socket, message) :
    client_socket.send (bytes(message, encoding="utf-8"))
    #client_socket.sendall(bytes(message,encoding="utf-8"))


# Ferme la connexion avec le client
def close_connexion (client_socket) :
    try:
        send_message(client_socket, "Close_Python")
        print("Fermeture de la socket")
        client_socket.close ()
        # Force la fermeture du script
        sys.exit(0)
    except:
        # En ignore si la socket est déjà ferme
        return ""

#  Censé check si la connexion à la socket est fonctionnelle, mais renvoie False à chaque fois
# def checkConnection(client_socket) :
#     result = client_socket.connect_ex(('localhost', 1024))
#     if result == 0:
#         return True
#     else:
#         return False

