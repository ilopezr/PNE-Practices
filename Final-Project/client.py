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
    #print(f"Response received!: {r1.status} {r1.reason}\n")
    # -- Read the response's body
    data1 = r1.read().decode("utf-8")  # This is a string
    # -- Create a variable with the data, form the JSON received
    received_data = json.loads(data1)  # This is a dictionary
    return received_data



# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)

try:
    ENDPOINT = "/listSpecies"
    PARAMETERS = "?limit=10&json=1"
    received_data = connect(ENDPOINT, PARAMETERS)

    print('The total number of species in the ensembl is:', termcolor.colored(received_data['number_species'], 'blue'))
    print('The limit you have selected is:', termcolor.colored(received_data['limit'], 'yellow'))
    print('The names of species are:')
    for specie in received_data['list_species']:
        print(termcolor.colored(specie, 'green'))

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

try:
    ENDPOINT = "/karyotype"
    PARAMETERS = "?specie=mouse&json=1"
    received_data = connect(ENDPOINT, PARAMETERS)
    print('The names of the choromosomes are:')
    for chromo in received_data['list_chromosomes']:
        print(termcolor.colored(chromo, 'white'))
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

try:
    ENDPOINT = "/chromosomeLength"
    PARAMETERS = "?specie=mouse&chromo=18&json=1"
    received_data = connect(ENDPOINT, PARAMETERS)
    print('The length os the chromosome is:', termcolor.colored(received_data['length'], 'red'))
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

try:
    ENDPOINT = "/geneSeq"
    PARAMETERS = "?gene=FRAT1&json=1"
    received_data = connect(ENDPOINT, PARAMETERS)
    print('The sequence for gene FRAT1 is:', termcolor.colored(received_data['seq'], 'green'))
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

try:
    ENDPOINT = "/geneInfo"
    PARAMETERS = "?gene=FRAT1&json=1"
    received_data = connect(ENDPOINT, PARAMETERS)
    print('Start:', termcolor.colored(received_data['start'], 'red'))
    print('End:', termcolor.colored(received_data['end'], 'green'))
    print('Length:', termcolor.colored(received_data['length'], 'blue'))
    print('Id:', termcolor.colored(received_data['id'], 'yellow'))
    print('Chromosome name:', termcolor.colored(received_data['chromosome_name'], 'red'))

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

try:
    ENDPOINT = "/geneCalc"
    PARAMETERS = "?gene=FRAT1&json=1"
    received_data = connect(ENDPOINT, PARAMETERS)
    print('Length:', termcolor.colored(received_data['length'], 'white'))
    print('Percentages:', termcolor.colored(received_data['percent'], 'green'))
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()








