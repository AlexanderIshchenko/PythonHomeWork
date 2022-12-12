# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fiblist(a):
    fib = [0, 1]
    negfib = []
    for i in range(2, a+1):
        fib.append(fib[i-1]+fib[i-2])
    for i in range(0, a):
        negfib.append(fib[a-i])
        if (a-i) % 2 == 0:
            negfib[i] = negfib[i]*(-1)
    result = negfib + fib
    return result


print(fiblist(7))
