import random

should_continue = True

while should_continue: # Выполняется пока should_continue = true
	player = input('Камень, ножницы, бумага? [R, S, P]: ').lower() # Приведем к нижнему регистру для минимизации ошибок при вводе.
	computer = random.choice(['r', 's', 'p'])

	if player not in ['r', 's', 'p']:
		print('Ошибка ввода! Попробуйте снова.')
		continue # Сделали проверку на ввод.

	win_comb = [('r', 's'), ('s', 'p'), ('p', 'r')] # Комбинации для выйгрыша.
	
	if player == computer:
		print('Ничья! Еще раз!')
		continue
	elif (player, computer) in win_comb:
		print(f'Выбор игрока - {player}\nВыбор компьютера - {computer}')
		print('Победа!')
	else:
		print(f'Выбор игрока - {player}\nВыбор компьютера - {computer}')
		print('Не получилось..')

	should_continue = input('Хотите попробовать снова? (y/n): ') == 'y'
	print('\n')