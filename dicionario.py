score = (["bajo", 0, 25], ["aceptable", 26, 50], ["sobreSaliente", 51, 75], ["exelente", 76, 90])

def cal(nota):
    for i, n in enumerate(score, start=1):
        if (nota >= n[1] and nota <= n[2]):
            print(f"La nota es: {i} - {n[0]}")
            break

def promedios():
    mensaje = "Notas \n"
    for i, n in enumerate(score, start=1):
        mensaje += promedioNota(posicion= i, nombre= n[0], rango=[n[1], n[2]])
        #mensaje += f"{i}. {n[1]} a {n[2]} -> {n[0]} \n"
    return mensaje

def promedioNota(posicion: int, nombre: str, minMax: list):
    return f"{posicion}. {minMax[0]} a {minMax[1]} -> {nombre} \n"


nota = input("Ingrese la Nota: ")
print(promedios())
cal(int(nota))

