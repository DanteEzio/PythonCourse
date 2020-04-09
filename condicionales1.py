#Este programa nos permite saber si un alumno paso o reprobo


calificacion = int(input("Ingresa la calificacion del alumno: "))
puntos_extras = True

if calificacion > 7:
  print("El alumno aprobo")

elif calificacion >= 5 and calificacion <= 7:
  print("Si quieres pasar necesitas hacer un trabajo extra")

#elif calificacion >= 6 or puntos_extras:
#print("Chance y pasas")
else:
  print("El alumno reprobo")
