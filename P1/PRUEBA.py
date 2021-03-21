class Nombres:
    def __init__(self, nombrechica, nombrechica2):
        self.chica = nombrechica
        self.chica2 = nombrechica2

    def len(self):
        return len(self.chica2)

    def condicion(self):
        if self.len() == 3:
            print('3!')
        else:
            print('!=3')

objeto = Nombres('Ana', 'Yun')
objeto.condicion()

