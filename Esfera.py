#Volumen de una esfera 4/3pi * r ** 3
import math

Radio = float(input('Ingresa el radio en cm: '))
pi = 3.14

Volumen = (4/3 * math.pi) * (Radio ** 3)

print('El volumen de tu esfera es de: ', Volumen, 'cm3')
