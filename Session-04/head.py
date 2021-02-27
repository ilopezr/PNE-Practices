from pathlib import Path
FILENAME = "RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()
file_contents = file_contents[:file_contents.find('\n') + 1]

#Para leer el contenido de un archivo, el texto se almacena en la variable file_contents y despues lo imprimimos
print(file_contents)