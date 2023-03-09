import socket
import threading
from .response import Response
from .main import Main
#from .client import Client

class Server():
    def __init__(self, host, port, domain):
        self.host = host
        self.port = port
        self.domain = domain
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
    
    def start(self):
        self.server.listen()
        print("Server started listening.")
        
        while True:
            connection, address = self.server.accept()
            thread = threading.Thread(target=self.connect(connection, address))
            thread.start()

    def connect(self, connection, address):
        while True:
            msg = connection.recv(1024)
            msg = msg.decode()
            msg = msg.split('/')

            cmd = msg[0]
            email = msg[1]
            password = msg[2]
            id_msg = msg[3]
            subject = msg[4]
            body = msg[5]
            rcv = msg[6]

            match cmd: 
                case 'signup':
                    print("here")
                    res = Main(self.domain).signup(email, password)
                    res = Response(res.type, res.message).value().encode()
                    connection.send(res)
                    break
                case 'login': 
                    res = Main(self.domain).login(email, password)
                    res = Response(res.type, res.message).value().encode()
                    connection.send(res)
                    break
        
        connection.close()