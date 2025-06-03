colores = {
    "az": "verde",
    "za": "verde",
    "ar": "naranja",
    "ra": "naranja",
    "zr": "violeta",
    "rz": "violeta",
}

valor = input("ingrese dos letras para ve el color producido: ")
if valor in colores:
    print(colores(valor))
