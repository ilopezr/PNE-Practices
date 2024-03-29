import socket
import termcolor
import pathlib
from urllib.parse import urlparse, parse_qs


def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content

# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080
HTML_ASSETS = "./html/"


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0] #GET /info/A HTTP/1.1
    request = req_line.split(' ')[1]
    o = urlparse(request)
    path_name = o.path
    arguments = parse_qs(o.query)
    print("Resource requested: ", path_name)
    print("Parameters: ", arguments)
    print(req_line)

    # -- Generate the response message
    # It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)

    # This new contents are written in HTML language
    body = ""

    # -- Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n" #Exercise 2

    if path_name == "/":
        body = read_html_file(HTML_ASSETS + "index.html")

    elif "/info/" in path_name:
        try:
            #Where is the letter? It is in path_name.split('/')[-1] so here we are going to take A G T C
            body = read_html_file(HTML_ASSETS + path_name.split('/')[-1] + '.html' )
            """if path_name == "/info/A":
                body = read_html_file(HTML_ASSETS + "A.html") #specify the path
            elif path_name == "/info/C":
                body = read_html_file(HTML_ASSETS + "C.html")
            elif path_name == "/info/G":
                body =  read_html_file(HTML_ASSETS + "G.html")
            elif path_name == "/info/T":
                body = read_html_file(HTML_ASSETS + "T.html")"""
        except FileNotFoundError:
            body = read_html_file(HTML_ASSETS + "Error.html")

    else:
        body = read_html_file(HTML_ASSETS + "Error.html")


    # -- Add the Content-Length
    header += f"Content-Length: {len(body)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()