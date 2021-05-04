import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-1.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring) #Acceder al people-1.json, lee todo_ el contenido de people-1.json
# y lo convierte en un diccionario llamado person


# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# -- Read the Firtname
firstname = person['Firstname'] #coger el valor de la key firstname,
# para almacenarlo en una variable en forma de string y posteriormente hacer lo que quiera con ella

lastname = person['Lastname']
age = person['age']

# Print the information on the console, in colors
print()
termcolor.cprint("Name: ", 'green', end="")
print(firstname, lastname)
termcolor.cprint("Age: ", 'green', end="")
print(age)