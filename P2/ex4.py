from client0 import Client
import termcolor
import colorama
colorama.init(strip='False')

PRACTICE = 2
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

#Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 12000

#Create a client object
c = Client(IP, PORT)

c.debug_talk("Message 1---")
c.debug_talk("Message 2: Testing !!!")