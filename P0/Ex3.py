import Seq0

GENE_FOLDER = './sequences/'

gene_list =['U5' , 'ADA', 'FRAT1', 'FXN']

print('--------- | Exercise 3 | ---------')

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + '.txt') #Quitamos la primera línea del gen
    print('Gene', gene, '---> Length:', Seq0.seq_len(sequence)) #Calculamos la longitud del gen



