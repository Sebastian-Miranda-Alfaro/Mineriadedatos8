num = int(input("Ingresa un numero "))
if num %2 ==0 :
    print("Es par")
else :
    print("Es impar")

#EJERCICIO 2

if num<0:
    print("Es negativo")
else :
   print("Es positivo")

#EJERCICIO 3
edad = int(input("Ingresa tu edad "))
if edad >=18:
    print("Mayor de edad")
else:
    print("Menor de edad")

#Ejercicio 4
calif = int(input("Ingrese una calificacion "))
if calif>=60:
    print("Aprobado")
else :
   print("Reprobado")

#Ejercicio 5
if(calif>=90 and calif<=100):
    print("A")
elif(calif>=80 and calif<=89):
    print("B")
elif(calif>=70 and calif<=79):
    print("C")
elif(calif>=60 and calif<=69):
    print("D")
else:
    print("F")
#Ejercicio 6
temp=int(input("Ingresa la temperatura en Celsius "))
if(temp<0):
    print("Es solido")
elif(temp>0 and temp<100):
    print("Es liquido")
else:
    print("es vapor")