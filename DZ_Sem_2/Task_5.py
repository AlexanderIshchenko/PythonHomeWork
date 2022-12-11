# Реализуйте алгоритм перемешивания списка.

# import random # 1-й вариант
# list = [0, 1, 2, 3, 4, 6, 7, 8, 9]
# print(list)
# random.shuffle(list)
# print(list)

import random  # 2-ой вариант
list = [0, 1, 2, 3, 4, 6, 7, 8, 9]
print(list)
for i in range(len(list)):
    j = random.randint(i, len(list)-1)
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
print(list)
