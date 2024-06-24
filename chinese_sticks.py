import random

player1, player2 = input('Имя первого игрока: '), input('Имя второго игрока: ')
how_much_sticks = int(input('Сколько палок?: '))

first_step = random.choice([player1, player2])


def player_step(first_step):
    global how_much_sticks

    print(f'Игрок - {first_step}')

    try:
        x = int(input('Сколько палок взять? (1-3): '))
    except ValueError as e:
        print('(1 - 3) !!!')
        player_step(first_step)
    else:
        how_much_sticks -= x


def play():
    global first_step

    print(f'Осталось {how_much_sticks} палок')
    if first_step == player1:
        first_step = player2
    else:
        first_step = player1


while how_much_sticks > 0:
    play()
    player_step(first_step)
else:
    print(f'Игра окончена! Проиграл {first_step}')