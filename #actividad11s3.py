#ejercicio 11: sistema que pida los datos de sexo,edad y altura
hombres = mujeres = suma_altura = mayores_170 = menores_150 = 0

#iniciamos variables para digitar la informacion 
while True:
    edad = int(input("Ingresa la edad (0 para terminar): "))
    if edad == 0:
        break
    sexo = input("Ingresa el sexo (H/M): ").upper()
    altura = float(input("Ingresa la altura: "))

    suma_altura += altura

    if sexo == 'H':
        hombres += 1
    elif sexo == 'M':
        mujeres += 1

    if altura > 1.70:
        mayores_170 += 1
    elif altura <= 1.50:
        menores_150 += 1

total_alumnos = hombres + mujeres

#imprimimos la informacion dada
if total_alumnos > 0:
    print(f"Hombres: {hombres}")
    print(f"Mujeres: {mujeres}")
    print(f"Altura promedio: {suma_altura / total_alumnos}")
    print(f"Alumnos con altura mayor a 1.70: {mayores_170}")
    print(f"Alumnos con altura menor o igual a 1.50: {menores_150}")