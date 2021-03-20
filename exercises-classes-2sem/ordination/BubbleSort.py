# em Python existe o conceito de variável auxiliar

lista = [25, 21, 22, 24, 23, 27, 26]

indexUltimoElemento = len(lista) - 1

print(lista)


def bubbleSort(lista):
    for bloqueio in range(indexUltimoElemento, 0, -1):
        for indice in range(bloqueio):
            if lista[indice] > lista[indice + 1]:
                aux = lista[indice]
                lista[indice] = lista[indice + 1]
                lista[indice + 1] = aux


print(lista)