# Ejercicio 6: Calcular la cantidad de hombres y mujeres presentes en un salón de clases

# Pedimos al usuario que ingrese el número total de personas en el salón de clases
totalPersonas = int(input("Ingrese el número total de personas en el salón de clases: "))

# Inicializamos las variables para contar los hombres y mujeres
hombres = 0
mujeres = 0

# Leemos el género de cada persona
for i in range(totalPersonas):
    genero = input(f"Ingrese el género de la persona {i+1} (H/M): ")

    # Contamos los hombres y mujeres
    if genero.upper() == "H":
        hombres += 1
    elif genero.upper() == "M":
        mujeres += 1
    else:
        print("Género inválido. Por favor, ingrese H para hombre o M para mujer.")

# Imprimimos los resultados
print("Cantidad de personas por género:")
print(f"Hombres: {hombres}")
print(f"Mujeres: {mujeres}")