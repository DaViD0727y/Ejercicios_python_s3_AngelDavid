# Ejercicio 4: Calcular e imprimir la tabla de multiplicar de un numero cualquiera

# Pedimos al usuario que ingrese el numero para calcular la tabla de multiplicar
numero = int(input("Ingrese un numero para calcular la tabla de multiplicar: "))

# Imprimimos el titulo de la tabla de multiplicar
print(f"Tabla de multiplicar del {numero}:")
print("-------------------------------")

# Calculamos y imprimimos la tabla de multiplicar
for i in range(1, 11):  # Iteramos desde 1 hasta 10
    producto = numero * i
    print(f"{numero} x {i} = {producto}")