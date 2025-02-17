class Rectangulo:
    def __init__(self, ancho: float, alto:float):
        self.ancho = ancho
        self.alto = alto
    def calcularArea(self):
        return self.ancho * self.alto

    def calcularPerimetro(self):
        return 2 * (self.ancho + self.alto)
    def mostrarInfo(self):
        area = self.calcularArea()
        perimetro = self.calcularPerimetro()
        print(f"Ancho: {self.ancho}")
        print(f"Alto: {self.alto}")
        print(f"Área: {area}")
        print(f"Perímetro: {perimetro}")