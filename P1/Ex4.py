from Seq1 import Seq

"""The len() method should works with the three types of sequences. 
In case the sequence is Null or invalid, the length should be always 0."""

print('--------- |Exercise 3| ---------')

s1 = Seq()
s2 = Seq('ACTG')
s3 = Seq('Invalid Sequence')


print('Sequence' + str(1) + ': (Length: ' + str(s1.len()) + ') ' + str(s1))
print('Sequence' + str(2) + ': (Length: ' + str(s2.len()) + ') ' + str(s2))
print('Sequence' + str(3) + ': (Length: ' + str(s3.len()) + ') ' + str(s3))