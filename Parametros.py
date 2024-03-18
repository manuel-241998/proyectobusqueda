#Parametros y retorno
def calcular_iva(subtotal, porcentaje_iva=10):
    valor_iva = (subtotal * porcentaje_iva) / 100
    return valor_iva

subtotal = 100
valor_iva = calcular_iva(subtotal)
print(f'El valor del IVA es: {valor_iva}')

subtotal_mc = 100
valor_iva = calcular_iva(subtotal_mc, porcentaje_iva=20)
print(f'El valor del IVA es: {valor_iva}')