import Seq0
from pathlib import Path

GENE_FOLDER = './sequences/'
FILENAME = 'U5.txt'

new_fragment = Seq0.seq_read_fasta(GENE_FOLDER + FILENAME)
new_fragment = new_fragment[0:20]
print(new_fragment)

print('--------- | Exercise 7 | ---------')
print('Gene U5: ')
print('Frag: ', new_fragment)
print('Comp: ', Seq0.seq_complement(new_fragment))