from menu import *
from client import Client

client = Client('localhost', 7777)

print(f'\033[;1m{"-"*30 + "Welcome" + "-"*30 + "":^50}\033[m')

while True: 
    MenuLogin()
    op = str(input('\nSelect a option: '))

    match op:
        case '1':
            email = str(input('Type your email: ')).lower()
            password = str(input('Type your password: '))
            res = client.send(f'login/{email}/{password}/false/false/false/false')
            expected = '\033[1;32mLogin successful.\033[m'

            if res == expected:
                print(res)
                print("Bem vindo!")

                while True: 
                    MenuMaster()
                    op_master = str(input('\nSelect a option: '))
            
            else:
                print("Email or password incorrect.")
        
        case '2': 
            email = str(input('Type your email: ')).lower()
            password = str(input('Type your password: '))
            print(client.send(f'signup/{email}/{password}/false/false/false/false'))