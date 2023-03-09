import socket

class Client():
    def __init__(self, host, port):
        self._HOST = host
        self._PORT = port
        
    def send(self, msg):
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client.connect((self._HOST, self._PORT))
        message = msg.encode()
        self.__client.send(message) 
        response = self.__client.recv(1024).decode()
        self.__client.close()
        return response
