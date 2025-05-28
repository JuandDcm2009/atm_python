dinero = [10, 10, 0, 0]
def printDinero():
    print(f"""
    Dinero Disponible:
    50k: {dinero[0]}
    20k: {dinero[1]}
    10k: {dinero[2]}
    5k: {dinero[3]}
    """)
def validarMonto(denominacion):
    cantidad = 1
    while True:
        cantidad = int(input("Ingrese la cantidad a retirar: "))
        if cantidad  % denominacion != 0:
            input(f"Ingrese un numero valido \n Este cajero solo admite multiplos de {denominacion} COP \n Enter para continuar...")
        else:
            return cantidad

def validarDenominacion(denominacion):
    can = len(denominacion)
    temp = 0

    for i in range(can):

        if denominacion[i] > 0:
            if i  == 0:
                temp = 50_000
            elif i == 1:
                temp = 20_000
            elif i == 2:
                temp = 10_000
            else:
                temp = 5_000
    return temp

denominacion = validarDenominacion(denominacion= dinero)
print(f"La minbima demonimacion es de: {denominacion}")
printDinero()
cantidad = validarMonto(denominacion=denominacion)

total = cantidad
can_50 = 0
can_20 = 0
can_10 = 0
can_5 = 0


while total > 0:

    if total >= 50_000:
        can_50 += 1
        total -= 50_000
        dinero[0] -= 1
    elif total >= 20_000:
        can_20 += 1
        total -= 20_000
        dinero[1] -= 1
    elif total >= 10_000:
        can_10 += 1
        total -= 10_000
        dinero[2] -= 1
    elif total >= 5_000:
        can_5 += 1
        total -= 5_000
        dinero[3] -= 1
    else:
        print("No tenemos fondos suficientes")
        break

result = f"""
Total: {cantidad}
Billetes de 50k: {can_50}
Billetes de 20k: {can_20}
Billetes de 10k: {can_10}
Billetes de 5k: {can_5}

"""

print(result)
printDinero()
