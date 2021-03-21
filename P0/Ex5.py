import Seq0

"""Implement the seq_count(seq) function, that calculates the number of times all the bases appears on the sequence. 
It returns a dictionary with all the information. The keys of the dictionary are the bases: 'A', 'T', 'C' and 'G'.

It similar to the exercise 4, but what is printed on the console is the dictionary returned by the seq_count() function"""

GENE_FOLDER = './sequences/'

gene_list =['U5' , 'ADA', 'FRAT1', 'FXN']

print('--------- | Exercise 5 | ---------')

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + '.txt') #Va leyendo cada lista de genes
    print('Gene', gene, ':', Seq0.seq_count(sequence)) #printea un dict con el numero de bases de cada gen