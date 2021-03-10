from Seq1 import Seq

"""Write a python program that automatically calculate the answer to this question:
Which is the most frequent base in each gene?
This exercise is the same than the exercise 8 of practice 0, 
but we are using the Seq Class instead of the functions developed 
in the Seq0 module"""


PROJECT_PATH = '../P0/sequences/'

print('--------- |Practice 1, Exercise 9| ---------')

list_sequences = ['U5.txt','ADA.txt', 'FRAT1.txt', 'FXN.txt', 'RNU6_269P.txt']

for i in list_sequences:

    seq = Seq()
    seq.seq_read_fasta(PROJECT_PATH + i) #quitan la primera línea y leen el código
    print('Gene ' + i[:-4] + ': Most frequent Base: ' + seq.processing_genes())