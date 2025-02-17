from Cuenta import CuentaBancaria

nombre = input("Ingresa el nombre del titular: ")
cuenta = CuentaBancaria(nombre)

# Menú
while True:
    print("\nOpciones:")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Mostrar saldo")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == '1':
        cantidad = float(input("Ingresa la cantidad a depositar: "))
        cuenta.depositar(cantidad)
    elif opcion == '2':
        cantidad = float(input("Ingresa la cantidad a retirar: "))
        cuenta.retirar(cantidad)
    elif opcion == '3':
        cuenta.mostrarSaldo()
    elif opcion == '4':
        print("Saliendo del programa.")
        break 
    else:
        print("Opción no válida.")
print("Programa finalizado.")