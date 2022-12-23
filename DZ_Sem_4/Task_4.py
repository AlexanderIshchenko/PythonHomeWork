# 3. Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0
# или 8*(x**4) + 5*x + 4 = 0 и т.д.

from pathlib import Path


def equation(k):
    import random
    lst_k = []
    for i in range(k+1):
        lst_k.append(random.randint(0, 100))
    result = []
    for i in range(k-1):
        if lst_k[i] != 0:
            result.append(f'{lst_k[i]}x^{k-i}')
    result.append(f'{lst_k[k-1]}x + {lst_k[k]} = 0')
    a = ' + '
    result = a.join(result)
    return result


k = 5
print(equation(k))

file_path = Path('equation.txt')

with open(file_path, 'w') as data:
    data.write(equation(k))
