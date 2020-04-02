#Este programa genera la multiplicacion de dos numeros

primer_numero = float(input('Ingrese el primer numero: '))
segundo_numero = float(input('INgrese el segundo numero: '))

Resultado = primer_numero * segundo_numero

#Ejemplo de concatenacion con la forma "','{:decimales}' .format(Variable a calcular)"
print('El resultado de la multiplicacion es: ','{:0.3}'.format(Resultado))


