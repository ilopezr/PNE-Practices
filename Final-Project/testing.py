import http.client
import json

def test(ENDPOINT, PARAMETERS, SERVER, PORT):
    conn = http.client.HTTPConnection(SERVER, PORT)
    try:
        conn.request("GET", ENDPOINT + PARAMETERS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

"""    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")

    # -- Create a variable with the data,
    # -- form the JSON received
    datajson = json.loads(data1)
    return datajson"""