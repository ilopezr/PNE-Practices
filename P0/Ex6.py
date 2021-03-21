import Seq0

GENE_FOLDER = './sequences/'
FILENAME = 'U5.txt'

new_fragment = Seq0.seq_read_fasta(GENE_FOLDER + FILENAME)[0:20] #Leemos el archivo habiendole quitado la primera línea y la recortamos (20 primeras bases)
#Ponemos [0:20] y no 21, porque la base de la posicion cero es la base una, y la base de la posicion 20 es la 21.

print('--------- | Exercise 6 | ---------')
print('Gene U5: ')
print('Frag: ', new_fragment)
print('Rev: ', Seq0.seq_reverse(new_fragment))