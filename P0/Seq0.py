"""ESTE ARCHIVO SÓLO ALMACENA FUNCTIONS Y NO CLASS"""

from pathlib import Path #Sirve para abrir un archivo FASTA
import operator #Para ordenar unos diccionarios

def seq_ping():
    print('Ok')

def take_out_first_line(sequence): #Quitar la primera linea de un archivo fasta
    return sequence[sequence.find("\n")+ 1:].replace('\n', '')

def seq_read_fasta(filename): #Leer y almacenar el cuerpo de un archivo fasta
    sequence = take_out_first_line(Path(filename).read_text()) #We are working with strings not with files
    return sequence

def seq_len(sequence): #longitud de una secuencia
    return len(sequence)

def seq_count_base(sequence, base): #contar el número de una base de una sequencia
    return sequence.count(base)

def seq_count(sequence): #Diccionario con el numero de todas las bases de una secuencia
    a, c, g, t = 0, 0, 0, 0
    for d in sequence: #Importante que la d sea distinta a a,g,c,t minúsculas
        if d == 'A':
            a += 1
        elif d == 'C':
            c += 1
        elif d == 'G':
            g+= 1
        else:
            t+= 1
    return {'A':a, 'C':c, 'G':g, 'T':t}

#Otra solucion, un poco mejor
#def seq_count(sequence):
    #gene_dict = {'A':0, 'C':0, 'G':0, 'T':0}
    #for d in sequence: #Importante que la d sea distinta a a,g,c,t
        #gene_dict[d] += 1
    #return gene_dict

def seq_reverse(sequence):
    return sequence[::-1]

def seq_complement(sequence):
    dict_complement = {'A': 'T', 'T':'A', 'C':'G', 'G':'C'}
    complement = ""
    try:
        for i in sequence:
                complement = complement + dict_complement[i]
        return complement
    except KeyError:
        return 'Can not calculate the complement. The sequence must only contain A,C,T,G bases.'

def processing_genes(sequence):
    counter_dict = {'A': sequence.count('A'), 'C': sequence.count('C'), 'G': sequence.count('G'), 'T': sequence.count('T')}
    counter_dict_sorted = sorted(counter_dict.items(), key=operator.itemgetter(1), reverse=True) #Ordena el diccionario según los items, de mayor a menor
    return counter_dict_sorted[0][0] #coge el key del primer item, el key del item que más se repite

def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number): #Creamos tantas secuencias como nos indique el número
        # A i = 0 ---> i = 1
        list_seq.append(Seq(pattern * (i + 1))) #NO ENTIENDO DE DONDE SALE ESE SEQ
    return list_seq #Lista de cadenas






