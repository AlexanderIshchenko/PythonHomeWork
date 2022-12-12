# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

def n(a=None):
    min_element = a[0] % 1
    max_element = a[0] % 1
    for i in range(len(a)):
        if a[i] % 1 < min_element:
            min_element = a[i] % 1
        if a[i] % 1 > max_element:
            max_element = a[i] % 1
    result = max_element-min_element
    return round(result, 2)


list_a = [1.1, 1.2, 3.1, 10.01]
print(n(list_a))
