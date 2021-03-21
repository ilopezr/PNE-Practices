import Seq0

"""Implement the seq_complement(seq) function, that calculates a new sequence complement to the original bases.
 A and T are complement, as well as C and G. 
Therefore, the complement sequence of "ATTCG" is "TAAGC". It should be written in the Seq0.py file
Write a python program for creating a new fragment composed of the first 20 bases of the U5 gene. 
This fragment should be printed on the console. Then calculate the complement of this fragment by calling the seq_complement() function."""


GENE_FOLDER = './sequences/'
FILENAME = 'U5.txt'

new_fragment = Seq0.seq_read_fasta(GENE_FOLDER + FILENAME)[0:20]

print('--------- | Exercise 7 | ---------')
print('Gene U5: ')
print('Frag: ', new_fragment)
print('Comp: ', Seq0.seq_complement(new_fragment))