from menu import *
from client import Client

client = Client('localhost', 7777)

print(f'\033[;1m{"-"*10 + " Welcome " + "-"*10 + "":^50}\033[m')

while True: 
    MenuLogin()
    op = str(input('\nSelect a option: '))

    match op:
        case '1': # Login
            email = str(input('Type your email: ')).lower()
            password = str(input('Type your password: '))
            res = client.send(f'login/{email}/{password}/false/false/false/false')
            expected = '\033[1;32mLogin successful.\033[m'

            if res == expected:
                print(res)
                while True: 
                    MenuMain()
                    op_main = str(input('\nSelect a option: '))
                    match op_main:
                        case '1': # Mailbox
                            print(f'\033[;1m{"-"*10 + " Mailbox " + "-"*10 + "":^50}\033[m')
                            print(client.send(f'mailbox/{email}/false/false/false/false/false'))

                        case '2': # Open email
                            print(f'\033[;1m{"-"*10 + " Open Email " + "-"*10 + "":^50}\033[m')
                            res = client.send(f'mailbox/{email}/false/false/false/false/false')
                            print(res)
                            if(res != '\033[;1m\033[1;31mYou have no messages.\033[m'):
                                id_msg = int(input('Type email index: '))
                                print(client.send(f'open/{email}/false/{id_msg-1}/false/false/false'))

                        case '3': # Send email
                            print(f'\033[;1m{"-"*10 + " Send Email " + "-"*10 + "":^50}\033[m')
                            rcv = str(input('Type receiver email: ')).lower()
                            subject = str(input('Type subject: '))
                            body = str(input('Type email body: '))
                            print(client.send(f'send/{email}/false/false/{subject}/{body}/{rcv}'))

                        case '4': # Delete email
                            print(f'\033[;1m{"-"*10 + " Delete Email " + "-"*10 + "":^50}\033[m')
                            res = client.send(f'mailbox/{email}/false/false/false/false/false')
                            print(res)
                            if(res != '\033[;1m\033[1;31mYou have no messages.\033[m'):
                                id_msg = int(input('Type email index: '))
                                print(client.send(f'delete/{email}/false/{id_msg-1}/false/false/false'))
                        
                        case '5': # Clear mailbox
                            print(f'\033[;1m{"-"*10 + " Clear Mailbox " + "-"*10 + "":^50}\033[m')
                            print(client.send(f'clear/{email}/false/false/false/false/false'))
                        
                        case '6': # Quit
                            print(client.send(f'quit/{email}/false/false/false/false/false'))
                            break
                        
                        case other:
                            print("Please type a valid option.")
            
            else:
                print("Email or password incorrect.")
        
        case '2': # Signup
            email = str(input('Type your email: ')).lower()
            password = str(input('Type your password: '))
            print(client.send(f'signup/{email}/{password}/false/false/false/false'))