# Ejercicio 5: Calcular el promedio de peso de niños, jóvenes, adultos y ancianos
#definicion de variables
cantidadmuestras = 50 
edadniños= (0,12)
edadjovenes= (13,29)
edadadultos= (30,59)
edadancianos=(60, float("inf"))#60 e adelante

# Inicializamos las variables para almacenar los pesos y edades
pesosNiños = []
pesosJovenes = []
pesosAdultos = []
pesosAncianos = []

# Leemos las edades y pesos de las 50 personas
for i in range(50):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    peso = float(input(f"Ingrese el peso de la persona {i+1} (en kg): "))

    # Clasificamos la persona según su edad
    if edad <= 12:
        pesosNiños.append(peso)
    elif edad <= 29:
        pesosJovenes.append(peso)
    elif edad <= 59:
        pesosAdultos.append(peso)
    else:
        pesosAncianos.append(peso)

# Calculamos el promedio de peso para cada categoría
promedioNiños = sum(pesosNiños) / len(pesosNiños) if pesosNiños else 0
promedioJovenes = sum(pesosJovenes) / len(pesosJovenes) if pesosJovenes else 0
promedioAdultos = sum(pesosAdultos) / len(pesosAdultos) if pesosAdultos else 0
promedioAncianos = sum(pesosAncianos) / len(pesosAncianos) if pesosAncianos else 0

# Imprimimos los resultados
print("Promedios de peso:")
print(f"Niños: {promedioNiños:.2f} kg")
print(f"Jóvenes: {promedioJovenes:.2f} kg")
print(f"Adultos: {promedioAdultos:.2f} kg")
print(f"Ancianos: {promedioAncianos:.2f} kg")