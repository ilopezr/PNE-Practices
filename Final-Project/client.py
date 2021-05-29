import http.client
import json
import termcolor

PORT = 8080
SERVER = '127.0.0.1'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

def connect(ENDPOINT, PARAMETERS):
    conn.request("GET", ENDPOINT + PARAMETERS)
    # -- Read the response message from the server
    r1 = conn.getresponse()
    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")
    # -- Read the response's body
    data1 = r1.read().decode("utf-8")  # This is a string
    print(data1)
    # -- Create a variable with the data, form the JSON received
    received_data = json.loads(data1)  # This is a dictionary
    return received_data


#First of all, we define a dictionary with all the endpoints and also with all the parameters.

dict_endp_params = {"/listSpecies":"?limit=10&json=1", "/karyotype":"?specie=mouse&json=1", "/chromosomeLength":"?specie=mouse&chromo=18&json=1",
                    "/geneSeq":"?gene=FRAT1&json=1", "/geneInfo":"?gene=FRAT1json=1", "/geneCalc":"?gene=FRAT1&json=1"}


# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)



try:  #/LISTSPECIES
    ENDPOINT = "/listSpecies"
    PARAMETERS = "?limit=10&json=1"
    received_data = connect(ENDPOINT, PARAMETERS)
    print(received_data)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

try:
    ENDPOINT = "/karyotype"
    PARAMETERS = "?specie=mouse&json=1"
    received_data = connect(ENDPOINT, PARAMETERS)
    print(received_data)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()












# Print the information in the object
#DO STUFF







