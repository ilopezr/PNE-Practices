class Dog:
    def __init__(self, the_name, the_age): #self is where we store the attributes
        self.name = the_name
        self.age = the_age   #name and age are the attributtes

    def sit(self): #no es una funcion, es un method of the class, y es compulsory poner en () el self 
        print('This is {}, and Im sitting down here'.format(self.name))

    def set_name(self, name):
        self.name = name
        print('This is {}, and Im sitting down here'.format(self.name))


ares = Dog('ares', 10) #name, age
toby = Dog('toby', 21)

ares.name ='trueno' #accedemos al attribute y lo modificamos
ares.age = 1
ares.set_name('toby') #Así es como entramos a un method de una class
print(ares.name)