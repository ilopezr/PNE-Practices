from client0 import Client

PRACTICE = 2
EXERCISE = 1
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

#Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 12000

#Create a client object
c = Client(IP, PORT)

#Test the ping method
c.advanced_ping()
c.ping()

#Print the IP and PORTs
print(f"IP: {c.ip}, {c.port}")