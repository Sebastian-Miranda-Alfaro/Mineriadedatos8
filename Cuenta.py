class CuentaBancaria:
    
    def __init__(self, titular: str, saldo: float = 0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad: float):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Saldo actual: ${self.saldo:.2f}, Se han depositado ${cantidad:.2f}")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad: float):
        if cantidad > self.saldo:
            print("Fondos insuficientes.")
        elif cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que 0.")
        else:
            self.saldo -= cantidad
            print(f"Se han retirado ${cantidad:.2f}. Saldo actual: ${self.saldo:.2f}")

    def mostrarSaldo(self):
        print(f"Titular: {self.titular}, Saldo actual: ${self.saldo:.2f}")