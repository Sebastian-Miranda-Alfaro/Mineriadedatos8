#Ejercicio 1
n = int(input("Ingresa un numero del 1 al 10  "))
suma = 0
for i in range(1,n+1):
    suma += i
print(f"El total es {suma}") 
#Ejercicio 2
multi = 1
for i in range(1,n+1):
    multi *= i
print(f"El total es {multi}") 
#Ejercicio 3
m=0
for i in range(1,11,1):
   m=i*n
   print(str(n)+" x "+str(i)+" = "+str(m)+"\n")
#Ejercicio 4
i=0
suma1=0
prom=1
while(i<4):
    materia=int(input(f"Calificación {i+1}: "))
    suma1+=materia
    prom=suma1/4
    i+=1
print("El promedio es: "+str(prom))    
#Ejercicio 5
def fibonacci(n):
    a, b = 0, 1  
    for i in range(n):
        print(a)  
        a, b = b, a + b  
    else:
        print("Serie de Fibonacci")  
        
N = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
fibonacci(N)

#Ejercicio 6
num=int(input("\nDame un numero "))
exp=int(input("Dame un exponente "))
res=1
for i in range(1,exp+1):
    res=res*num
print(f"El resultado es: {res}")
#Ejercicio 7
a=int(input("Ingresa el primer valor "))
b=int(input("Ingresa el segundo valor "))
suma2=0

for  i in range (a,b+1,1):
    if(i%2==0):
        suma2+=i
print(f"El resultado de lo números pares de entre {a} y {b} es: {suma2}" )
    