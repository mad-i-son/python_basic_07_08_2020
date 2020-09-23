"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр
и вывести на экран. Например, если введено число 3486, надо вывести 6843.
"""
import timeit
import cProfile

# user_var = '3486789'
# symbols = list(user_var)
# for el in range(len(user_var) // 2):
#     tmp = symbols[el]
#     symbols[el] = symbols[len(user_var) - el - 1]
#     symbols[len(user_var) - el - 1] = tmp
# str_reverse = ''.join(symbols)
# print(timeit.timeit(str_reverse))

# user_var = '3486' 0.021174683
# user_var = '3486789' 0.029046696000000004
# user_var = '3486789999' 0.020913837999999997
# 0.021417414999999995
# 100 loops, best of 5: 22.6 nsec per loop



# num = int(3486789999)
# newnum = ""
# while num:
#     newnum += str((num % 10))
#     num = num // 100
# print(timeit.timeit(newnum))
# user_var = '3486' 0.030763928999999995
# user_var = '3486789' 0.05085719000000001
# user_var = '3486789999' 0.026371217000000002
# 0.02094100900000001
# 100 loops, best of 5: 27.2 nsec per loop


# n = int(3486789999)
#
# while n>0:
#     print(n%10, end="")
#     n=n//10

# 100 loops, best of 5: 22.6 nsec per loop

def main():
    n = int(3486789999)
    while n>0:
        print(n%10, end="")
        n=n//10

cProfile.run('main()')

# 14 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:46(main)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}