radio = float(input("ingrese radio: "))
altura = float(input("ingrese altura: "))

pi = 3.14

vol = pi*(radio**2)*altura

print(altura)

if (vol >= 300):
    print(vol)
else:
    print("el valor es incorrecto")
