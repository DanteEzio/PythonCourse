"""Este programa calcula el area de un circulo
a = pi * r**2"""

import math

print("Este programa calcula el area de un circulo")
radio = float(input("Ingresa el valor del radio: "))

total = math.pi * radio**2

print("El area del circulo es: ","{:0.5f}".format(total) , "cm2")


"""print("Este programa calcula el area de un circulo")
radio = float(input("Ingresa el valor del radio: "))

pi = 3.1415922
total = pi * radio**2

print("El area del circulo es: ","{:0.5f}".format(total), "cm2")"""
