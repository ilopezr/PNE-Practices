import socket
import termcolor
import colorama
# SERVER IP, PORT
PORT = 12000 #El port no tiene que ser usado por ninguna aplicación más
IP = "127.0.0.1"

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes IMPORTANTE
s.send(str.encode("HELLO FROM THE CLIENT!!!"))

# Receive data from the server
colorama.init(strip = 'False')
msg = s.recv(2048)
print("MESSAGE FROM THE SERVER:\n")
print(msg.decode("utf-8"))

# Closing the socket
s.close()