from Seq1 import test_sequences

"""Write a python program that creates three sequences: null, valid and invalid. 
Then it prints their lengths, sequences and dictionary returned by the count() method."""


def print_result(i, sequence):
    print('Sequence' + str(i) + ': (Length: ' + str(sequence.len()) + ') ' + str(sequence))
                                                #sequence = Seq('ACGT').len()
    print('Bases:', sequence.count())

print('--------- |Practice 1, Exercise 6| ---------')
list_sequences = list(test_sequences()) #lista de s1, s2, s3
for i in range(0, len(list_sequences)):
    print_result(i, list_sequences[i])

"""IMPORTANTE!! No hemos puesto Seq1.test_sequences porque directamente hemos importado la funcion. 
No obstante, si hubieramos puesto import Seq1, si que hubieramos tenido que ponerlo. """

#DUDA PREGUNTAR DAVID
#En este ejercicio tengo una duda, cuando ponemos la variable sequence dentro de print_result, estamos
#haciendo una llamada a la class no? Entonces, si no hemos importado la class, por qué se supone que funciona?