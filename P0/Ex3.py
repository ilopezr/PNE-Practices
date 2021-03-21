"""Implement the seq_len(seq) function, calcula el número de bases totales en la sequencia. It should be written in the
Seq0.py file. Write a python program for calculating the total length of the 5 Genes: U5, ADA, FRAT1, FXN and U5.
The program should call the seq_len() function"""


import Seq0

GENE_FOLDER = './sequences/'

gene_list =['U5' , 'ADA', 'FRAT1', 'FXN']

print('--------- | Exercise 3 | ---------')

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + '.txt') #Quitamos la primera línea del gen, almacenamos el body
    print('Gene', gene, '---> Length:', Seq0.seq_len(sequence)) #Calculamos la longitud del gen



