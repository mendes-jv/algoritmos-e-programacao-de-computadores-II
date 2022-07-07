class Retangulo:

    def setTamanho(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento

    def perimetro(self):
        self.perimetro = (largura + comprimento) * 2
        print(self.perimetro)

    def area(self):
        self.area = largura * comprimento
        print(self.area)
        