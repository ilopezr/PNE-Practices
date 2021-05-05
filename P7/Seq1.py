import termcolor
from pathlib import Path
import operator

class Seq:
    NULL_SEQUENCE = 'NULL'
    INVALID_SEQUENCE = 'ERROR'

    def __init__(self, strbases = NULL_SEQUENCE):
        self.strbases = strbases

        if strbases == Seq.NULL_SEQUENCE:
            print('NULL Seq created')
            self.strbases = strbases

        else: #if strbases != Seq.NULL_SEQUENCE:
            if Seq.is_valid_sequence_2(strbases): #Si es una sequencia correcta... strbases = strbases / #Ponemos Seq. porque se trata de un staticmethod, al que hay que meterle arguments
                print('New sequence created!')
                self.strbases = strbases
            else:                                 #Si NO es una sequencia correcta... strbases == ERROR
                self.strbases = Seq.INVALID_SEQUENCE
                print('INCORRECT sequence detected')

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    @staticmethod
    def is_valid_sequence_2(bases):
        for i in bases:
            if i != 'A' and i != 'T' and i != 'C' and i != 'G':
                return False
        return True

    def len(self):
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = 'Sequence' + str(i) + ': ( Lenght :' + str(list_sequences[i].len()) + ')' + str(list_sequences[i])
            termcolor.cprint(text, 'yellow')

    def count_bases(self): #Si se ejecuta con una secuencia incorrecta returnearíamos 0 0 0 0
        a, g, c, t = 0, 0, 0, 0

        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return a, g, c, t
        else:
            for i in range(0, len(self.strbases)):
                if self.strbases[i] == 'A':
                    a += 1
                elif self.strbases[i] == 'G':
                    g += 1
                elif self.strbases[i] == 'C':
                    c += 1
                elif self.strbases[i] == 'T':
                    t += 1
            return a, g, c, t

    def count(self):
        a, c, g, t, = self.count_bases()
        return {'A': a, 'C': c, 'T': t, 'G':g}

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return 'Null Sequence. The result can not be calculated.'
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return 'The result can not be calculated. The sequence you have introduced is not correct.'
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return 'Null Sequence. The result can not be calculated.'
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return 'The result can not be calculated. The sequence you have introduced is not correct.'
        else:
            complement = ''
            for ch in self.strbases:
                if ch == 'A':
                    complement += 'T'
                elif ch == 'C':
                    complement += 'G'
                elif ch == 'G':
                    complement += 'C'
                elif ch == 'T':
                    complement += 'A'
            return complement

    @staticmethod
    def take_out_first_line(sequence):
        return sequence[sequence.find("\n") + 1:].replace('\n', '')

    def seq_read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())


    def processing_genes(self):
        counter_dict = {'A': self.strbases.count('A'), 'C': self.strbases.count('C'), 'G': self.strbases.count('G'),
                        'T': self.strbases.count('T')}
        counter_dict_sorted = sorted(counter_dict.items(), key=operator.itemgetter(1), reverse=True)
        return counter_dict_sorted[0][0]


    def percentage_base(self, count_bases, seq_len):
        a = str(round(count_bases[0] / seq_len*100, 2)) + '%'
        c = str(round(count_bases[1] / seq_len*100, 2)) + '%'
        g = str(round(count_bases[2] / seq_len*100, 2)) + '%'
        t = str(round(count_bases[3] / seq_len*100, 2)) + '%'
        return {'A': a, 'C':c, 'G': g, 'T':t}

    @staticmethod
    def frequent_base(dict_count):
        return max(dict_count, key= dict_count.get)

def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number): #Creamos tantas secuencias como nos indique el número
        # A i = 0 ---> i = 1
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq

def test_sequences(): #FUNCIÓN PARA CREAR LAS 3 SEQUENCIAS
    s1 = Seq()
    s2 = Seq('ACTG')
    s3 = Seq('Invalid Sequence')
    return s1, s2, s3

