import json
from .response import Response

class Main:
    def __init__(self, server):
        users = {}
        self.server = server
        self.load_users()
    
    def load_users(self):
        with open('C:/Users/otavi/OneDrive/Ambiente de Trabalho/trabalho/server/database/users.json', 'r') as file:
            if not file:
                file.create_file()
            self.users = json.load(file)
    
    def save_users(self):
        with open('C:/Users/otavi/OneDrive/Ambiente de Trabalho/trabalho/server/database/users.json', 'w') as file:
            json.dump(self.users, file)
    
    def signup(self, email, password):
        self.users[email] = {'Password': password, 'Messages': []}
        self.save_users()
        return Response('Success', 'Registration successful.')
    
    def login(self, email, password):
        if email not in self.users:
            return Response(type='Error', message='Email not found.')
        elif password != self.users[email]['Password']:
            return Response(type='Error', message='Incorrect password.')
        elif password == self.users[email]['Password']:
            return Response(type='Success', message='Login successful.')
