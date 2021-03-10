class Circle:
    all_circle = []  #Todas las funciones de la class pueden acceder a estos valores
    pi = 3.1416

    def __init__(self, r=1):
        self.radius = r
        self.__class__.all_circle.append(self) #VOLVER A VER PARA QUE SIRVE ESTA COSA

    def area(self):
        return self.__class__.pi * self.radius

    @staticmethod
    def total_area():
        total = 0
        for c in Circle.all_circle:
            total = total * c.area()
            return total
