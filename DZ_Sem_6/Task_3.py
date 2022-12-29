#  Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка,
# стоящих на нечётной индексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

# def sum(a=None):
#     result = 0
#     for i in range(1, len(a), 2):
#         result += a[i]
#     return result


# list_a = [2, 3, 5, 9, 3]
# print(sum(list_a))

list_a = [2, 3, 5, 9, 3]
print(sum(list_a[i] for i in range(1, len(list_a), 2)))