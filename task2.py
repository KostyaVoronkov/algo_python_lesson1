import cProfile

def eratosfen(n):
    sieve = [i for i in range(n*100)]
    sieve[1] = 0
    for i in range(2, n*100):
        if sieve[i] != 0:
            j = i + i
            while j < n*100:
                sieve[j] = 0
                j += i
        result = [i for i in sieve if i != 0]
        if (len(result)) == n-1:
            break
    return result[n-1]

# timeit n =5: 100 loops, best of 5: 18.4 msec per loop
# timeit n =10: 100 loops, best of 5: 70.6 msec per loop
# timeit n =50: 100 loops, best of 5: 1.68 sec per loop

cProfile.run('eratosfen(5)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.019    0.019 <string>:1(<module>)
   #    498    0.018    0.000    0.018    0.000 task2.py:12(<listcomp>)
   #      1    0.001    0.001    0.019    0.019 task2.py:3(eratosfen)
   #      1    0.000    0.000    0.000    0.000 task2.py:4(<listcomp>)
   #      1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
   #    498    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('eratosfen(10)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.071    0.071 <string>:1(<module>)
   #    998    0.069    0.000    0.069    0.000 task2.py:12(<listcomp>)
   #      1    0.002    0.002    0.071    0.071 task2.py:3(eratosfen)
   #      1    0.000    0.000    0.000    0.000 task2.py:4(<listcomp>)
   #      1    0.000    0.000    0.072    0.072 {built-in method builtins.exec}
   #    998    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('eratosfen(50)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    1.735    1.735 <string>:1(<module>)
   #   4998    1.712    0.000    1.712    0.000 task2.py:12(<listcomp>)
   #      1    0.021    0.021    1.735    1.735 task2.py:3(eratosfen)
   #      1    0.000    0.000    0.000    0.000 task2.py:4(<listcomp>)
   #      1    0.000    0.000    1.735    1.735 {built-in method builtins.exec}
   #   4998    0.001    0.000    0.001    0.000 {built-in method builtins.len}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



def simple_number(n):
   i = 0
   temp = 1
   number_is_not_simple = False
   number = 0
   result=[]
   while i != n:
       temp += 1
       for item in range(2, n):
           if temp < item:
               break
           if temp % item == 0 and temp != item:
               number_is_not_simple = True
               break
       if number_is_not_simple == False:
           i += 1
           number = temp
           result.append(number)
       number_is_not_simple = False
   return number

# timeit n =5: 100 loops, best of 5: 12.3 usec per loop
# timeit n =10: 100 loops, best of 5: 38.6 usec per loop
# timeit n =50: 100 loops, best of 5: 581 usec per loop

cProfile.run('simple_number(5)')

   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 task2.py:53(simple_number)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      5    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('simple_number(10)')

   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 task2.py:53(simple_number)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #     10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('simple_number(50)')

   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
   #      1    0.001    0.001    0.001    0.001 task2.py:53(simple_number)
   #      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
   #     50    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#Вывод: Решето Эратосфена в данной редакции имеет явно не линейное время решения задачи в зависимости от количества
#элементов.
#В тоже время поиск в цикле реализуется намного быстрее и имеет линейную зависимость времени от количества искомых элементов.
