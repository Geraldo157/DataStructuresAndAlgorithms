import random

valid = True
lista = []

for i in range(100):
    ran = round(random.randint(0, 1000))
    if ran not in lista:
        lista.append(ran)

while valid:
    num = int(input('Type a number to be found'))
    if num in lista:
        lista.sort()
        while valid:
            mid = len(lista) // 2
            if num < lista[mid]:
                lista = lista[0:mid]
                print(lista)
            elif num > lista[mid]:
                lista = lista[mid:-1]
                print(lista)
            elif num == lista[mid]:
                lista = lista[mid]
                valid = False
    else:
        print('This number not in the list, try again')

print(lista)
