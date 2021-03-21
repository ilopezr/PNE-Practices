import Seq0

"""Which is the most frequent base in each gene?"""

GENE_FOLDER = './sequences/'
gene_list =['U5' , 'ADA', 'FRAT1', 'FXN']

print('--------- | Exercise 8 | ---------')
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + '.txt') #Leemos la sequencia del gen sin su primera línea
    print('Gene' , gene , ': Most frequent Base:', Seq0.processing_genes(sequence))