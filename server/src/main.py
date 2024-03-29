import json
from .response import Response

class Main:
    def __init__(self, server):
        users = {}
        self.server = server
        self.load_users()
    
    def load_users(self): # Load users from json
        with open('C:/Users/otavi/OneDrive/Ambiente de Trabalho/trabalho/server/database/users.json', 'r') as file:
            if not file:
                file.create_file()
            self.users = json.load(file)
    
    def save_users(self): # Dump users to json
        with open('C:/Users/otavi/OneDrive/Ambiente de Trabalho/trabalho/server/database/users.json', 'w') as file:
            json.dump(self.users, file)
    
    def signup(self, email, password): # Signup
        self.users[email] = {'Password': password, 'Emails': []}
        self.save_users()
        return Response('Success', 'Registration successful.')
    
    def login(self, email, password): # Login 
        if email not in self.users: # Check if email exists
            return Response(type='Error', message='Email not found.')
        elif password != self.users[email]['Password']: # Check if the password match
            return Response(type='Error', message='Incorrect password.')
        elif password == self.users[email]['Password']:
            return Response(type='Success', message='Login successful.')
    
    def mailbox(self, email): # Mailbox
        if self.users[email]['Emails'] == []: # Check if there are emails 
            return Response(type='Error', message='You have no messages.')
        data = ''
        for i in range(len(self.users[email]['Emails'])):
            data += (f'{i+1} - Subject: {self.users[email]["Emails"][i]["Subject"]}\n')
        return Response(type='Success', message='', data=data)
    
    def send(self, sender, rcv, subject, body): # Send email
        if rcv not in self.users: # Check if the receiver exists
            return Response(type='Error', message='Invalid receiver.')
        self.users[rcv]['Emails'].append({'From': str(sender), 'Subject': str(subject), 'Body': str(body)})
        self.save_users()
        return Response(type='Success', message='Email sent successfully.')
    
    def open(self, email, id_msg): # Open email
        if not self.users[email]['Emails']: # Check if there are emails
            return Response(type='Error', message='You have no messages.')
        if int(id_msg) >= len(self.users[email]['Emails']):
            return Response(type='Error', message='You have no message with that index.')
        return Response(type='Success', message='', data=
        f'From: {self.users[email]["Emails"][int(id_msg)]["From"]}\n'
        f'Subject: {self.users[email]["Emails"][int(id_msg)]["Subject"]}\n'
        f'Body: {self.users[email]["Emails"][int(id_msg)]["Body"]}')
    
    def delete(self, email, id_msg): # Delete email
        if not self.users[email]['Emails']: # Check if there are emails
            return Response(type='Error', message='You have no messages.')
        if int(id_msg) >= len(self.users[email]['Emails']):
            return Response(type='Error', message='You have no message with that index.')
        self.users[email]['Emails'].pop(int(id_msg))
        self.save_users()
        return Response(type='Success', message='Email deleted successfully.')
    
    def clear(self, email): # Clear mailbox
        if not self.users[email]['Emails']: # Check if there are emails
            return Response(type='Error', message='You have no messages.')
        self.users[email]['Emails'] = []
        self.save_users()
        return Response(type='Success', message='Mailbox cleared.')