# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

# n = input('Введите вещественное число --> ').split('.')
# result = 0
# for j in range(len(n)):
#     for i in range(len(n[j])):
#         result += int(n[j][i])
# print('Сумма чисел --> ', result)

n = input('Введите вещественное число --> ')
print(f"Сумма чисел --> {sum(map(int, n.replace('.', '')))}")