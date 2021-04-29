import http.server
import socketserver
import termcolor
import pathlib
from urllib.parse import urlparse, parse_qs
import server_utils as su
import jinja2


def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content

def read_template_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content
# Define the Server's port
PORT = 8080

LIST_SEQUENCES  = ['AAACCCTTTT', 'GGGCCCTTT', 'AGTAGT', 'CTGCTG', 'ATATATA']

LIST_GENES = ['ADA', 'FRAT1', 'FXN', 'RNU269P', 'U5']

LIST_OPERATIONS = ['Info', 'Comp', 'Rev']

BASES_INFORMATION = {
    'A':{
        'link': "https://en.wikipedia.org/wiki/Adenine",
        'formula': 'C5H5N5',
        'name': 'ADENINE',
        'colour':'green'
    }, #El value de A es un diccionario a su su vez
    'C': {
        'link': "https://en.wikipedia.org/wiki/Citosine",
        'formula': 'C5H5N5',
        'name': 'CITOSINE',
        'colour':'yellow'

    },
    'G': {
        'link': "https://en.wikipedia.org/wiki/Guanine",
        'formula': 'C5H5N5',
        'name': 'GUANINE',
        'colour':'blue'

    },

    'T': {
        'link': "https://en.wikipedia.org/wiki/Timine",
        'formula': 'C5H5N5',
        'name': 'TIMINE',
        'colour':'pink'

    }
} #Diccionario


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self): #Get all the requests
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

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

        # IN this simple server version, We are NOT processing the client's request

        #Contex is a dict that we create with the values we are going to pass to any file.html
        context = {}

        if path_name == '/': #ESTA VA A SER NUESTRA PÁGINA PRINCIPAL, Y LO QUE SE VA A VER ESTÁ DENTRO DE INDEX.HTML
            context['n_sequences'] = len(LIST_SEQUENCES) #creamos key y value para mandar esa informacion a INDEX-HTML, que la va a usar
            context['list_genes'] = LIST_GENES #creamos una nueva key y value, el valor sera una lista con los nombres de las secuencias de genes
            context['list_operations'] = LIST_OPERATIONS
            contents = su.read_template_html_file('./html/index.html').render(context=context)

        elif path_name == '/test': #Cuando trabajamos con forms si usamos self.path, la ruta luego se le añade un ? al final. SOLO PASA CON FORMS

            #FORMS: For sending information from the client to the server we use the html forms
            #Lo mejor va a ser usar siempre PATH_NAME !! Para que nunca haya ningun problema

            contents = su.read_template_html_file('./html/test.html').render()

        elif path_name == '/ping':
            contents = su.read_template_html_file("./html/ping.html").render()#ERROR SOLUCIONARLO


        elif path_name == '/get':

            """Cuando en el browser seleccionamos alguna de las secuencias:
            Resource requested:  /get
            Parameters: {'sequence': ['1']}"""

            number_sequence = arguments['sequence'][0] #accedemos al valor de la key sequence.
            #Ese valor, es una lista, que a su vez, contiene sólo un elemento, que es el número
            #De la secuencia que queremos obtener. por tanto ponemos number_sequence = arguments['sequence'][0]


            """Una vez que el server tiene el número de la secuencia que el client quiere obtener,
            tenemos que hacer lo mismo que en la práctica 3 anterior, es decir:
            - """

            contents = su.get(LIST_SEQUENCES, number_sequence) #esto es informacion que vamos a mandar
            #a la funcion get de server_utils (su). Esa informacion es el numero de la secuencia que queremos
            #y también, la lista de secuencias. Una vez que llegue a la función get, alli lo que va a hacer es,
            #Crear un diccionario recopilando toda la informacion, context, que será enviado a GET.HTML
            #para que se pueda imprimir la información deseada.

            """QUÉ ESTÁ OCURRIENDO EN SERVER_UTILS (SU):
            def get(list_sequences, seq_number):
            sequence = list_sequences[int(seq_number)] #almacenamos la secuencia que nos pide el client
            context = {'number': seq_number, 'sequence': list_sequences} #crear el HTML con la secuencia que nos ha pedido el client
            contents = read_template_html_file('./html.get.html').render(context=context)
            return contents """

        elif path_name == '/gene':
            gene = arguments['gene'][0]
            contents = su.gene(gene)

        elif path_name == '/operation':

            """ Fijarnos en lo que nos sale en la terminal: 
            Resource requested:  /operation
            Parameters: {'sequence': ['AAAA'], 'calculation': ['Comp']}"""

            sequence = arguments['sequence'][0]
            operation = arguments['calculation'][0]


            if operation == 'Info':
                contents = su.info(sequence, operation)
            elif operation == 'Comp':
                contents = su.comp(sequence, operation)
            else:
                contents = su.rev(sequence, operation)



        else:
            contents = su.read_template_html_file("./html/error.html").render()


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html') #ESPECIFICAR EL CONTENIDO QUE ESTAMOS MANDANDO
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