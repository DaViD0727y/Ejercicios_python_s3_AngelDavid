n = int(input("Ingresa el número de autos que entraron a la ciudad: "))
colores = {'Amarillo': 0, 'Rosa': 0, 'Rojo': 0, 'Verde': 0, 'Azul': 0}

for _ in range(n):
    ultimo_digito = int(input("Ingresa el último dígito de la placa: "))
    if ultimo_digito in [1, 2]:
        colores['Amarillo'] += 1
    elif ultimo_digito in [3, 4]:
        colores['Rosa'] += 1
    elif ultimo_digito in [5, 6]:
        colores['Rojo'] += 1
    elif ultimo_digito in [7, 8]:
        colores['Verde'] += 1
    elif ultimo_digito in [9, 0]:
        colores['Azul'] += 1

for color, cantidad in colores.items():
    print(f"Color {color}: {cantidad}")