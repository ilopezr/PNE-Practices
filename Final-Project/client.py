import http.client
import json
import termcolor

PORT = 8080
SERVER = '127.0.0.1'
ENDPOINT = "/listSpecies"
PARAMETERS = "?limit=10&json=1"

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + PARAMETERS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")
print(data1)

# -- Create a variable with the data,
# -- form the JSON received
person = json.loads(data1)
print(person)

# Print the information in the object
#DO STUFF






