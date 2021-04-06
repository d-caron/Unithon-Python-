from socket import *
import DAO

import sys


def init_connexion () :
    """
    @do :       Initialise la connexion avec le client Unity
    @args :     None
    @return :   Socket -> socket du client
    """

    print ("\n4. INFO (help info) :")
    print (" - Pour obtenir la liste des IA disponibles")
    print (" > info IA")
    print (" - Pour obtenir la liste des regions disponibles")
    print (" > info regions")

    sock = socket (AF_INET, SOCK_STREAM)
    sock.bind (('localhost', 1024))     # Choix du port arbitraire
    sock.listen (1)                     # Ecoute d'1 seul client
    client_socket, client_address = sock.accept ()

    return client_socket


def rcv_message (client_socket) :
    """
    @do :       Ecoute la socket et transforme les message reçu en DAO
    @args :     Socket client_socket -> socket du client
    @return :   DAO -> message reçu
    """

    dao = DAO.DAO ()

    try:
        msg = client_socket.recv (1024).decode ()
        return dao.deserialize (msg)
    except:
        # Si erreur : Socket ferme
        # alors on simule la reception du message "sys exit"
        dao.type = "sys"
        dao.action = "exit"
        return dao


def send_message (client_socket, message) :
    """
    @do :       Envois un message au client au format "bytes"
    @args :     Socket client_socket -> socket du client
                String message -> message a envoyer
    @return :   None
    """
    
    client_socket.send (bytes(message, encoding="utf-8"))


def close_connexion (client_socket) :
    """
    @do :       Ferme la connexion avec le client
    @args :     Socket client_socket -> socket du client
    @return :   None
    """
    
    try:
        send_message(client_socket, "Close_Python")
        print("Fermeture de la socket")
        client_socket.close ()
        
        sys.exit(0)
    except:
        # Si deja ferme, on ne fait rien
        return