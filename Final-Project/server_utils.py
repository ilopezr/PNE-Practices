from Seq1 import Seq
import jinja2
import pathlib
import http.client
import json
# JSON Transforma strings que provienen de .decode() en dictionary

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

def get_info(ENDPOINT): #Creamos una función que nos permita pasar json info a nuestros html files
    SERVER = 'rest.ensembl.org'

    #ENDPOINT: Cada vez será distinto por tanto lo definimos en el server y posteriormente lo introducimos
    #a la función

    PARAMS = '?content-type=application/json'

    #stablish connection
    connection = http.client.HTTPConnection(SERVER)

    #Ask for information
    connection.request('GET', ENDPOINT + PARAMS)

    #Get the information
    information = connection.getresponse()
    information_decoded = information.read().decode() #informacion decoded pero almacenada en string
    dict_information = json.loads(information_decoded) #diccionario con la informacion
    return dict_information

def info_listSpecies(dict_information, limit): #context = su.info_listSpecies(dict_information, limit)

    #Necesitamos saber el número total de especies, el límite seleccionado, y el nombre de nuestras especies

    #NÚMERO DE ESPECIES: Las especies se almacenan en el diccionario, en una lista bajo la key 'species'
    number_species = len(dict_information['species']) #obtenemos la lista y medimos su longitud

    #LÍMITE
    limit = limit

    #NOMBRE DE NUESTRAS ESPECIES Hay que hacer un bucle
    list_species = []
    for i in range(0, int(limit)):
        list_species.append(dict_information['species'][i]['display_name']) #iteramos sobre cada una de las especies,
        # es decir, sobre cada uno de los elementos de la lista de value de la key 'species'.
        #De cada especie extraemos el valor de la key 'display_name' que es la key que nos da el nombre de cada especie

    #Ya tenemos nuestra lista de especies, nuestro límite y el número de especies asique almacenamos ese contenido en un
    #diccionario para posteriormente mandarlo al html de listspecies.

    context = {'number_species' : number_species, 'limit': limit, 'list_species':list_species}
    return context

def info_karyotype(dict_information):

    #Tenemos que guardar en una lista los nombres de los cromosomas
    #Los nombres de los cromosomas se almacenan en la key 'karyotype' de dict_information, en una lista de valores.

    list_chromosomes = dict_information['karyotype']
    context = {'list_chromosomes': list_chromosomes}
    return context

def info_chromoLength(dict_information, chromo):

    length = dict_information['top_level_region'][int(chromo)]['length']
    context = {'length': length}
    return context

def geneSeq(dict_information, gene):
    seq = dict_information['seq']
    context = {'seq':seq , 'gene': gene}
    return context

def geneInfo(dict_information, gene):
    length = len(dict_information['seq'])
    id = dict_information['id']
    desc = dict_information['desc'].split(':') #['chromosome', 'GRCh38', '10', '97319271', '97321915', '1']
    chromosome_name = desc[1]
    end = desc[4]
    start = desc[3]
    context = {'start': start, 'end': end, 'length':length , 'id': id, 'chromosome_name': chromosome_name}
    return context


def calculate_percentaje(number_repetitions, arg):
    return round(number_repetitions * 100 / len(arg), 1)


def geneCalc(dict_information, gene):

    #Lo primero de todo_ es sacar la secuencia
    sequence = dict_information['seq']

    #Una vez tenemos la secuencia...

    correct_dna = Seq.is_valid_sequence_2(sequence)

    if correct_dna:  # Same as :  if correct_dna == True:
        argument_object = Seq(sequence)
        a, g, c, t = argument_object.count_bases() # De esta manera solo se ejecuta el bucle una vez cuando hacemos luego el print
        percent = f"""
        A: {a} ({calculate_percentaje(a, sequence)} %) 
        C: {c} ({calculate_percentaje(c, sequence)} %) 
        G: {g} ({calculate_percentaje(g, sequence)} %) 
        T: {t} ({calculate_percentaje(t, sequence)} %)"""  #MANDAMOS EL CÓDIGO SÓLO UNA VEZ, PORQUE SI NO, ConnectionResetError: [WinError 10054]

        length = len(sequence)
        context = {'percent': percent, 'length': length}
        return context

    else:
        percent = 'The percentages can not be calculated. Introduce a correct sequence. '
        length = len(sequence)
        context = {'percent': percent, 'length': length}
        return context















