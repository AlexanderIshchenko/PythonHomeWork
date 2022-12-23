# 1. Вычислить число c заданной точностью d
# Пример: - при d = 0.001, π = 3.141
#     Ввод: 0.01
#     Вывод: 3.14

#     Ввод: 0.001
#     Вывод: 3.141

d = 0.00001
def pi_round(d):
    import math
    count = 0
    while d != 1:
        d *= 10
        count += 1
    return round(math.pi,count)
print(pi_round(d))