# Ejercicio 1: Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros

# Inicializamos las variables para contar los números positivos, negativos y neutros
positivosCount = 0
negativosCount = 0
neutrosCount = 0

# Leemos 20 números del usuario
for i in range(20):
    numero = float(input(f"Ingrese el número {i+1}: "))

    # Verificamos si el número es positivo, negativo o neutro
    if numero > 0:
        positivosCount += 1
    elif numero < 0:
        negativosCount += 1
    else:
        neutrosCount += 1

# Imprimimos los resultados
print(f"Positivos: {positivosCount}")
print(f"Negativos: {negativosCount}")
print(f"Neutros: {neutrosCount}")