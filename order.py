#nums = [2, 6, 9, 2, 1, 0, 9, 6, 7, 3, 4, 5, 2]
#numeros_ordenasdos = sorted(nums,reverse=False)
#print(numeros_ordenasdos)

lista = [3, 9, 4, 7, 7969, 86, 800, 7789, 89786, 7876, 76, 67, 456,23,456,0.9999, 795, 975, 9876, 1324, 23, 65]

def ordenar():
    for li in range(len(lista) - 1):
        for lis in range(li + 1, len(lista)):
            if lista[li] > lista[lis]:
                temp = lista[lis]
                lista[lis] = lista[li]
                lista[li] = temp
    print(lista)

ordenar()
