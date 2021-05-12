import http.server
import socketserver
import pathlib
from urllib.parse import urlparse, parse_qs
import server_utils as su
import jinja2


def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

# Define the Server's port
PORT = 8080

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

        # IN this simple server version, We are NOT processing the client's request

        #Contex is a dict that we create with the values we are going to pass to any file.html
        context = {}

        if path_name == '/': #ESTA VA A SER NUESTRA PÁGINA PRINCIPAL, Y LO QUE SE VA A VER ESTÁ DENTRO DE INDEX.HTML
            contents = su.read_template_html_file('./html/index.html').render()

        elif path_name == '/listSpecies':
            ENDPOINT = '/info/species'
            dict_information = su.get_info(ENDPOINT)

            #Tenemos que controlar los límites, si user introduce un límite mayor del esperado, imprimimos toda la lista
            #de especies, pero si introduce un número más pequeño de especies que las que hay en la lista, imprimimos sólo
            #las que nos pide

            try: #Intentamos imprimir los diccionarios que el user pide  Parameters: {'limit': ['10']}
                limit = arguments['limit'][0] #Es una lista por tanto cogemos sólo el elemento en posición 0
            except KeyError: #En el caso de que el límite fuera mayor del que nosotros tenemos o no hubieran introducido límite
                limit = len(dict_information)

            #Ahora tenemos que enviarle el contenido dict_information y el límite a la función que se encargue
            #de sacar la informacion de ese diccionario para posteriormente enviarla al html correspondiente.
            #Esta función se va a llamar def info_listSpecies():

            context = su.info_listSpecies(dict_information, limit)
            contents = read_template_html_file("./html/listSpecies.html").render(context=context) #lo naranja siempre
            # igual que el nombre que hay en la plantilla, y lo que hay detrás del igual, es la variable que le pasamos como argument

        elif path_name == '/karyotype':

            """Resource requested:  /karyotype
            Parameters: {'specie': ['mouse']}"""
            specie = arguments['specie'][0]

            ENDPOINT = '/info/assembly/' + str(specie)

            try: #Tenemos que controlar que la especie que introduce exista
                dict_information = su.get_info(ENDPOINT)  #Extraer la información de la especie deseada

                # Ahora tenemos que enviarle el contenido dict_information a la función que se encargue
                # de sacar la informacion de ese diccionario para posteriormente enviarla al html correspondiente.
                # Esta función se va a llamar def info_karyotype:
                context = su.info_karyotype(dict_information) #Nos devuelve la lista de cromosomas, es decir el cariotipo
                contents = read_template_html_file('./html/karyotype.html').render(context = context)

            except KeyError:
                contents = su.read_template_html_file("./html/error.html").render()

        elif path_name == '/chromosomeLength':

            """Resource requested:  /chromosomeLength
            Parameters: {'specie': ['mouse'], 'chromo': ['18']}"""

            specie = arguments['specie'][0]
            chromo = arguments['chromo'][0]

            #/info/assembly/homo_sapiens?content-type=application/json

            ENDPOINT = '/info/assembly/' + str(specie)

            try: #Tenemos que asegurarnos de que el cromosoma y la especie existan
                dict_information = su.get_info(ENDPOINT)
                context = su.info_chromoLength(dict_information, chromo)
                contents = read_template_html_file('./html/chromosomeLength.html').render(context=context)

            except KeyError:
                contents = su.read_template_html_file("./html/error.html").render()


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