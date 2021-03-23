import termcolor
import socket
import colorama


#Socket sirve para poder crear la conexión
#Se puede importar dentro de la clase (o bien dentro de una def, o bien debajo de crear la class) pero asi también está bien


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self): #Sirve para ver si una pagina web funciona, si nos manda respuestas es que funciona
        print('Ok')

    def advanced_ping(self): #How the connections and messages are send, SOCKETS
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #crear el socket para crear la conexción, el socket es como el intermediario
        try:
            s.connect((self.ip, self.port))  #conectar el socket
            print('Server is up') #Nos confirma que estamos conectados a un server

            #Si ahora ponemos s.close() no pasaría nada, porque el socket ya está conectado

        except ConnectionRefusedError: #EXAMEN APRENDERNOS ESTA EXCEPCION
            print('Could not connect to the server') #esta excepción se dará cuando no runneamos el server primero, nos confirma que no estamos conectados a un server

    def __str__(self):
        return 'Connection to SERVER at ' + self.ip + ', PORT:' + str(self.port) #ESTA FUNCION ES NECESARIA PARA IMPRIMIR CUALQUIER STR, TOODO LO QUE SE RETURNEE HA DE SER STR

    def talk(self, msg):
        colorama.init(strip = 'False')
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data
        #print(termcolor.colored('To server:' + msg, 'yellow'))
        s.send(str.encode(termcolor.colored(msg, 'green'))) #encodeamos para convertir en bytes

        # Receive data, el 2048 es el numero de caracteres máximos que vamos a poder recibir
        response = s.recv(2048).decode("utf-8") #pasamos la respuesta desde bytes a string y la guardamos

        # Close the socket
        s.close()

        # Return the response del server
        return response

    def debug_talk(self, msg):
        colorama.init(strip='False')
        response_server = Client.talk(self, msg)
        print('To server: ', termcolor.colored(msg, 'blue'))
        print('From server: ', 2 * '\n', termcolor.colored(response_server, 'yellow'))

