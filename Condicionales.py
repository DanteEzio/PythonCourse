# si x cosa es verdad haz esto, sino, haz lo otro

# No se usan llaves ni parentesis
calificacion = int(input('Cual es tu calificacion? '))
puntos_extras = False
# String vacio es Falsy, string con x cosa es Truthy
# None False
# Truthy o Falsy
# and or
# and: validar que ambos valores sean Truthy => True
# or: validar que minimo uno de los valores sea Truthy => True
if calificacion >= 7:
  print('Ya pasaste')
elif calificacion >= 5 and calificacion < 7:
  print('Si te rifas con un pomo, pasas')
# elif calificacion == 6 or puntos_extras:
#   print('Chance y pasas')
else:
  print('Ya ni vengas')