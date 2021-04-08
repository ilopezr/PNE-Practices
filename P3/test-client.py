from client0 import Client

# SERVER IP, PORT
PORT = 8080 #El port no tiene que ser usado por ninguna aplicación más
IP = "localhost"

client = Client(IP, PORT)
msg = input('Enter here the message: ')
client.talk(msg)

