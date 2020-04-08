# For

for i in range(5): #Empieza en 0 y termina en 5
  # for(var i = 0; i < 5; i++)
  print('Hola usuario', i)

print('===============================')
print('Tabla del 4')
for i in range(1, 10): #Empieza en 1 y termina en 10
  # for(var i = 0; i < 10; i++)
  # Tabla del 4
  print(f'4 x {i} = {4*i}')

print('===============================')
print('Numeros pares hasta el 50')
for i in range(0, 52, 2):
  print(i)


print('===============================')
print("Lista de egresados")
persons = ["Arturo", "David", "Topi", "Martin"]

for person in persons:
  print('Ing.', person)

print('===============================')
print('Estudiantes y sus calificaciones')
students = [
  ['Martin', [10, 10, 10]],
  ['Arturo', [7, 8, 9]],
  ['Chocha', [5, 10, 3]],
  ['Topa', [10, 8, 7]],
  ['Tablón', [6, 0, 10]],
]

for student in students:
  print('###################')
  print('Nombre del alumno:', student[0])
  print('Calificaciones')

  notes = student[1]

  # Acceder a cada una de las calificaciones de cada estudiante
  # Mostrar cada una
  # Obtener el promedio
  # Si su promedio es mayor que 6, imprimir en la consola 'APROBADO', sino, imprimir 'REPROBADO'
  # sum() Toma una lista de numeros y hace la suma de todos

  for i, note in enumerate(notes): 
      print(f'Calificacion #{i + 1}: {note}')

  average = sum(notes)/len(notes)
  print(f'PROMEDIO: {average:.2f} - {"APROBADO" if average > 6 else "REPROBADO"}')
