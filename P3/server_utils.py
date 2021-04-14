from Seq1 import Seq
from pathlib import Path

def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip='False')
    print(termcolor.colored(message, color))

def format_command(command): #Con esta función quitamos los carateres extra del msg_raw (que está en bytes)
    return command.replace('\n', '').replace('\r', '')

def ping(cs):
    print_colored('PING command!', 'green')
    response = 'OK!'
    cs.send(str(response).encode()) #como estamos usando cs, lo importamos en el Seq-Server

def get(cs, list_sequences, argument):
    print_colored('GET', 'yellow')
    response = list_sequences[int(argument)]
    print(response)
    cs.send(str(response).encode())

def info(cs, argument):
    print_colored('INFO', 'yellow')
    print('Sequence:', argument)
    correct_dna = Seq.is_valid_sequence_2(argument)
    if correct_dna:  # Same as :  if correct_dna == True:
        argument_object = Seq(argument)
        a, g, c, t = argument_object.count_bases() # De esta manera solo se ejecuta el bucle una vez cuando hacemos luego el print
        list_bases = [a, g, c, t]

        print('Total length: ' + str(len(argument)))
        cs.send(('Total length: ' + str(len(argument))).encode())
        for base in list_bases:
            print(base.upper() + ': ' + str(base) + ' (' + str(round(base * 100 / len(argument), 1)) + '%)')
            cs.send((base.upper() + ': ' + str(base) + ' (' + str(round(base * 100 / len(argument), 1)) + '%)').encode())

        """print('A: ' + str(a) + ' (' + str(round(a * 100 / len(argument), 1)) + '%)')
        cs.send(('A: ' + str(a) + ' (' + str(round(a * 100 / len(argument), 1)) + '%)').encode())
        print('G: ' + str(g) + ' (' + str(round(g * 100 / len(argument), 1)) + '%)')
        cs.send(('G: ' + str(g) + ' (' + str(round(g * 100 / len(argument), 1)) + '%)').encode())
        print('C: ' + str(c) + ' (' + str(round(c * 100 / len(argument), 1)) + '%)')
        cs.send(('C: ' + str(c) + ' (' + str(round(c * 100 / len(argument), 1)) + '%)').encode())
        print('T: ' + str(t) + ' (' + str(round(t * 100 / len(argument), 1)) + '%)')
        cs.send(('T: ' + str(t) + ' (' + str(round(t * 100 / len(argument), 1)) + '%)').encode())"""

    else:
        print('The seq_dna is not correct. Please introduce another one.')

def comp(cs, argument):
    print_colored('COMP', 'yellow')
    print('Sequence:', argument)
    response = Seq(argument).complement()
    print(response)
    cs.send(str(response).encode())

def rev(cs, argument):
    print_colored('REV', 'yellow')
    print('Sequence:', argument)
    response = Seq(argument).reverse()
    print(response)
    cs.send(str(response).encode())

def gene(cs, argument):
    response = Seq()
    if argument == 'U5':
        filename = '../P0/sequences/U5.txt'

    elif argument == 'ADA':
        filename = '../P0/sequences/ADA.txt'

    elif argument == 'FRAT1':
        filename = '../P0/sequences/FRAT1.txt'

    elif argument == 'FXN':
        filename = '../P0/sequences/FXN.txt'

    elif argument == 'RNU6_269P':
        filename = '../P0/sequences/RNU6_269P.txt'

    else:
        print('The argument you have provided is not correct. Try again with this ones: U5, ADA, FRAT1, FXN or RNU6_269P')

    print(response.seq_read_fasta(filename))
    cs.send(str(response.seq_read_fasta(filename)).encode())
