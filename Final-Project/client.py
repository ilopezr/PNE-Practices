import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:

    path_name = input('Please enter here a path')

    if path_name == '/listSpecies': #http://127.0.0.1:8080/listSpecies?limit=10
        try:
            limit = str(int(input('Enter here a limit: ')))
            request = path_name + '?limit=' + limit + '&json=1'

        except ValueError:
            print('The limit must be a number')

    elif path_name == '/karyotype':                 #http://127.0.0.1:8080/karyotype?specie=lion
        specie = str(input('Enter here a specie: '))
        request = path_name + '?specie=' + specie + '&json=1'

    elif path_name == '/chromosomeLength':            #http://127.0.0.1:8080/chromosomeLength?specie=mouse&chromosome=18
        specie = str(input('Enter here a specie: '))
        chromo = str(input('Enter here a chromo: '))

        request = path_name + '?specie=' + specie + '&chromosome=' + chromo + '&json=1'


    elif path_name == '/geneSeq' or path_name == '/geneInfo' or path_name == '/geneCalc':   #http://127.0.0.1:8080/geneSeq?gene=FRAT1
        gene = str(input('Enter here a gene: '))
        request = path_name + '?gene=' + gene + '&json=1'

    conn.request("GET", request)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
#r1 = conn.getresponse()

# -- Print the status line
#print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
#data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
#content = json.loads(data1)
#print(content)

print("CONTENT: ")

# Print the information in the object
