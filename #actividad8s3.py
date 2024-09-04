# Ejercicio 8: Algoritmo para calcular calificaciones de estudiantes

# Inicializar variables para almacenar la cantidad de estudiantes en cada rango de calificación
below50 = 0
fiftyToSixtyNine = 0
seventyToSeventyNine = 0
eightyOrAbove = 0

# Iterar a través de cada uno de los 23 estudiantes
for i in range(23):
  # Pedir al usuario que ingrese la calificación del estudiante
  while True:
    try:
      grade = int(input(f"Ingrese la calificación para el estudiante {i + 1}: "))
      if grade < 1 or grade > 100:
        print("Calificación inválida. Por favor, ingrese una calificación entre 1 y 100.")
      else:
        break
    except ValueError:
      print("Entrada inválida. Por favor, ingrese un número entero.")

  # Actualizar la cantidad de estudiantes en cada rango de calificación
  if grade < 50:
    below50 += 1
  elif grade < 70:
    fiftyToSixtyNine += 1
  elif grade < 80:
    seventyToSeventyNine += 1
  else:
    eightyOrAbove += 1

# Imprimir los resultados
print(f"Estudiantes con una calificación menor a 50: {below50}")
print(f"Estudiantes con una calificación de 50 o más pero menor que 70: {fiftyToSixtyNine}")
print(f"Estudiantes con una calificación de 70 o más pero menor que 80: {seventyToSeventyNine}")
print(f"Estudiantes con una calificación de 80 o más: {eightyOrAbove}")