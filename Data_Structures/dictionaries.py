hashmap = {}

with open('nyc_weather.csv', 'r') as data:
    for k in data:
        data_format = k.split(',')
        hashmap[data_format[0]] = data_format[1][0:2]

hashmap.pop('date')
media = 0
max_temp = 0
i = 0
for k in hashmap:
    if i < 7:
        media += int(hashmap.get(k)) / 7
    if int(hashmap.get(k)) > max_temp:
        max_temp = int(hashmap.get(k))
    i += 1
print(f'{media:.2f}')
print(f'{max_temp:.2f}')
print()
# Q2

print(hashmap.get('Jan 4'))
print(hashmap.get('Jan 9'))

# Q3
print()
poem_map = {}

i = 0

with open('poem.txt', 'r') as poem:
    lista = poem.read().split()
    for k in lista:
        poem_map[k] = lista.index(k)
print(poem_map.get('diverged'))
print(poem_map.get('in'))
print(poem_map.get('I'))

