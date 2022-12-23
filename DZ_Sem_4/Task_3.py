# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]


def uniq_elements(lst):
    result_lst = []
    for i in range(len(lst)):
        if lst.count(lst[i]) == 1:
            result_lst.append(lst[i])
    return result_lst


lst = [1, 1, 2, 3, 4, 4, 4]
print(uniq_elements(lst))