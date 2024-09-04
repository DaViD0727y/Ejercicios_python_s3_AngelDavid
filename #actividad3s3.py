# Ejercicio 3: Calcular el promedio y la calificación más alta y más baja de un grupo de 20 alumnos

# Inicializamos las variables para almacenar las calificaciones
calificaciones = []

# Leemos las calificaciones de los 20 alumnos
for i in range(20):
    calificacion = float(input(f"Ingrese la calificación del alumno {i+1}: "))
    calificaciones.append(calificacion)

# Calculamos el promedio de las calificaciones
promedio = sum(calificaciones) / len(calificaciones)

# Encontramos la calificación más alta y más baja
calificacionAlta = max(calificaciones)
calificacionBaja = min(calificaciones)

# Imprimimos los resultados
print(f"Promedio del grupo: {promedio:.2f}")
print(f"Calificación más alta: {calificacionAlta:.2f}")
print(f"Calificación más baja: {calificacionBaja:.2f}")