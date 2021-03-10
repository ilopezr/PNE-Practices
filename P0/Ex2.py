import P0.Seq0 as Seq0

FOLDER = './sequences/' #Un solo punto significa dentro de la carpeta en el que tenemos este archivo, dos puntos significan dentro de PNE PRACTICES (la carpeta padre del anterior), y asi...
ID = 'ADA.txt'

U5_Seq = Seq0.seq_read_fasta(FOLDER + ID) #Quita la primera línea de código
print('The first 20 bases are: ', U5_Seq[0:20]) #La letra de la posicion 20 es la 21, porque la letra de la posicion 0 es la 1
