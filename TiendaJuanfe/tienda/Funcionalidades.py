




salario = float(input("INgrese el salario del empleado a calcular"))

salario_minimo = 1300000

aux_transporte = 162000

def calcular_salud(salario):
    descuento_salud = salario * (4/100)
    return descuento_salud

def calcular_pension(salario):
    descuento_pension = salario * 0.04
    return descuento_pension

def calcular_salario_neto(salario, salario_minimo , aux_transporte):
    salud = calcular_salud(salario)
    pension = calcular_pension(salario)
    if salario < (salario_minimo*2):
        salario_neto = salario - salud -pension + aux_transporte
        print(f"El salario a pagar es {salario_neto}")
    else:
        salario_neto = salario - salud - pension
        print(f"El salario a pagar es {salario_neto}")


calcular_salario_neto(salario, salario_minimo, aux_transporte)