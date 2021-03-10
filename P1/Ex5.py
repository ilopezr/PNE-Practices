from Seq1 import Seq

"""Write a python program that creates three sequences: null, valid and invalid. 
Then it prints their lengths, sequences and the number of bases on the console."""


def print_result(i, sequence):
    print('Sequence' + str(i) + ': (Length: ' + str(sequence.len()) + ') ' + str(sequence))
    a, c, g, t = sequence.count_bases()
    print('A:' + str(a) + ', C:' + str(c) + ', G:' + str(g) + ', T:' + str(t))


print('--------- |Practice 1, Exercise 5| ---------')

s1 = Seq()
s2 = Seq('ACTG')
s3 = Seq('Invalid Sequence')

list_seq = [s1, s2, s3]

for i in range(0, len(list_seq)):
    print_result(i, list_seq[i])
