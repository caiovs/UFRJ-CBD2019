class Registro_GH(object):
    """docstring for Registro."""

    def __init__(self, dado):
        print("############", dado)
        dado = dado.split(',')
        print("******************/nDado :", type(dado),"      ",dado)
        print("dado[0]", dado[0])
        self.uhe = dado[0]
        print("dado[1]", dado[1])
        self.cenario = dado[1]
        print("dado[2]", dado[2])
        self.estagio = dado[2]
        print("dado[3]", dado[3])
        self.geracao = dado[3]

    def __repr__(self):
        return [self.uhe,self.cenario,self.estagio,self.geracao]

    def __str__(self):
        return str(self.__repr__())