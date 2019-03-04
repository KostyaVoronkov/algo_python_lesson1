#Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со
# значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
# начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random as rand
MINNUMBER=1
MAXNUMBER=100
MAXSIZE=10

mass = [rand.randint(MINNUMBER, MAXNUMBER) for _ in range(MAXSIZE)]
new_mass = []
for i, item in enumerate(mass):
    if item % 2 == 0:
        new_mass.append(i)
print(new_mass)
