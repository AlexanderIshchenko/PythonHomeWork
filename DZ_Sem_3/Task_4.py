# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def decToBin(num):
    arr = []
    while num != 0:
        arr.append(num % 2)
        num = int(num/2)
    for i in range(int(len(arr)/2)):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    for i in range(len(arr)):
        print(arr[i], end='')


decToBin(45)
