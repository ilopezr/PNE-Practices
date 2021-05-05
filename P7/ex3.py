import http.client
import json

DICT_GENES = {'FRAT1':'ENSG00000165879',
              'ADA': 'ENSG00000196839',
              'FXN':'ENSG00000165060',
              'RNU6_269P':'ENSG00000212379',
              'MIR633':'ENSG00000207552',
              'TTTY4C':'ENSG00000226906',
              'RBMY2YP':'ENSG00000227633',
              'FGFR3':'ENSG00000068078',
              'KDR':'ENSG00000128052',
              'ANK2':'ENSG00000145362'}

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
ID = DICT_GENES['MIR633']
PARAMETERS  ='?content-type=application/json'

connection = http.client.HTTPConnection(SERVER)
connection.request('GET' ,ENDPOINT + ID + PARAMETERS)

response = connection.getresponse()
print('Response received!', response.status, response.reason)


if response.status == 200: #Esto es simplemente para evitar fallos en la conexión y por si nos equivocamos al escribir el '/sequence/id/'
    response = json.loads(response.read().decode())
    #print(response)


    """Se imprime asi:  {'id': 'ENSG00000207552', 'molecule': 'dna', 'version': 1, 'desc': 'chromosome:GRCh38:17:62944215:62944312:1', 'query': 'ENSG00000207552', 'seq': 'AACCTCTCTTAGCCTCTGTTTCTTTATTGCGGTAGATACTATTAACCTAAAATGAGAAGGCTAATAGTATCTACCACAATAAAATTGTTGTGAGGATA'}"""

    #print(json.dumps(response, indent=4, sort_keys=True)) #Lo transforma en una string y despues hace que se imprima de una mejor manera

    """{
        "desc": "chromosome:GRCh38:17:62944215:62944312:1",
        "id": "ENSG00000207552",
        "molecule": "dna",
        "query": "ENSG00000207552",
        "seq": "AACCTCTCTTAGCCTCTGTTTCTTTATTGCGGTAGATACTATTAACCTAAAATGAGAAGGCTAATAGTATCTACCACAATAAAATTGTTGTGAGGATA",
        "version": 1
    }"""

    print('Gene:', ID)
    print('Description: ', response['desc'])
    print('Bases: ' , response['seq'])

    """Ahora se imprime así:
    Gene: ENSG00000207552
    Description:  chromosome:GRCh38:17:62944215:62944312:1
    Bases:  AACCTCTCTTAGCCTCTGTTTCTTTATTGCGGTAGATACTATTAACCTAAAATGAGAAGGCTAATAGTATCTACCACAATAAAATTGTTGTGAGGATA"""

elif response.status == 404:
    print('Check if the ENDPOINT was correctly written')