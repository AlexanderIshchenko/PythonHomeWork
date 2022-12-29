# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите число n --> '))  # 2-ой вариант решения
# result = 1
# for x in range(1, n+1):
#     result *= x
#     print(result, end=' ')

import math
n = int(input('Введите число n --> '))
print(list(map(lambda x: ((x == 1) and 1) or x * math.factorial(x -1),list(range(1,n+1)))))
