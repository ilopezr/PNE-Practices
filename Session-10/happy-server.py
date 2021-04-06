"""CREATING A SERVER : The steps that should be followed to setup a working server are:
Step 1: Create the socket (Method socket())
Step 2: Configure the socket: bind it to the remote IP and PORT (Method bind()
Step 3: Configure the socket in listening mode (Method listen())
Main loop:
Step 5: Wait for a client to connect (method accept())
Step 6: When a client connects, the socket library creates a new socket for communicating with the client
Step 7: Read the client messages. What does the client want? (metho rcv)
Step 8: Process the request and send a response message (method send) """

import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "localhost" #Es lo mismo que poner 127.0.0.1, o poner "", este ultimo es peor, pero ambos son nuestro IP por defecto.

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

# -- Waits for a client to connect
print("Waiting for Clients to connect")
(cs, client_ip_port) = ls.accept()

"""Si no se conecta nadie no sigue. Para que se conecte tenemos que irnos a la terminal 
del ordenador y poner cd Downloads despues cd nc y despues cd nc. Luego ponemos 
cd localhost 8080 y despues runneas el happy-server.py OJO! cd localhost porque el port de este server es localhost, 
si fuera otro pondriamos el otro. """

print("A client has connected to the server!")


"""Si nos saliera OSError: [Errno 98] Address already in use o Si nos saliera que no tenemos permiso:
Esto se debe a que el sistema operativo aún no ha liberado el puerto. A veces, se tarda uno o dos minutos en liberarlo. 
Una solución es simplemente cambiar el puerto del servidor a otro. Por ejemplo 8081. Luego, ejecútelo de nuevo.

Otra solución es configurar el socket para que las direcciones se puedan reutilizar.
Debe agregar esta línea debajo de las creaciones de socket: ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1

"""

# -- Read the message from the client
# -- The received message is in raw bytes
msg_raw = cs.recv(2048)

# -- We decode it for converting it
# -- into a human-redeable string
msg = msg_raw.decode()

# -- Print the received message
print(f"Received Message: {msg}")

# -- Close the socket
ls.close()
