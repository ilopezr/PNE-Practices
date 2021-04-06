"""class Dog:
 def walk(self):
     return "*walking*"
 def speak(self):
    return "Woof!"
class JackRussellTerrier(Dog):
 def speak(self):
    return "Arff!"
bobo = JackRussellTerrier()
print(bobo.walk()) #Aqui está llamando a una funcion de dentro de dog, pero como es fuera de la función, y walk no usa atributos que no tenga jackrusselterrier, funciona."""



"""class A:
    def __init__(self, s= 'Welcome'):
        self.s = s

    def print(self):
        return self.s

a = A()
print(a.print())"""


"""class Grupos:
    def __init__(self):
        self.m = 'mecano'
        self.a = 'alaska'

    def duplicado(self):
        return self.m + self.m

class Mecano(Grupos):

    def __str__(self):
        print(self.m)  #Para hacer una llamada, si hay que poner el super(), sin embargo, a la hora de imprimir
                       #podemos hacer esto: A = Mecano()  print(A.duplicado())

A = Mecano()
A.__str__()"""

