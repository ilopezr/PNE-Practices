from pathlib import Path #Sirve para abrir un archivo
import operator #Para ordenar unos diccionarios
import termcolor #Para poner el código de colores

def seq_ping():
    print('Ok')

def take_out_first_line(sequence): #Quitar la primera linea de un archivo fasta
    return sequence[sequence.find("\n")+ 1:].replace('\n', '')

def seq_read_fasta(filename): #LEER, ALMACENAR un body de un archivo fasta
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
    counter_dict_sorted = sorted(counter_dict.items(), key=operator.itemgetter(1), reverse=True)
    return counter_dict_sorted[0][0]



class Seq: #Dentro de las class, el orden de las funciones no es relevantes

    def __init__(self, strbases): #Es una funcion que se usa para que s1 y s2 puedan usarse en las demas funciones que hay dentro de la class, solo se ejecute si stanciamos la class
        if Seq.is_valid_sequence_2(strbases):
            print('New sequence created')
            self.strbases = strbases
        else:
            self.strbases = 'Error'
            print('INCORRECT sequence detected')

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        return len(self.strbases)

    @staticmethod
    def is_valid_sequence_2(bases):
        for i in bases:
            if i != 'A' and i != 'T' and i != 'C' and i != 'G':
                return False
            return True

    def is_valid_sequence(self):
        for i in self.strbases:
            if i != 'A' and i != 'T' and i != 'C' and i != 'G':
                return False
            return True

    def len(self):
        return len(self.strbases)

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = 'Sequence ' + str(i) + ': (Lenght : ' + str(list_sequences[i].len()) + ') ' + str(list_sequences[i])
            termcolor.cprint(text, 'yellow')

#FUERA DE LA CLASS

def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number): #Creamos tantas secuencias como nos indique el número
        # A i = 0 ---> i = 1
        list_seq.append(Seq(pattern * (i + 1))) #NO ENTIENDO DE DONDE SALE ESE SEQ
    return list_seq #Lista de cadenas






