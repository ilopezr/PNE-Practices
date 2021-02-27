from pathlib import Path #and what does Path make? Sirve para abrir un archivo

def seq_ping():
    print('Ok')

def take_out_first_line(sequence):
    return sequence[sequence.find("\n")+ 1:].replace('\n', '')

def seq_read_fasta(filename):
    sequence = take_out_first_line(Path(filename).read_text()) #We are working with strings not with files
    return sequence

def seq_len(sequence):
    return len(sequence)

def seq_count_base(sequence, base):
    return sequence.count(base)

def seq_count(sequence):
    a, c, g, t = 0, 0, 0, 0

    for d in sequence: #Importante que la d sea distinta a a,g,c,t
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
    #for d in seq: #Importante que la d sea distinta a a,g,c,t
        #gene_dict[d] += 1
    #return gene_dict

def seq_reverse(sequence):
    return ''.join(reversed(sequence))

def seq_complement(sequence):

    complement = ""
    for i in range(0, len(sequence)):
        if sequence[i] == "A":
            complement = complement + "T"
        elif sequence[i] == "T":
            complement = complement + "A"
        elif sequence[i] == "C":
            complement = complement + "G"
        elif sequence[i] == "G":
            complement = complement + "C"
    return complement


