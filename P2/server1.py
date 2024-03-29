import termcolor
import colorama

#WE ALWAYS RUN FIRST THE SERVER AND THEN THE CLIENT. Una vez que hemos run el server le damos boton derecho
# en la terminal,split right y runneamos el client.

#EL SERVER Y EL CLIENT MISMO PORT

import socket

# Configure the Server's IP and PORT
PORT = 12000 #El port no tiene que ser usado por ninguna aplicación más
IP = "127.0.0.1" #Standard IP recommendated to use, es el local host
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        colorama.init(strip='False')
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(termcolor.colored(msg, 'green')))

        # Send the messag
        message = termcolor.colored("Hello from the teacher's server", 'green')
        # We must write bytes, not a string
        clientsocket.send(message.encode())
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()