from client0 import Client
from pathlib import Path

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

#Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 12000


c = Client(IP, PORT)

print('Response:' , c.talk('Sending the U5 gene to the server...'))
print('From server:' , c.talk(Path('U5.txt').read_text())) #Leer el contenido de un FASTA FILE

