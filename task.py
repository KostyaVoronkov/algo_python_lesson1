# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# # Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Определить, какое число в массиве встречается чаще всего.
import random
import sys

def used_memory_dimension(*args):
    total_used_memory = 0
    for item in args:
        total_used_memory += sys.getsizeof(item)
        if hasattr(item, '__iter__'):
            for item2 in item:
                total_used_memory += sys.getsizeof(item2)
    return total_used_memory

MINNUMBER=0
MAXNUMBER=120000000
#120000000
MAXSIZE=100
mass = [random.randint(MINNUMBER, MAXNUMBER) for _ in range(MAXSIZE)]
print(mass)
number = max = 0
mass_tocken = [0 for _ in range(MAXNUMBER + 1)]

for i, item in enumerate(mass):
    mass_tocken[item] += 1
for i, item in enumerate(mass_tocken):
    if item > max:
        max = item
        number = i
used_memory = used_memory_dimension(MINNUMBER, MAXNUMBER, MAXSIZE, mass, number, max, mass_tocken, i, item)
print("Чаще всего встречается: " + str(number) + " Количество вхождений: " + str(max))
print(f'Суммарной потребленный объем памяти: {used_memory} байт или {used_memory/1024} кБайт или {used_memory/(1024*1024)} мБайт')

# Итог работы:
# когда MAXNUMBER = 120 Результат:
# Суммарной потребленный объем памяти: 4086 байт или 3.990234375 кБайт или 0.0038967132568359375 мБайт

#Зато когда MAXNUMBER = 120000000 массив mass_tocken образует столько же элементов. Резульат:

#Суммарной потребленный объем памяти: 1923597416 байт или 1878513.1015625 кБайт или 1834.485450744629 мБайт

#Теперь сформируем массив не 0, а None
number = max = 0
mass_tocken = [None for _ in range(MAXNUMBER + 1)]

for i, item in enumerate(mass):
    if mass_tocken[item] == None:
        mass_tocken[item] = 0
    mass_tocken[item] += 1
for i, item in enumerate(mass_tocken):
    if item != None and item > max:
        max = item
        number = i
used_memory = used_memory_dimension(MINNUMBER, MAXNUMBER, MAXSIZE, mass, number, max, mass_tocken, i, item)
print("Чаще всего встречается: " + str(number) + " Количество вхождений: " + str(max))
print(f'Суммарной потребленный объем памяти: {used_memory} байт или {used_memory/1024} кБайт или {used_memory/(1024*1024)} мБайт')

#При 120 элементах результат:
#Суммарной потребленный объем памяти: 3878 байт или 3.787109375 кБайт или 0.0036983489990234375 мБайт

#При 120000000 элементах результат:
#Суммарной потребленный объем памяти: 1443597808 байт или 1409763.484375 кБайт или 1376.722152709961 мБайт

# ******* Разница между 1377 мБайт и 1834 мБайт впечатляет *********