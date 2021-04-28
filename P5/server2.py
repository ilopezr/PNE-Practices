import http.server
import socketserver
import termcolor
import pathlib
import jinja2

def read_html_file(filename):

    content = pathlib.Path(filename).read_text()
    return content

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    #Estamos creando un template object que contenga un html file y tenemos que añadir el valor
    # de esos valores en ese template
    return content

# Define the Server's port
PORT = 8080

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
        termcolor.cprint(self.requestline, 'green') #GET /info/A HTTP/1.1
        termcolor.cprint(self.path, 'blue') #/info/A

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok


        if self.path == '/':
            contents = read_html_file('./html/index.html')

        elif '/info/' in self.path:
            base = self.path.split('/')[-1] #Ahora sabemos la base
            context = BASES_INFORMATION[base]
            context['letter'] = base #añadimos un key
            contents = read_template_html_file('./html/info/general.html').render(base_information = context)

            """El .render() lo que hace es reemplazar las variables de 'general.html por las que nosotros le digamos"""
            """            contents = read_html_file('./html/general.html').render(name = BASES_INFORMATION[base]['name'],
                                                                    formula= BASES_INFORMATION[base]['formula'],
                                                                    letter=BASES_INFORMATION[base],
                                                                    link = BASES_INFORMATION[base]['link'])"""

        elif self.path.endswith('.html'):
            #Try to open the file
            try:
                contents = read_html_file('/.html' + self.path)
            except FileNotFoundError: #Si el file no se encuentra dentro de la carpeta es porque no existe
                contents = read_html_file('./html/error.html')
        else:
            contents = read_html_file('./html/Error.html')


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html') #ESPECIFICAR EL CONTENIDO QUE ESTAMOS MANDANDO
        self.send_header('Content-Length', len(contents.encode()))

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