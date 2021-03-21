#Hemos hecho otro server pero hemos cambiado el port de uno porque dos servers no pueden estar en el mismo port

"""Write a python program that takes 10 fragments of 10 bases each from the FRAT1
gene and sends them to two servers.
The odd segments (1,3,5,7 and 9) should be sent to server 1,
and the even segments (2,4,6,8 and 10) to server 2.
The client should print on the console all the fragments"""

from client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

#Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 12000
PORT_2 = 12700


c = Client(IP, PORT) #conexión con el server 1
c_2 = Client(IP, PORT_2) #conexion con el server 2

s = Seq() #Creamos un object donde se almacenaran las instances
s.seq_read_fasta('U5.txt') #Leer un fasta quitandole la primera linea y almacenandolo en s.strbases

count = 0
i = 0
while i < len(s.strbases) and count < 10:
    fragment = s.strbases[i: i+10]
    count += 1
    i += 10
    print('Fragment', count, ':', fragment)
    if count % 2 == 0: #Si el modulo es par lo enviamos al server 2
        print(c_2.talk('Fragment' + str(count) + ':' + fragment))
    else: #Si el modulo es impar lo enviamos al server1
        print(c.talk('Fragment' + str(count) + ':' + fragment))
