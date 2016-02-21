__author__ = 'Tomas'
import socket

from controllers.process import ProcessServer
import time

HOST = "192.168.0.4"  #socket.gethostname()
PORT = 65534

print("Ip server ", HOST)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((HOST, PORT))

serversocket.listen(1)

while True:
        clientsocket,addr = serversocket.accept()

        print("Conectado con", addr)

        server = ProcessServer(clientsocket)
        server.startRun()

        print("Hilos en corriendo del Cliente", addr)
