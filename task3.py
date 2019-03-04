# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random as rand
MINNUMBER=0
MAXNUMBER=100000
MAXSIZE=10
mass = [rand.randint(MINNUMBER,MAXNUMBER) for _ in range(MAXSIZE)]
min = max = 0
min_ind = max_ind = 0

for i, item in enumerate(mass):
    if i == 0:
        min = max = item
        min_ind = max_ind = i
    if item > max:
        max = item
        max_ind = i
    if item < min:
        min = item
        min_ind = i
print(mass)
mass[min_ind] = max
mass[max_ind] = min
print(mass)