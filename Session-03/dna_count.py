def correct_sequence(seq_dna):
    for i in seq_dna:
        if i != 'A' or i != 'T' or i != 'C' or i != 'G':
            return False
    return True

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

seq_dna = input('Enter here a dna sequence: ')
correct_dna = correct_sequence(seq_dna)

if correct_dna:
    a, g, c, t = count_bases(seq_dna) #De esta manera solo se ejecuta el bucle una vez cuando hacemos luego el print
    #Evita running el loop muchas veces, solo run 1 vez

    print('Number of "A" :', a)
    print('Number of "G" :', g)
    print('Number of "C" :', c)
    print('Number of "T" :', t)
    print('Longitud de la sequencia: ', len(seq_dna))

else:

