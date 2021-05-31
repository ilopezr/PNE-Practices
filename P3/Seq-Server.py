import termcolor
import colorama
"""Para realizar el ejercicio no debemos cometer el fallo de escribirlo dentro de nuestro main program -- main loop.
Para evitar eso, creamos otro archivo """

import server_utils
import socket

list_sequences = ['AAACCCTTTT', 'GGGCCCTTT', 'AGTAGT', 'CTGCTG', 'ATATATA']

# Configure the Server's IP and PORT
PORT = 8080
IP = "localhost"  #Es lo mismo que poner 127.0.0.1, o poner "", este ultimo es peor, pero ambos son nuestro IP por defecto.

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
        (cs, client_ip_port) = ls.accept()  #CUANDO SE EJECUTA, SE ESTABLECE LA CONEXIÓN
        count_connections += 1
        client_adress_list.append(client_ip_port)
        print('New client connected!!')

    except KeyboardInterrupt:
        print('Server stopped by the user')
        ls.close()
        exit()

    # -- Read the message from the client
    # -- The received message is in raw bytes
    colorama.init(strip='False')
    msg_raw = cs.recv(2048)  #CUIDADO AQUI!!!
    #print(msg_raw)  #'PING \r\n' --tenemos que quitar esos carácteres, usando la funcion format_command en server_utils
#Lo imprimimos aquí porque si lo pasamos a string esos carácteres no se ven

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode()
    formatted_message = server_utils.format_command(msg)
    #print(termcolor.colored(formatted_message, 'green'))
    formatted_message = formatted_message.split(" ")
    print(formatted_message)#En el caso del GET 2, divide el mensaje en una lista con, 'GET' y con 2


    #Cuando tenemos una string, y usamos el split, este lo que hace es crear una lista con elementos separados por lo que hay dentro del paréntesis del split

    if len(formatted_message) == 1:
        command = formatted_message[0]
    else:
        command = formatted_message[0]
        argument = formatted_message[1]

    if command == "PING":
        server_utils.ping(cs)

    elif command == 'GET':
        try:
            server_utils.get(cs, list_sequences, argument)
        except IndexError:
            cs.send(str('Index out of range. Try again').encode())

    elif command == 'INFO':
        server_utils.info(cs, argument)

    elif command == 'COMP':
        server_utils.comp(cs, argument)

    elif command == 'REV':
        server_utils.rev(cs, argument)

    elif command == 'GENE':
        try:
            server_utils.gene(cs, argument)
        except UnboundLocalError:
            cs.send(str('Incorrect gene. Try with this ones: U5, ADA, FRAT1, FXN or RNU6_269P').encode())


    else:
        response = 'Not available command '
        cs.send(str(response).encode())

    # -- Close the data socket
    cs.close()