import Seq0

"""Implement the seq_reverse(seq) function, that calculates the reverse of the given sequence. 
Imaging we have this sequence: "ATTCG". Its reverse is: "GCTTA". It should be written in the Seq0.py file

Write a python program for creating a new fragment composed of the first 20 bases of the U5 gene. 
This fragment should be printed on the console. Then calculate the reverse of this fragment by calling the seq_reverse()
 function. Finally print it on the console"""

GENE_FOLDER = './sequences/'
FILENAME = 'U5.txt'

new_fragment = Seq0.seq_read_fasta(GENE_FOLDER + FILENAME)[0:20] #Leemos el archivo habiendole quitado la primera línea y la recortamos (20 primeras bases - 1)
#Ponemos [0:20] y no 21, porque la base de la posicion cero es la base una, y la base de la posicion 20 es la 21.

print('--------- | Exercise 6 | ---------')
print('Gene U5: ')
print('Frag: ', new_fragment)
print('Rev: ', Seq0.seq_reverse(new_fragment))