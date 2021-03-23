import socket

PORT = 8080
IP = "192.168.124.179"

while True:
    msg = input('Introduce your message...')

    #CREAMOS SOCKET Y CONECTAMOS AL SERVER
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    #LE MANDAMOS LA INFORMACION, HAY QUE PASARLA A BYTES CON STR.ENCODE()
    s.send(str.encode(msg))  # El encode lo transforma a bytes

    #CERRAMOS EL SOCKET
    s.close()
