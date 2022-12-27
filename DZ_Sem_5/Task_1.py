# 1. Напишите программу, удаляющую из текста все слова,
# содержащие ""абв"".

from pathlib import Path

file_path = Path('DZ_sem_5_ex_1.txt')
file_path_2 = Path('DZ_sem_5_ex_1_result.txt')

with open(file_path, 'w') as data:
    data.write('Я люблю Джавуабв абви Питон')
with open(file_path, 'r') as data:
    a = data.read()
filtered_list = list(filter(lambda x: "абв" not in x, a.split(" ")))
with open(file_path_2, 'w') as data:
    data.write(' '.join(filtered_list))
