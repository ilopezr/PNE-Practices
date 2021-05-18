import http.server
import socketserver
import pathlib
from urllib.parse import urlparse, parse_qs
import server_utils as su
import jinja2
import json


def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

# Define the Server's port
PORT = 8080

genes_dict = {'FRAT1':'ENSG00000165879',
              'ADA': 'ENSG00000196839',
              'FXN':'ENSG00000165060',
              'RNU6_269P':'ENSG00000212379',
              'MIR633':'ENSG00000207552',
              'TTTY4C':'ENSG00000226906',
              'RBMY2YP':'ENSG00000227633',
              'FGFR3':'ENSG00000068078',
              'KDR':'ENSG00000128052',
              'ANK2':'ENSG00000145362'}

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self): #Get all the requests

        # Print the request line
        print(self.requestline) #GET /info/A HTTP/1.1
        print(self.path) #/info/A

        o = urlparse(self.path) #Creating urlparse object --- #/test
        path_name = o.path #get the path, es mas o menos parecido a self.path PERO NO es lo mismo
        arguments = parse_qs(o.query) #todo_ aquello que esté despues de la interrogación del request del client
        #arguments va a ser un diccionario, que contenga cada argument como key, y como value su valor.

        #GET /echo?msg=ALELUYA&base=T HTTP/1.1  arguments == msg=ALELUYA&base=T HTTP/1.1
        #Argument 1 : msg = ALELUYA
        #Argument 2 : base = T

        print("Resource requested: ", path_name)
        print("Parameters:", arguments)
        print(arguments['json'])

        # IN this simple server version, We are NOT processing the client's request

        #Contex is a dict that we create with the values we are going to pass to any file.html
        context = {}

        if path_name == '/': #ESTA VA A SER NUESTRA PÁGINA PRINCIPAL, Y LO QUE SE VA A VER ESTÁ DENTRO DE INDEX.HTML
            contents = su.read_template_html_file('./html/index.html').render()

        elif path_name == '/listSpecies':
            ENDPOINT = '/info/species'


            try:

                #Tenemos que controlar los límites, si user introduce un límite mayor del esperado, imprimimos toda la lista
                #de especies, pero si introduce un número más pequeño de especies que las que hay en la lista, imprimimos sólo
                #las que nos pide

                #Intentamos imprimir los diccionarios que el user pide  Parameters: {'limit': ['10']}
                dict_information = su.get_info(ENDPOINT)

                limit = arguments['limit'][0] #Es una lista por tanto cogemos sólo el elemento en posición 0
                if int(limit) > len(dict_information['species']):
                    limit = len(dict_information['species'])

                if arguments['json'] == ['1']:
                    context = su.info_listSpecies(dict_information, limit)
                    contents = json.dumps(context)
                    content_type = 'application/json'
                    error_code = 200

                else:

                    context = su.info_listSpecies(dict_information, limit)
                    contents = read_template_html_file("./html/listSpecies.html").render(context=context) #lo naranja siempre
                    # igual que el nombre que hay en la plantilla, y lo que hay detrás del igual, es la variable que le pasamos como argument

            except ValueError:
                contents = su.read_template_html_file("./html/error.html").render()
            except KeyError:
                contents = su.read_template_html_file("./html/error.html").render()


        elif path_name == '/karyotype':

            """Resource requested:  /karyotype
            Parameters: {'specie': ['mouse']}"""

            try: #Tenemos que controlar que la especie que introduce exista
                specie = arguments['specie'][0]
                ENDPOINT = '/info/assembly/' + str(specie)
                dict_information = su.get_info(ENDPOINT)  #Extraer la información de la especie deseada

                # Ahora tenemos que enviarle el contenido dict_information a la función que se encargue
                # de sacar la informacion de ese diccionario para posteriormente enviarla al html correspondiente.
                # Esta función se va a llamar def info_karyotype:
                context = su.info_karyotype(dict_information) #Nos devuelve la lista de cromosomas, es decir el cariotipo
                contents = read_template_html_file('./html/karyotype.html').render(context = context)

            except KeyError:
                contents = su.read_template_html_file("./html/error.html").render()

        elif path_name == '/chromosomeLength': #CREO QUE NO VA BIEN !!

            """Resource requested:  /chromosomeLength
            Parameters: {'specie': ['mouse'], 'chromo': ['18']}"""

            try: #Tenemos que asegurarnos de que el cromosoma y la especie existan
                specie = arguments['specie'][0]
                chromo = arguments['chromo'][0]

                # /info/assembly/homo_sapiens?content-type=application/json

                ENDPOINT = '/info/assembly/' + str(specie)
                dict_information = su.get_info(ENDPOINT)

                context = su.info_chromoLength(dict_information, chromo)
                contents = read_template_html_file('./html/chromosomeLength.html').render(context=context)

            except KeyError:
                contents = su.read_template_html_file("./html/error.html").render()

        elif path_name == '/geneSeq':
            """Resource requested:  /geneSeq
            Parameters: {'gene': ['FRAT1']}"""

            try:
                gene = arguments['gene'][0]
                print('gene:', gene)
                id = genes_dict[gene]
                print(id)
                ENDPOINT = '/sequence/id/' + id #"/sequence/id/" + id
                dict_information = su.get_info(ENDPOINT) #Diccionario con la informacion que necesitamos
                print(dict_information)
                print('length', len(dict_information['seq']))

                context = su.geneSeq(dict_information, gene)
                contents = read_template_html_file("./html/geneSeq.html").render(context=context)

            except KeyError:
                contents = su.read_template_html_file("./html/error.html").render()

        elif path_name == '/geneInfo':
            try:
                gene = arguments['gene'][0]
                id = genes_dict[gene]
                ENDPOINT = '/sequence/id/' + id  # "/sequence/id/" + id
                dict_information = su.get_info(ENDPOINT)
                print(dict_information)

                context = su.geneInfo(dict_information, gene)
                print(context)
                contents = read_template_html_file("./html/geneInfo.html").render(context=context)

            except KeyError:
                contents = su.read_template_html_file("./html/error.html").render()

        elif path_name == '/geneCalc':
            try:
                gene = arguments['gene'][0]
                id = genes_dict[gene]
                ENDPOINT = '/sequence/id/' + id  # "/sequence/id/" + id
                dict_information = su.get_info(ENDPOINT)
                print(dict_information)

                context = su.geneCalc(dict_information, gene)
                print(context)
                contents = read_template_html_file("./html/geneCalc.html").render(context=context)

            except KeyError:
                contents = su.read_template_html_file("./html/error.html").render()


        else:
            contents = su.read_template_html_file("./html/error.html").render()


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', content_type) #ESPECIFICAR EL CONTENIDO QUE ESTAMOS MANDANDO
        self.send_header('Content-Length',  len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return

# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()