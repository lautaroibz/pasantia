"""
Ejercicio 1

lista=[20, 10, 5, 50, 18, 7, 20, 1, 99, 119]
num = 7
maximo = 0

for item in lista:
    if item > maximo:
        maximo = item

print("el numero mayor es: ", maximo)
"""

"""
ejercicio 2

lista=[20,10,50,18,7,91,119]
bandera=0
for i in range(0,len(lista)):
    if lista[i]==7:
        bandera=1
        print("el numero 7 esta en la lista")
        break
if bandera==0:
    print("el numero 7 no esta en la lista")
"""

"""
ejercicio 3

import math 

num=float(input("ingrese un numero: "))
raiz=math.sqrt(num)
print(raiz)
"""
"""
ejercicio 4

import math

num = float(input("ingrese un numero: "))
raiz=math.sqrt(num)
divisible = False
for i in range (2, int(raiz)):
    if num%i==0 :
        divisible=True
        break
if divisible==False :
    print("es primo")
else :
    print("no es primo")
"""

""""
ejercicio 5

import math 

num=int(input("ingrese un numero: "))
factorial=math.factorial(num)

print(f"el numero factorial de {num} es {factorial}")
"""


""""import math

angulo=(input("ingrese un angulo en grados: "))
angulo=float(angulo.replace("°",""))
angulo= math.radians(angulo)
sin= math.sin(angulo)
print(sin)
cos=math.cos(angulo)
print(cos)
tan=math.tan(angulo)
print(tan) 
"""


