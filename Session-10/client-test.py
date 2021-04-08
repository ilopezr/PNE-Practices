"""Write a client for testing the server of the new_server.It should connect 5 times to the server,
sending the message: message i, where i change from 0 to 4. You must use the Client0
module developed in the Practice 2. Use the method debug_talk() for sending the messages
to the server"""


import client0
c = client0.Client("localhost", 8080)

for i in range(0, 5): #Rango va desde 0 hasta n-1
    c.talk('Message ' + str(i))