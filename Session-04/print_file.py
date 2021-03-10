from pathlib import Path

# Constant with the new of the file to open
FILENAME = "RNU6_269P.txt"

#Open and read the entire file
file_contents = Path(FILENAME).read_text()

#Para leer el contenido de un archivo, el texto se almacena en la variable file_contents y despues lo imprimimos
print(file_contents)


