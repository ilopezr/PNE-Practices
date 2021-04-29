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
        'sequence': sequence
    } #crear el HTML con la secuencia que nos ha pedido el client
    contents = read_template_html_file('./html/get.html').render(context=context)
    return contents


def calculate_percentaje(number_repetitions, arg):
    return round(number_repetitions * 100 / len(arg), 1)


def info(sequence, operation): #Esto es lo que se envía desde el server: contents = su.info(sequence, operation)

    correct_dna = Seq.is_valid_sequence_2(sequence)

    if correct_dna:  # Same as :  if correct_dna == True:
        argument_object = Seq(sequence)
        a, g, c, t = argument_object.count_bases() # De esta manera solo se ejecuta el bucle una vez cuando hacemos luego el print
        result = f""" Sequence: {sequence}
        Total length: {len(sequence)} 
        A: {a} {calculate_percentaje(a, sequence)} %
        C: {c} {calculate_percentaje(c, sequence)} %
        G: {g} {calculate_percentaje(g, sequence)} %
        T: {t} {calculate_percentaje(t, sequence)} %"""  #MANDAMOS EL CÓDIGO SÓLO UNA VEZ, PORQUE SI NO, ConnectionResetError: [WinError 10054]

        context = {'sequence': sequence, 'operation': operation, 'result': result}
        contents = read_template_html_file('./html/operation.html').render(context=context)
        return contents

    else:
        result = 'The result can not be calculated. Introduce a correct sequence. '
        context = {'sequence': sequence, 'operation': operation, 'result': result}
        contents = read_template_html_file('./html/operation.html').render(context=context)
        return contents


def comp(sequence, operation): #Esto es lo que se envía desde el server: contents = su.comp(sequence, operation)
    result = Seq(sequence).complement()
    context = {'sequence': sequence, 'operation': operation, 'result': result}
    contents = read_template_html_file('./html/operation.html').render(context=context)
    return contents

def rev(sequence, operation): #Esto es lo que se envía desde el server: contents = su.rev(sequence, operation)

    result = Seq(sequence).reverse()
    context = {'sequence': sequence, 'operation': operation, 'result': result}
    contents = read_template_html_file('./html/operation.html').render(context=context)
    return contents


def gene(seq_name): #CAMBIARLO
    PATH = './sequences/' + seq_name + '.txt'
    s1 = Seq()
    s1.seq_read_fasta(PATH)
    context = {'gene_name': seq_name, 'gene_contents': s1.strbases}
    contents = read_template_html_file('./html/gene.html').render(context=context)
    return contents