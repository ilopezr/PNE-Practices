import Seq0

"""Implement the seq_count_base(seq, base) function, que calcula el número de veces que aparece cada base en una cadena.
Write a python program for calculating the number of each bases located on each of the five genes"""


GENE_FOLDER = './sequences/'

gene_list =['U5' , 'ADA', 'FRAT1', 'FXN']
base_list = ['A', 'C', 'T','G']

print('--------- | Exercise 4 | ---------')

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + '.txt') #Quitamos la primera línea del gen
    print('Gene', gene)  #Indicamos qué gen estamos leyendo
    for base in base_list: #Bucle, número de veces que aparece cada base en *cada secuencia*
        print(base, ':', Seq0.seq_count_base(sequence, base))
