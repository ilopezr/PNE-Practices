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

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        print("A client has connected to the server!")

    except KeyboardInterrupt:
        print('Server stopped by the user')
        ls.close()
        exit()

    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode()

    # -- Print the received message
    print(f"Message received: {msg}")

    # -- Send a response message to the client
    try:
        response = int(msg) ** int(msg) #msg es una string, por lo que para hacer eso lo pasamos a integer

        # -- The message has to be encoded into bytes
        cs.send(str(response).encode()) #La respuesta la transformamos a string porque siempre tiene que ser una string
    except ValueError:
        cs.send('We need a number'.encode())

    # -- Close the data socket
    cs.close()
