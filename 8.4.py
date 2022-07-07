class Animal:
    """representa um animal"""

    def __init__(self, especie='animal', linguagem='emite sons'):
        self.esp = None
        self.ling = None

    def setEspecie(self, espécie):
        """define a espécie do animal"""
        self.esp = espécie

    def setLinguagem(self, linguagem):
        """define a linguagem do animal"""
        self.ling = linguagem

    def fla(self):
        """ exibe uma sentença pelo animal"""
        print('IEu sou um {} e sei {}'.format(self.esp, self.ling))
