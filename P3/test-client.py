from client0 import Client

# SERVER IP, PORT
PORT = 8080 #El port no tiene que ser usado por ninguna aplicación más
IP = "localhost"

client = Client(IP, PORT) #Client creado

correct = True
while correct:
    msg = input('Enter here the command you want to test: ').replace(' ', '').upper()

    if msg == 'EXIT':
        print('The process has finished correctly.')
        correct = False

    elif msg == 'PING':
        client.talk(msg)

    elif msg == 'GET':
        for i in range(0,5):
            client.talk(msg + ' ' + str(i))

    elif msg == 'INFO' or msg == 'COMP' or msg == 'REV':
        msg = msg + ' ' + str('AAACCCTTTT')  #client.talk('GET 0')
        client.talk(msg)

    elif msg == 'GENE':
        list_gene_names = ['U5', 'ADA', 'FRAT1', 'FXN' , 'RNU6_269P']
        for i in list_gene_names:
            client.talk(msg + ' ' + str(i))

    else:
        print('The command is not correct. Try with this ones: PING, GET, INFO, COMP, REV, GENE')



