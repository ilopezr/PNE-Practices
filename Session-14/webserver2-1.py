"""La diferencia entre el webserver1 y este, es que ahora en este está en en Handler

ANTES : Handler = http.server.SimpleHTTPRequestHandler
AHORA : Handler = TestHandler

Testhandler() ahora es una clase que hemos creado (es una child class de http.server.BaseHTTPRequestHandler), y
por ello va a heredar todos los parámetros y métodos del http.server.BaseHTTPRequestHandler, tambien puede tener
nuevos methods, que harán que la respuesta hacia el browser sea una u otra dependiendo de la request del client.

 Esta clase lo que hace es definir todo_ aquello que pasa una vez que recibimos una HTTP request. """

import http.server
import socketserver

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    """Una vez que el server recibe un GET, ese mensaje va a ser pasado a TestHandler que a su ves hereda todo_ lo de
    BaseHTTPRequestHandler y va a hacer que el server que haga algo determinado al recibir ese mensaje (do_GET), es decir,
    el server va a responder algo determinado cuando en el browser """


    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # AQUI DENTRO ESTÁ LA RESPUESTA DEL SERVER We just print a message
        print("GET received!")

        #Se imprime muchas veces porque el browser intenta acceder a la respuesta muchas veces hasta que ve que en realidad no se puede

        # IN this simple server version:
        # We are NOT processing the client's request
        # We are NOT generating any response message
        return

# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd: #Handler es uan clase que tenemos que programar y en ella podemos definir methods que van a ser eecutados cuando el http request,llegue al server

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever() #es muy parecido a bind() y listen()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()