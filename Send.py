import socket
import sys
import json

UDP_IP = "127.0.0.1"
UDP_PORT = 80
#MESSAGE_JSON = {"name": "chacal", "voiture":"Dacia"}
#MESSAGE = json.dumps(MESSAGE_JSON)
MESSAGE = b"George"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

try:
    # Connect to server and send data
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    #sock.connect((UDP_IP, UDP_PORT))
    #sock.sendall(bytes(MESSAGE, encoding="utf-8"))

finally:
    sock.close()