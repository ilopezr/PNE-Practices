import P0.Seq0 as Seq0 # o tambien si marcamos P0 como sources root, import Seq 0

"""Implement the seq_read_fasta(filename) function, que tiene que leer y almacenar y devolver el body de un archivo FASTA. 
The head is removed, as well as the '\n' characters. This function should be written in the  Seq0.py file. 

Write a python program for opening the U5.txt file and writing into the console the first 20 bases of the sequence"""

FOLDER = './sequences/' #Un solo punto significa dentro de la carpeta en el que tenemos este archivo, dos puntos significan dentro de PNE PRACTICES (la carpeta padre del anterior), y asi...
ID = 'ADA.txt'

U5_Seq = Seq0.seq_read_fasta(FOLDER + ID) #Quita la primera línea de código, almacena el body de un fasta y lo devuelve.
print('The first 20 bases are: ', U5_Seq[0:20])
