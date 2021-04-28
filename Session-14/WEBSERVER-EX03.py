import http.server
import socketserver
import termcolor

from server import read_html_file
HTML_ASSETS = "./html/"

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):


    """Como nuestra clase TestHandler hereda todos los methods de http.server.BaseHTTPRequestHandler.

    In our TestHandler Class we can use the following methods for generating the response very easily:

    self.send_response(code) : Creates a response header with a status line with the error CODE passed as an argumento.
    The response is not really sent yet, but stored into a buffer. The status codes can be found in this link
    self.send_header(): Add a header to the response message (Ex. Content-Type, Content-Length...)
    self.end_headers(): Add a blank line to the response message (indicating that the header is finished)"""


    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        file_name = self.path.strip('/')
        try:
            if file_name == "" or file_name == "index.html":
                contents = read_html_file(HTML_ASSETS + 'index.html')
            else:
                contents = read_html_file(HTML_ASSETS + file_name)
        except FileNotFoundError:
            contents = read_html_file(HTML_ASSETS + 'error.html')


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers() #Cada vez que enviamos un header luego tenemos que terminar de enviarlo,
        #crea una línea vacía indicando que el header ha terminado

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