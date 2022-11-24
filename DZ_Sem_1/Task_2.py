# 2. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋀ - and ⋁ - or ¬ - not

# not(x or y or z) = not x and not y and not z
# -(x+y+z) = (-x)*(-y)*(-z)

for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            print(x, y, z, end=' - ')
            print(not (x or y or z) == (not x and not y and not z))