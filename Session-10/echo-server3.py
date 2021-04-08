#Modify the server of exercise 2 so that it stores the client's tuples (IP, PORT) in a list.
# After 5 clients has connected, it will print the information of all the clients in
# the console and finish

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

count_connections = 0
client_adress_list = []

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept() #CUANDO SE EJECUTA, SE ESTABLECE LA CONEXIÓN
        count_connections += 1
        client_adress_list.append(client_ip_port)

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
    response = 'ECHO ' + msg
    # -- The message has to be encoded into bytes
    cs.send(str(response).encode()) #La respuesta la transformamos a string porque siempre tiene que ser una string

    # -- Close the data socket
    cs.close()
    if count_connections == 5:
        for i in range(0, len(client_adress_list)):
            print('Client ' + str(i) + ': Client IP, PORT: '+ str(client_adress_list[i]))
        exit(0)

        """¿Por qué ponemos 0? 
        Hay tres formas de finalizar un programa: 
        - '0' cuando el programa finaliza con éxito sin errores, el programa está programado para finalizar. 
        - '-1' cuando el programa finaliza sin éxito manualmente 
        - '1' cuando el programa finaliza a causa de la aparición de una excepción """




