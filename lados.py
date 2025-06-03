"""lado1 =float(input("ingrese el lado1 "))
lado2 =float(input("ingrese el lado2: "))
lado3 =float(input("ingrese el lado3: "))

if lado1 == lado2 == lado3:
    print("el triangulo es equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("el triangulo es isoceles")
else:
    print("el triangulo es escaleno")"""

lado1 = float(input("ingrese el lado1: "))
lado2 = float(input("ingrese el lado2: "))
lado3 = float(input("ingrese el lado3: "))

if lado1 < 0 or lado2 < 0 or lado3 < 0:
    print("valores invalidos")
else:
    hipotenusa = 0
    cateto1 = 0
    cateto2 = 0
    if lado1 > hipotenusa:
        hipotenusa = lado1
        cateto1 = lado2
        cateto2 = lado3
    if lado2 > hipotenusa:
        hipotenusa = lado2
        cateto1 = lado1
        cateto2 = lado3   
    if lado3 > hipotenusa:
        hipotenusa = lado3
        cateto1 = lado1
        cateto2 = lado2

    print(hipotenusa)
    hipotenusa = hipotenusa **2
    suma = cateto1 ** 2 + cateto2 ** 2

    print(hipotenusa)
    print(suma)

    if hipotenusa == suma:
        print("el triangulo es rectangulo")
    else:
        print("no es rectangulo")