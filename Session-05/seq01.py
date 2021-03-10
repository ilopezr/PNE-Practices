import termcolor

class Seq: #Dentro de las class, el orden de las funciones no es relevantes

    """@staticmethod cuando no queremos trabajar con self pero queremos que la funcion este dentro de nuestra class,
    and therefore you cant work with attributes.
    And what´s better, create functions inside the class with the static method or in another file and import it?.
    It depends, when programming i need to check if im going to use that method anywhere else or if the method
    is only going to be used inside that class."""

    #To call a function in ahother module 'Seq0' : Seq0.is_valid_sequence()
    #Para printear un method normal : self.funcion(), we use self
    #Para printear un sthatic method : Seq.funcion('Hello), we call the class

    # De primeras hubieramos hecho lo que tenemos debajo, sin embargo está mal,
    # porque según el, en algunos casos estamos asignando dos veces un valor para una variable
    # self.strbases = strbases y luego si da error , self.strbases = 'Error'

    """"    self.strbases = strbases #OJO DEFINIR LOS ATTRIBUTES AT THE BEGINNING OF OUR INNIT 
    if self.is_valid_sequence_2(strbases):
        print('New sequence created')
    else:
        self.strbases = 'Error'
        print('INCORRECT sequence detected')  """

    def __init__(self, strbases): #Es una funcion que se usa para que s1 y s2 puedan usarse en las demas funciones que hay dentro de la class, solo se ejecute si stanciamos la class
        if Seq.is_valid_sequence_2(strbases):
            print('New sequence created')
            self.strbases = strbases
        else:
            self.strbases = 'Error'
            print('INCORRECT sequence detected')

    """Otra manera de hacer el innit sería, copiando def is_valid_sequence(self) en Seq0 y: 
        if Seq0.is_valid_sequence_2(strbases):
        print('New sequence created')
        self.strbases = strbases
    else:
        self.strbases = 'Error'
        print('INCORRECT sequence detected')"""

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        return len(self.strbases)

    #Hacemos una con el self.method, y otra con el staticmethod para ver la diferencia.

    #def is_valid_sequence(self): ESTA LA HEMOS TRASPASADO A SEQ0
        #for i in self.strbases:
            #if i != 'A' and i != 'T' and i != 'C' and i != 'G':
               # return False
            #return True

    @staticmethod
    def is_valid_sequence_2(bases):
        for i in bases:
            if i != 'A' and i != 'T' and i != 'C' and i != 'G':
                return False
            return True

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = 'Sequence' + str(i) + ': ( Lenght :' + str(list_sequences[i].len()) + ')' + str(list_sequences[i])
            termcolor.cprint(text, 'yellow')


#class Gene(Seq): #dentro del parentesis se pone la clase padre
    #pass #el child heredará los innit y todos los method del father class

def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
        return list_seq

#s1 = Seq("ACCTGC") #La función innit convierte esto a "ACCTGC" y
# lo guarda en self.strbases para selfmethod o s1 para static methods

#s2 = Seq("Hello? Am I a valid sequence?") #La función innit convierte esto a "Hello?..." y lo guarda en self.strbases

