import Seq0

GENE_FOLDER = './sequences/'
FILENAME = 'U5.txt'

new_fragment = Seq0.seq_read_fasta(GENE_FOLDER + FILENAME)[0:20]

print('--------- | Exercise 7 | ---------')
print('Gene U5: ')
print('Frag: ', new_fragment)
print('Comp: ', Seq0.seq_complement(new_fragment))