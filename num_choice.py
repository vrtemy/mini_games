import random

number = random.randint(1,50)
total = 0

print('Загадано число от 1 до 50. Угадывайте.\nПопыток: 6')

while total < 6:
	x = int(input('Введите число: '))
	if x == number:
		print('Верно!')
		break
	elif x > number:
		print('Меньше!')
		total += 1
		continue
	elif x < number:
		print('Больше!')
		total += 1
		continue
	else:
		print('Не число!')