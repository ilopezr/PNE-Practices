# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT) #Creamos una http conection, nos conectamos al server

#conn es una clase que contiene los methods de HTTPConnection, entre ellos estan .request(), .getresponse()

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", "/") #Enviamos la request #Para imprimir el file que el server nos manda cuando ponemos '/'.

    #Si queremos imprimir el contenido que nos manda cuando ponemos /listusers pondríamos  conn.request("GET", "/listusers")

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n") #Accedemos al contenido de la respuesta del server y la imprimimos

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Print the received data
print(f"CONTENT: {data1}")