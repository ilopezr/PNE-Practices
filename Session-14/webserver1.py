import http.server
import socketserver

"""En este caso no estamos importando el socket, por qué? porque http.server y socketserver hacen uso del socket de 
por si, es decir, en ellos esta importado ya el modulo socket. """

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# -- Use the http.server Handler
Handler = http.server.SimpleHTTPRequestHandler #SimpleHTTPRequestHandler es una clase que entiende los mensajes en HTTPRequest

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    #Le pasamos una serie de argumentos a TCPServer, el primero es una tuppla ("", que es la IP localhost (donde va a estar el server)
    # y PORT). El segundo argumento es Handler que sabe como hacer frente a los mensajes http y por ello el TCPServer lo usa, para que le ayude el HTTP Request """

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server Stopped!")
        httpd.server_close()