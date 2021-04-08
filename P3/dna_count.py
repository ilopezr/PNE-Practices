def correct_sequence(seq_dna):
    for i in seq_dna:
        if i != 'A' or i != 'T' or i != 'C' or i != 'G':
            return False
    return True #Si returnea eso significará que no se ha metido dentro del if, por tanto, estará bien la cadena.

def count_bases(seq_dna):
    a, g, c, t = 0 , 0, 0, 0
    for i in range(0,len(seq_dna)):
        if seq_dna[i] == 'A':
            a += 1
        elif seq_dna[i] == 'G':
            g += 1
        elif seq_dna[i] == 'C':
            c += 1
        else:
            t += 1
    return a , g, c, t


