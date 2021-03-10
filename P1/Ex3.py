from Seq1 import Seq

""" We will manage three types of sequences: Valid, Invalid and Null:
Null: Empty sequence "". It has no bases
Valid: A sequence compose of the union of only the four valid bases: 'A', 'T', 'C', 'G'. 
Invalid: A sequence that has one or more not valid bases."""

"""Write a python program that creates first a null sequence and then a valid sequence.
 It should prints the objects."""

print('--------- |Exercise 3| ---------')

s1 = Seq()
s2 = Seq('ACTG')
s3 = Seq('Invalid Sequence')

#Como vemos, a la hora de imprimir si no especificamos ninguna función, se imprime lo del __innit__

print('Sequence 1:', s1)
print('Sequence 2:', s2)
print('Sequence 3:', s3)