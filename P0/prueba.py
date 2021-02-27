i = {'A':2, 'E':3}
print(list(i)[1][0])


print(sorted(i))

import Seq0
from pathlib import Path

GENE_FOLDER = './sequences/'
gene_list =['U5' , 'ADA', 'FRAT1', 'FXN']

print('--------- | Exercise 8 | ---------')
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + '.txt') #Leemos la sequencia del gen sin su primera línea

    A, C, G, T = sequence.count('A'), sequence.count('C'), sequence.count('G') , sequence.count('T')

    if A >= C and A  >= G and A >= T:
        print('Gene ', gene, ': Most frequent Base: A')
    if C >= A and C >= G and C >= T:
        print('Gene ', gene, ': Most frequent Base: C')
    if G >= A and G >= C and G >=T:
        print('Gene ', gene, ': Most frequent Base: G')
    if T >= A and T >= C and T >=G:
        print('Gene ', gene, ': Most frequent Base: T') #I put in all of them if and not elif, just because if there`s a tie