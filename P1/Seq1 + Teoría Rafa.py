import termcolor
from pathlib import Path

class Seq: #La primera letra e la class tiene que estar en mayúscula

    NULL_SEQUENCE = 'NULL'        #A CONSTANT IS A VALUE WHOSE VALUE IS NEVER GOING TO CHANGE, AND IT IS WRITTEN WITH UPPER LETTERS
    INVALID_SEQUENCE = 'ERROR'

    def __init__(self, strbases = NULL_SEQUENCE): #En los arguments, a diferencia de dentro del method, no hace falta que pongamos desde donde importamos el NULL_SEQUENCE, es decir, no tenemos que poner Seq.NULL_SEQUENCE
        self.strbases = strbases           #strbases = 'NULL'It is used in python for creating optional arguments. If no argument is given, python automatically will create one with the default value to "NULL".
                                           #This is the value we will use to identify the null sequences.

        if strbases == Seq.NULL_SEQUENCE:   #Si es una sequencia vacía... strbases == NULL #Dentro de la def tenemos que decir desde donde importamos NULL_SEQUENCE
            print('NULL Seq created')      #Dentro del innit podemos meter las funciones de debajo siempre y cuando las estancias esten creadas de ANTES
            self.strbases = strbases

        else: #if strbases != Seq.NULL_SEQUENCE:
            if Seq.is_valid_sequence_2(strbases): #Si es una sequencia correcta... strbases = strbases / #Ponemos Seq. porque se trata de un staticmethod, al que hay que meterle arguments
                print('New sequence created')
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
            return 'NULL'
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return 'ERROR'
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
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
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())  # We are working with strings not with files

class Gene(Seq): #TIENE TODOS LOS ATTRIBUTES DE CLASS SEQ

    def __init__(self, strbases, name=''): #Definimos el attributte adicional que esta clase va a tener, name = ''
        super().__init__(strbases)  #This is just the way you initialize or can call your parent innit method (en este caso es seq). Lo que pasará despues de eso es ejecutar el innit method of the parent class
        self.name = name
        print('New gene created')

    def __str__(self):
        return self.name + '-' + self.strbases

    def len(self): #En este caso, estamos moficiando el len method del padre, ya que se pueden modificar los methos del padre (methods, no FUNCIONES) en una child class.
        if len(self.strbases) < 10:
            return 'Sequence ' + self.strbases + 'is not long.'
        else:
            return 'Sequence ' + self.strbases + 'is long.'

        #Si en la child class no decimos nada sobre las funciones del padre, las funciones del padre no se modifican.
        #Dentro de la child class tambien podemos definir nuevos methods que sólo tendra el child


def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number): #Creamos tantas secuencias como nos indique el número
        # A i = 0 ---> i = 1
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq

def test_sequences():
    s1 = Seq()
    s2 = Seq('ACTG')
    s3 = Seq('Invalid Sequence')
    return s1, s2, s3



#s1 = Seq('ACGT')
#s1.len() #Aqui como trabajamos con attributes y se guardan en el self, no tenemos que meter nada

"""Seq.is_valid_sequence_2('ACGT') #En los static methods tenemos que poner Class.funcion(CON LO QUE VAMOS A TRABAJAR) y no el self
Seq0.is_valid_sequence('ACDG') #Si usamos un archivo externo nombredelarchivo.nombredefuncion(CON LO QUE VAMOS A TRABAJAR)
self.nombredelafuncion() #Si usamos una funcion de dentro de la class que no sea static method"""

#s2 = Seq('AGTATGD')
#s2.strbases = 'AG' #Para cambiar el atributo, en este caso las strbases de s2


#g = Gene('CTAAAAAGCT', 'FRAT1')
#print(g.len())