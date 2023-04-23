# monthly expense

expense = [2200, 2350, 2600, 2130, 2190]
valid = True


print(expense[1] - expense[0])
print(expense[1] + expense[0] + expense[2])
if 2000 in expense: print("possui")
expense.append(1980)
print(expense)
expense[3] = expense[3] - 200
print(expense)

print()

# favorite hero movie

heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
print(len(heroes))
heroes.append('black panther')
print(heroes)
hero = heroes.pop()
heroes.insert(3, hero)
print(heroes)
heroes.remove('thor') and heroes.remove('hulk') and heroes.insert(2, 'doctor strange')
print(heroes)
heroes_sorted = sorted(heroes)
print(heroes_sorted)

print()

# odd numbers

max_num = int(input())
odd = []

for i in range(1, max_num):
    if i % 2 ==1: odd.append(i)

print(odd)
