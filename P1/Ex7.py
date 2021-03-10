from Seq1 import test_sequences

"""Implement the reverse() method. If the sequence is Null or invalid, it should return the string
 "NULL" or  "ERROR" respectively (and not its reverse!) Write a python program that creates three sequences: 
 null, valid and invalid. Then it prints their lengths, sequences, the dictionary with the bases 
 and the reverse sequence. """


def print_result(i, sequence): #Para cada una de las secuencias...
    print('Sequence' + str(i) + ': (Length: ' + str(sequence.len()) + ') ' + str(sequence))
    print('BASES:', sequence.count()) #Imprime diccionario con el numero de bases
    print('Rev:', sequence.reverse()) #Imprime la sequencia revertida

print('--------- |Practice 1, Exercise 7| ---------')
list_sequences = list(test_sequences())
for i in range(0, len(list_sequences)):
    print_result(i, list_sequences[i])
