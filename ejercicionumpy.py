import numpy as np 
from numpy import random
'''Crea un array de 10 números aleatorios enteros entre 0 y 100.'''
a1 = np.array(random.randint(0,101, size=10))
print(a1)
'''Crea un array de 5 números aleatorios decimales entre 0 y 1.'''
a2 = np.array(random.rand(5))
print(a2)
'''Crea dos arrays de números aleatorios enteros de longitud 5 y concaténalos.'''
a3 = np.array(random.randint(0,101, size=5))
a4 = np.array(random.randint(0,101, size=5))
c=np.concatenate((a3,a4))
print(c)
'''Crea un array de 10 números aleatorios enteros y sepáralo en dos arrays de 5 elementos cada uno.'''
a5 = np.array(random.randint(0,101, size=10))
s=np.split(a5,2)
print(s)
'''Crea una matriz de 3x3 con números aleatorios decimales entre 0 y 1.'''
m = np.array(random.rand(3, 3))
print(m)
'''Crea un array de 10 números aleatorios enteros y selecciona 3 elementos al azar.'''
a6 = np.array(random.randint(0,101, size=10))
print(random.choice(a6,3))
'''Crea un array de 10 números aleatorios enteros entre 0 y 100 y calcula la media.'''
a7 = np.array(random.randint(0,101, size=10))
media = np.mean(a7)
print(f"La media es {media}")