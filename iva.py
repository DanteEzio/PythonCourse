#El usuario ingrese el precio del producto
#Se le muestra al finalel valor de IVA

precio = float(input('Ingresa el precio del producto: '))

iva = precio * 0.16
total_con_iva = precio + iva

print('El precio del IVA es: ', str(iva))
print('El precio del producto con IVA incluido es: ', str(total_con_iva))


