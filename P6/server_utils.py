from Seq1 import Seq
import jinja2
import pathlib

def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip='False')
    print(termcolor.colored(message, color))

def format_command(command): #Con esta función quitamos los carateres extra del msg_raw (que está en bytes)
    return command.replace('\n', '').replace('\r', '')


def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    #Estamos creando un template object que contenga un html file y tenemos que añadir el valor
    # de esos valores en ese template
    return content

def ping(cs):
    print_colored('PING command!', 'green')
    response = 'OK!'
    cs.send(str(response).encode()) #como estamos usando cs, lo importamos en el Seq-Server

def get(list_sequences, seq_number):
    sequence = list_sequences[int(seq_number)] #almacenamos la secuencia que nos pide el client
    context = {
        'number': seq_number,
        'sequence': list_sequences
    } #crear el HTML con la secuencia que nos ha pedido el client
    contents = read_template_html_file('./html.get.html').render(context=context)
    return contents


def calculate_percentaje(number_repetitions, arg):
    return round(number_repetitions * 100 / len(arg), 1)


def info(cs, argument):
    print_colored('INFO', 'yellow')
    print('Sequence:', argument)
    correct_dna = Seq.is_valid_sequence_2(argument)
    if correct_dna:  # Same as :  if correct_dna == True:
        argument_object = Seq(argument)
        a, g, c, t = argument_object.count_bases() # De esta manera solo se ejecuta el bucle una vez cuando hacemos luego el print
        response = f""" Sequence: {argument}
        Total length: {len(argument)} 
        A: {a} {calculate_percentaje(a, argument)} %
        C: {c} {calculate_percentaje(c, argument)} %
        G: {g} {calculate_percentaje(g, argument)} %
        T: {t} {calculate_percentaje(t, argument)} %"""  #MANDAMOS EL CÓDIGO SÓLO UNA VEZ, PORQUE SI NO, ConnectionResetError: [WinError 10054]
        print(response)
        cs.send(response.encode())

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

def gene(seq_name): #CAMBIARLO
    PATH = './sequences/' + seq_name + '.txt'
    s1 = Seq()
    s1.seq_read_fasta(PATH)
    context = {'gene_name': seq_name, 'gene_contents': s1.str_bases}
    contents = read_template_html_file('/html/gene.html').render(context=context)
    return contents