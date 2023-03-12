# ********************************************************************************
# Source : GuessTheNumber.py / Python 3.9
# Created : 09.03.2023 
# Modified : - 
# Author : Евгений Гайворонский
# Description: программа генерирует случайное число в диапазоне от 1 до 100 
# и просит пользователя угадать это число. 
# Если догадка пользователя больше случайного числа, то программа должна вывести 
# сообщение <<Слишком много, попробуйте еще раз>>.
# Если догадка меньше случайного числа, то программа должна вывести сообщение 
# <<Слишком мало, попробуйте еще раз>>.
# Если пользователь угадывает число, то программа должна поздравить его и вывести 
# сообщение <<Вы угадали, поздравляем!>>.
# ********************************************************************************

from os import system
from random import randint, seed

# FUNCTIONS 
# ********************************************************************************

def printс(message): # вывод сообщения по центру окна
	if len(message) < 80:
		print((' ' * ((79 - len(message)) // 2)) + message)

def ask(message, yes, no): 
	ch = ''
	while  ((ch != yes) and (ch != no)):
		ch = input((' ' * ((79 - len(message)) // 2)) + message)
	if ch == no:
		return True
	elif ch == yes:
		return False

# DATA 
# ********************************************************************************

language   = -1
play_again	=	['Сыграть еще? Да(1) или Нет(2) ', 
				'Play again? Yes(1) or No(2) ', 
				'¿Jugar un poco más? Si(1) or No(2) ']
lets_play	=	['Я загадал число между 1 и 100. Попробуй угадать за 7 попыток: ', 
				'I guessed the number between 1 and 100. Try to guess in 7 attempts:', 
				'Adiviné el número entre 1 y 100. Intenta adivinar en 7 intentos:']
too_much	=	['Слишком много, попробуй еще раз' , 
				'Too high, try again', 
				'Demasiado, inténtalo de nuevo']
too_less	=	['Слишком мало, попробуй еще раз' , 
				'Too low, try again', 
				'Muy poco, inténtalo de nuevo']
win			=	['Верно, ты ВЫИГРАЛ!', 
				"That's right, You WIN!", 
				'¡Así es, usted GANA!'] 
loss		=	['Ты ПРОИГРАЛ!', 
				'You LOSE!', 
				'¡Tú PIERDES!']
next_time	=	['Попытка ', 
				'Attempt ', 
				'Intenar ']
see_you		=	['До встречи!',	
				'See You!', 
				'¡Nos vemos!']
input_error =	['Неверный ввод',
				'Invalid input', 
				'Entrada inválida']

# START 
# ********************************************************************************

system('mode con cols=80 lines=25')
print()
printс('--    Игра "УГАДАЙ ЧИСЛО!"    --')
printс('-- "Guess the number" game!"  --')
printс('-- Juego "Adivina el numero!" --')

while  not 0 <= language <= 2:
	print()
	printс('(1) - ru, (2) - eng, (3) - esp')
	language = int(input()) - 1


while True:
	printс(lets_play[language])
	turns = 6 # число попыток
	seed(randint(1, 100))
	guessed_number = randint(1, 100)
	# debug
	# print(guessed_number)
	# end debug
	while True:
		player_number = int(input())
		if player_number == guessed_number:
			printс(win[language])
			break
		elif turns == 0:
			printс(loss[language])
			break
		elif turns > 0 and player_number > guessed_number:
			printс(too_much[language])
			turns -= 1
			printс(next_time[language] + str(6 - turns + 1))
		else:
			printс(too_less[language])
			turns -= 1
			printс(next_time[language] + str(6 - turns + 1))

	if ask(play_again[language], '1', '2'):
		printс(see_you[language])
		break
    
# END 
# ********************************************************************************