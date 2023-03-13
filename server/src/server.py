import socket
import threading
from .response import Response
from .main import Main

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
        while True: # Listening to clients
            connection, address = self.server.accept()
            thread = threading.Thread(target=self.connect(connection, address)) # Threads to listen to more than one client
            thread.start()

    def connect(self, connection, address):
        while True:
            msg = connection.recv(1024)
            msg = msg.decode()
            msg = msg.split('/')

            # Message format is: cmd/email/password/id_msg/subject/body/rcv

            cmd = msg[0]
            email = msg[1]
            password = msg[2]
            id_msg = msg[3]
            subject = msg[4]
            body = msg[5]
            rcv = msg[6]

            match cmd: 
                case 'signup':
                    res = Main(self.domain).signup(email, password) # Call main function 'signup'
                    res = Response(res.type, res.message).value().encode()
                    connection.send(res)
                    break
                case 'login': 
                    res = Main(self.domain).login(email, password)
                    res = Response(res.type, res.message).value().encode()
                    connection.send(res)
                    break
                case 'mailbox':
                    res = Main(self.domain).mailbox(email)
                    if res.type == 'Success':
                        res = Response(res.type, res.data).value().encode()
                    else: 
                        res = Response(res.type, res.message).value().encode()
                    connection.send(res)
                    break
                case 'send':
                    res = Main(self.domain).send(email, rcv, subject, body)
                    res = Response(res.type, res.message).value().encode()
                    connection.send(res)
                    break
                case 'open': 
                    res = Main(self.domain).open(email, id_msg)
                    if res.type == 'Success':
                        res = Response(res.type, res.data).value().encode()
                    else: 
                        res = Response(res.type, res.message).value().encode()
                    connection.send(res)
                    break
                case 'delete':
                    res = Main(self.domain).delete(email, id_msg)
                    res = Response(res.type, res.message).value().encode()
                    connection.send(res)
                    break
                case 'clear':
                    res = Main(self.domain).clear(email)
                    res = Response(res.type, res.message).value().encode()
                    connection.send(res)
                    break
                case 'quit':
                    connection.close()                    
                    break
        
        connection.close()