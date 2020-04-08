#El usuario ingrese el precio del producto
#Se muestre al final el valor del IVA

print("Este programa nos muestra el IVA de un producto")

producto = float(input("Ingresa el valor del producto: "))

iva = producto * 0.16

print("El IVA del producto es: ","{:0.4f}".format(iva),"Pesos")

total = producto + iva

print("El valor del producto con IVA incluido es: ""{:0.4f}".format(total),"pesos")
