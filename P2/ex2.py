from client0 import Client

PRACTICE = 2
EXERCISE = 2
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

#Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 12000

#Create a client object
c = Client(IP, PORT)

#Print the IP and PORTs
print(c)