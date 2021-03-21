#En el client anterior, enviamos informacion y cerramos la conexion

#En el client actual, nos conectamos al server, enviamos la info, y ejecutamos algo más,
#puesto que queremos recibir alguna info del server. Ahora hay una interacción entre ambos.

import socket

# SERVER IP, PORT
PORT = 8080
IP = "192.168.124.179"

# First, create the socket, EL ELEMENTO QUE NOS RELACIONA EL CLIENT Y EL SERVER
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))

# Receive data from the server
msg = s.recv(2048) #--- todoo lo que recibimos lo guardamos en msg, el numero ese es como el numero de caracteres máximos que podemos recibir
print("MESSAGE FROM THE SERVER:\n")
print(msg.decode("utf-8"))

# Closing the socket
s.close()