import random

valid = True
lista = []
for i in range(100):
    lista.append(round(random.randint(0, 100)))

lista.sort()
i = 0

while valid:
    mid = len(lista) // 2
    lista_esq = lista[0: mid]
    lista_dir = lista[mid: -1]
    if 44 in lista_esq:
        lista = lista_esq
    if 44 in lista_dir:
        lista = lista_dir
    if lista[0] == 44:
        valid = False
    i += 1
print(lista)
print(i)
