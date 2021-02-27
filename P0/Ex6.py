import Seq0
from pathlib import Path

GENE_FOLDER = './sequences/'
FILENAME = 'U5.txt'

new_fragment = Seq0.seq_read_fasta(GENE_FOLDER + FILENAME)
new_fragment = new_fragment[0:20]
print(new_fragment)

print('--------- | Exercise 6 | ---------')
print('Gene U5: ')
print('Frag: ', new_fragment)
print('Rev: ', Seq0.seq_reverse(new_fragment))