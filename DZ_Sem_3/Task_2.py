# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def res(a=None):
    result = []
    if len(a) % 2 == 0:
        count = int(len(a)/2)
    else:
        count = int(len(a)/2)+1
    for i in range(count):
        result.append(a[i] * a[len(a)-1-i])
    return result


list_a = [2, 3, 4, 5, 6]
list_b = [2, 3, 5, 6]
print(res(list_a))
