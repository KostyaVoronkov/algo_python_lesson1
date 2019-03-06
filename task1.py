#Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.

import cProfile

# Возьмем 2е задание 2й лекции:
##Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные
## # цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def EvenOrOdd(number, iteraion=0, even=0, odd=0):
    iteraion += 1
    if (number % (10 ** iteraion))//10**(iteraion-1) == 0:
        return odd, even

    if ((number%10**iteraion)//10**(iteraion-1)) % 2 == 0:
        odd += 1
    else:
        even += 1
    return EvenOrOdd(number, iteraion,even,odd)

NUMBER_1 = 5873235434 # 10 чисел
NUMBER_2 = 7345784632578756324785619756347289569156873941569873245632486583274583475698732456823475982374384256
#100 чисел

# Выполняем (venv) F:\geekbrains\алгоритмы и структуры\1\4>python -m timeit -n 100 -s "import task1" "task1.EvenOrOdd(5873235434)
# 100 loops, best of 5: 35.4 usec per loop

# Выполняем F:\geekbrains\алгоритмы и структуры\1\4>python -m timeit -n 100 -s "import task1" "task1.EvenOrOdd(7345784632578756324785619756347289569156873941569873245632486583274583475698732
# 456823475982374384256)
# 100 loops, best of 5: 784 usec per loop

cProfile.run('EvenOrOdd(5873235434)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     11/1    0.000    0.000    0.000    0.000 task1.py:9(EvenOrOdd)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('EvenOrOdd(7345784632578756324785619756347289569156873941569873245632486583274583475698732456823475982374384256)')

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#    101/1    0.001    0.000    0.001    0.001 task1.py:9(EvenOrOdd)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Найдем тотже результат только при помощи массивов

def EvenOrOddMass(number):
    even = odd = 0
    i = 0
    str_number = str(number)
    while i < len(str_number):
        if int(str_number[i]) % 2 == 0:
            even += 1
        else:
            odd += 1
        i += 1
    return even, odd

# выполняем python -m timeit -n 100 -s "import task1" "task1.EvenOrOddMass(5873235434)"
# 100 loops, best of 5: 9.42 usec per loop

#выполняем python -m timeit -n 100 -s "import task1" "task1.EvenOrOddMass(734578463257875632478561975634728956915687394156987324563248658327458347569
#8732456823475982374384256)"
#100 loops, best of 5: 88.8 usec per loop

cProfile.run('EvenOrOddMass(5873235434)')

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task1.py:50(EvenOrOddMass)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('EvenOrOddMass(7345784632578756324785619756347289569156873941569873245632486583274583475698732456823475982374384256)')

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task1.py:50(EvenOrOddMass)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вывод:

#Время работы рекурсионной реализации функции при 10 и 100 элементах меняется в 20 раз, а количество элементов в 10 раз.
#Что говорит о не линейной зависимости от входных параметров функции.
#Время работы цикличной реализации функции линейно зависит от входных параметров функции.

# Разница между рекурсионной и цикличной реализацией слставляет почти в 4 раза в пользу цикличной.