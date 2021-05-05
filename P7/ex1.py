"""Para conectarnos a una pagina we no hace falta meternos en el browser, podemos
hacerlo desde pycharm de la siguiente manera:"""


import http.client #Import the package
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMS  ='?content-type=application/json'

#Establish connection with the server
connection = http.client.HTTPConnection(SERVER)

#A traves del modulo creamos querys
connection.request('GET', ENDPOINT + PARAMS) #Dentro de los paréntesis añadimos el tipo de query, GET, y el endpoint + parametros del query

response = connection.getresponse()
print(response) #<http.client.HTTPResponse object at 0x0000015257019250> eso es lo que se imprime

#Si recordamos, asi es como se imprimían los objets, entonces para imprimirlo bien hacemos

#print(response.read()) #Ahora se imprime esto b'{"ping":1}'

"""La b representa que la informacion que estamos recibiendo está en bytes """

#print(response.read().decode()) #Ahora se imprime {"ping":1}

answer_decoded = response.read().decode() #Recordar que cuando decodeamos tenemos una string
print(type(answer_decoded), answer_decoded)

#El módulo que transforma str en diccionarios es el jason module
dict_response = json.loads(answer_decoded)
print(type(dict_response), dict_response)

if dict_response['ping'] == 1:
    print('PING OK!! The database is running')
else:
    print('Database is down!! ')

"""Hay muchas cosas que podemos extraer de la respuesta. """