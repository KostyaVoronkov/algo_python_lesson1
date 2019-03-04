# Определить, какое число в массиве встречается чаще всего.
import random
MINNUMBER=0
MAXNUMBER=10
MAXSIZE=10
mass = [random.randint(MINNUMBER, MAXNUMBER) for _ in range(MAXSIZE)]
print(mass)
number = max = 0
mass_tocken = [0 for _ in range(MAXSIZE + 1)]

for i, item in enumerate(mass):
    mass_tocken[item] +=1
for i, item in enumerate(mass_tocken):
    if item > max:
        max = item
        number = i

print("Чаще всего встречается: " + str(number))
