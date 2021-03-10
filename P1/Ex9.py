from Seq1 import Seq

"""Write a python program that reads a sequence from the U5.txt file. Then it should print its lengths, 
the sequence, the dictionary with the bases, the reverse sequence and the complement. """

"""We want to create sequence from files in fasta format. That is the purpose of the read_fasta() method
For using the read_fasta() method we need first to create a Null sequence. 
And then we call the read_fasta() method"""


def print_result(i, sequence):
    print('Sequence' + str(i) + ': (Length: ' + str(sequence.len()) + ') ' + str(sequence))
    print('BASES:', sequence.count())
    print('Rev:', sequence.reverse())
    print('Complement:', sequence.complement())

PROJECT_PATH = '../P0/sequences/'

print('--------- |Practice 1, Exercise 9| ---------')
s1 = Seq()
s1.seq_read_fasta(PROJECT_PATH + 'ADA.txt') #quitan la primera línea y leen el código
print_result('', s1)