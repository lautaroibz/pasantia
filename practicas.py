"""num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
num3 = int(input("ingrese el tercer numero: "))

if num1 > 0 and num2 > 0 and num3 > 0:
    print(f"el cubo de {num1} es {num1 **3}")
    print(f"el cubo de {num2} es {num2 **3}")
    print(f"el cubo de {num3} es {num3 **3}")
else:
    print("todos los numero deben ser enteros positivos.")

"""


"""num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
num3 = int(input("ingrese el tercer numero: "))

if num1 > 0 and num2 > 0 and num3 > 0:
    cubo1 = num1**3
    cubo2 = num2**3
    cubo3 = num3**3

    print("El cubo del primer numero es", cubo1)
    print("El cubo del segundo numero es", cubo2)
    print("El cubo del tercer numero es", cubo3)
   
else:
    print("todos los numero deben ser enteros positivos.")"""


"""import random
suma = 0
num = int(input("ingrese numeros: "))
for i in range(5):
    numero = random.random(0 , 10) 
    print(f"Número {i+1}: {numero}")
    suma += numero

print(f"Suma total: {suma}")
"""
"""numeros = []
for i in range(5):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

menor = min(numeros)

print(f"El menor número es el {menor}")
"""


"""cantidad_pares = 0
cantidad_impares = 0
suma = 0
numeros = []

for i in range(6):
    num = int(input(f"ingrese el numero "))
    numeros.append(numeros)
    suma += num

    if num % 2  == 0:
        cantidad_pares +=1
    else:
        cantidad_impares +=1

promedio = suma / 6

print(f"Números pares:", cantidad_pares)
print(f"Números impares:", cantidad_impares)
print(f"Promedio total:", promedio)
"""

mayor = 0
contador_mayor = 0
menor = 0
contador_menor = 0

for i in range(10):
    num = int(input("Ingrese el número entero positivo " + str(i + 1) + ": "))
    
    while num < 0:
        print("Por favor, ingrese un número positivo.")
        num = int(input("Ingrese el número entero positivo " + str(i + 1) + ": "))

    if mayor is 0:
        mayor = num
        contador_mayor = 1
    else:
        if num > mayor:
            mayor = num
            contador_mayor = 1
        elif num == mayor:
            contador_mayor += 1

    if menor is 0:
        menor = num
        contador_menor = 1
    else:
        if num < menor:
            menor = num
            contador_menor = 1
        elif num == menor:
            contador_menor += 1

print("El número mayor ingresado es:", mayor)
print("Apareció", contador_mayor, "veces")
print("El número menor ingresado es:", menor)
print("Apareció", contador_menor, "veces")

