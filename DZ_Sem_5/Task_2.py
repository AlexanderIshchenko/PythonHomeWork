# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import sys
print('\nУсловие задачи:\n \nНа столе лежит 2021 конфета.'
      '\nИграют два игрока делая ход друг после друга.'
      '\nПервый ход определяется жеребьёвкой.'
      '\nЗа один ход можно забрать не более чем 28 конфет.'
      '\nВсе конфеты оппонента достаются сделавшему последний ход\n')
candy = 2021
while candy > 0:
    if candy > 28:
        player_1 = input(
            'Игрок 1: Сколько конфет возьмете? (от 1 до 28) --> ')
        while (not player_1.isdigit()):
            player_1 = input(
                'Необходимо ввести натуральное число (от 1 до 28) --> ')
        while (int(player_1) > 28 or int(player_1) < 1):
            player_1 = input(
                'Необходимо ввести натуральное число (от 1 до 28) --> ')

    else:
        player_1 = input(
            f'Игрок 1: Сколько конфет возьмете? (от 1 до {candy}) --> ')
        while (not player_1.isdigit()):
            player_1 = input(
                f'Необходимо ввести натуральное число (от 1 до {candy}) --> ')
        while (int(player_1) > candy or int(player_1) < 1):
            player_1 = input(
                f'Необходимо ввести натуральное число (от 1 до {candy}) --> ')

    candy -= int(player_1)
    print(candy)

    if candy == 0:
        print('Выиграл Игрок 1')
        sys.exit()

    if candy > 28:
        player_2 = input(
            f'Игрок 2: Сколько конфет возьмете? (от 1 до 28) --> ')
        while (not player_2.isdigit()):
            player_2 = input(
                'Необходимо ввести натуральное число (от 1 до 28) --> ')
        while (int(player_2) > 28 or int(player_2) < 1):
            player_2 = input(
                'Необходимо ввести натуральное число (от 1 до 28) --> ')

    else:
        player_2 = input(
            f'Игрок 2: Сколько конфет возьмете? (от 1 до {candy}) --> ')
        while (not player_2.isdigit()):
            player_2 = input(
                f'Необходимо ввести натуральное число (от 1 до {candy}) --> ')
        while (int(player_2) > candy or int(player_2) < 1):
            player_2 = input(
                f'Необходимо ввести натуральное число (от 1 до {candy}) --> ')

    candy -= int(player_2)
    print(candy)

    if candy == 0:
        print('Выиграл Игрок 2')
        sys.exit()
