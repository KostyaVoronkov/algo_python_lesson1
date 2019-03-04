#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
#Сами минимальный и максимальный элементы в сумму не включать.
import random
MINNUMBER=0
MAXNUMBER=100
MAXSIZE=10

mass = [random.randint(MINNUMBER, MAXNUMBER) for _ in range(MAXSIZE)]
print(mass)
min = MAXNUMBER
max = max_ind = min_ind = 0
sum_=0
for i, item in enumerate(mass):
    if item < min:
        min = item
        min_ind = i
    if item > max:
        max = item
        max_ind = i
print(f'Мимимальный: {min} индекс: {min_ind} Максимальный:{max} Индекс: {max_ind}')

if max_ind > min_ind:
    for item in mass[min_ind + 1 : max_ind - 1]:
        sum_ += item
else:
    for item in mass[max_ind + 1 : min_ind - 1]:
        sum_ += item
print("Сумма: " + str(sum_))

