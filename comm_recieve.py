from socket import *

def init_connexion () :
    connexion = socket (AF_INET, SOCK_STREAM)
    connexion.bind (('localhost', 81))
    connexion.listen (1)
    client_socket, client_address = connexion.accept ()
    return client_socket

def rcv_message (connexion) :
    return connexion.recv (1024).decode ()

def close_connexion (connexion) :
    connexion.close ()
    print ("sock : connexion closed.")

if __name__=="__main__":
    connexion = init_connexion ()
    msg = rcv_message (connexion)
    print (">> " + msg)
    close_connexion (connexion)