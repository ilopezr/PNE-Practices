from client0 import Client
from pathlib import Path
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

#Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)

s = Seq() #Crea una null sequence - objeto, dentro del objeto se guardan .strbases y lo que haya en el innit
s.seq_read_fasta('../Session-04/FRAT1.txt') #usa un method de esa class, y lo que hace es leer un archivo FASTA quitandole la primera línea

count = 0
i = 0


while i < len(s.strbases) and count < 5:
    fragment = s.strbases[i: i+10] #cogemos 10 bases
    count += 1
    i += 10
    print('Fragment', count, ':', fragment)
    print(c.talk(fragment)) #Para mandar los fragmentos al server
    #Dentro del loop que si no solo vamos a mandar el ult fragment