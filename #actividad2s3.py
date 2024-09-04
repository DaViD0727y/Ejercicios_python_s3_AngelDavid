# Ejercicio 2: Leer 10 números negativos, convertirlos a positivos e imprimir la suma de dichos números

# Inicializamos la variable para la suma de los números positivos
sumaPositivos = 0

# Leemos 10 números negativos del usuario
for i in range(10):
    numeroNegativo = float(input(f"Ingrese el número negativo {i+1}: "))

    # Verificamos si el número es negativo
    if numeroNegativo < 0:
        # Convertimos el número negativo a positivo
        numeroPositivo = abs(numeroNegativo)

        # Sumamos el número positivo a la suma total
        sumaPositivos += numeroPositivo
    else:
        print("Error: El número ingresado no es negativo. Intente nuevamente.")
        i -= 1  # Restamos 1 a la variable i para que el bucle vuelva a pedir el número

# Imprimimos la suma de los números positivos
print(f"La suma de los números positivos es: {sumaPositivos}")