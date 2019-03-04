# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

import random
MINNUMBER=-100
MAXNUMBER=100
MAXSIZE=10
mass = [random.randint(MINNUMBER, MAXNUMBER) for _ in range(MAXSIZE)]
print(mass)
ind = -1
max = 1
for i, item in enumerate(mass):
    if item < 0 and max > item:
        ind = i
        max = item

print(f'Значение: {max} индекс: {ind}')