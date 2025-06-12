"""
ejercicio practico 1

def calcular_temp(temp_max, temp_min):
    return (temp_max + temp_min) / 2

if __name__ == "__main__":
    cant_dias = int(input("Ingrese la cantidad de días a consultar: "))

    for i in range(cant_dias):
        temp_max = float(input(f"Ingrese la temperatura máxima del día {i+1}: "))
        temp_min = float(input(f"Ingrese la temperatura mínima del día {i+1}: "))

        temp_media = calcular_temp(temp_max, temp_min)

        print(f"La temperatura media del día {i+1} fue {temp_media:.2f}°C")
"""

"""
ejercico practico 2

def convertirEspaciado(texto):
    texto_sin_salto = texto.strip()  
    texto_espaciado = ' '.join(texto_sin_salto)  
    return texto_espaciado

def main():
    texto_usuario = input("Introduce un texto: ")
    resultado = convertirEspaciado(texto_usuario)
    print("Texto con espaciado:")
    print(resultado)

if __name__ == "__main__":
    main()
"""

"""
ejercicio practico 3

def calcularMaximo(lista_numeros):
    maximo = max(lista_numeros)
    minimo = min(lista_numeros)
    return maximo, minimo

def main():
    lista = []
    
    cantidad = int(input("¿Cuántos números vas a ingresar? "))
    
    for i in range(cantidad):
        numero = int(input(f"Ingrese el número {i+1}: "))
        lista.append(numero)
    
    maximo, minimo = calcularMaximo(lista)
    
    print(f"El número máximo es: {maximo}")
    print(f"El número mínimo es: {minimo}")

if __name__ == "__main__":
    main()
"""
"""
ejercicio practico 4

def contar_pares_impares(lista):
    cantidad_pares = 0
    cantidad_impares = 0

    for numero in lista:
        if numero % 2 == 0:
            cantidad_pares = cantidad_pares + 1
        else:
            cantidad_impares = cantidad_impares + 1

    print("Cantidad de números pares en la lista:", cantidad_pares)
    print("Cantidad de números impares en la lista:", cantidad_impares)

    return cantidad_pares, cantidad_impares

numeros_de_ejemplo = [10, 15, 22, 33, 40, 56, 58, 73, 80, 91]

resultado = contar_pares_impares(numeros_de_ejemplo)
"""

