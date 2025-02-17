class Coche:
    
    def __init__(self, marca: str, modelo: str, color: str):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, velocidad: int):
        self.velocidad += velocidad
        print(f"El coche se ha acelerado a {self.velocidad} km/h")

    def frenar(self, velocidad: int):
        self.velocidad -= velocidad
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"El coche se ha frenado a {self.velocidad} km/h")

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Velocidad: {self.velocidad} km/h")
