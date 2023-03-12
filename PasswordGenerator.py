# ********************************************************************************
# Source : PasswordGenerator.py / Python 3.9
# Created : 11.03.2023 
# Modified : - 
# Author : Евгений Гайворонский
# Description: программа генерирует заданное количество паролей и включает в себя 
# умную настройку на длину пароля, а также на то, какие символы требуется в него 
# включить, а какие исключить.
# ********************************************************************************

from os import system
from random import randint, seed

# FUNCTIONS 
# ********************************************************************************

def ask(message, yes, no): 
	ch = ''
	while  ((ch != yes) and (ch != no)):
		ch = input(message)
	if ch == no:
		return False
	elif ch == yes:
		return True

def generate_password(length, charset):
	password_length = 0
	password = ''
	char_list = list() 
	for idx in range(len(charset)):
		char_list.append(charset[idx])
	first = min(char_list)
	last = max(char_list)
	while password_length < length:
		char = chr(randint(ord(first),ord(last)))
		if char in charset:
			password += char
			password_length += 1
	return password

# DATA 
# ********************************************************************************
digits				= '0123456789'
lowercase_letters	= 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters	= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation			= '!#$%&*+-=?@^_'
exclusions			= 'iIl1Lo0O'
chars				= ''
buffer_string		= ''

quantity			= 1		# Количество паролей 
length				= 8		# Длина пароля
is_digits			= True	# Включать ли в пароль цифры от 0 до 9
is_uppercase		= True	# Включать ли в пароль прописные буквы
is_lowercase		= True	# Включать ли в пароль строчные буквы
is_punctuation		= False	# Включать ли в пароль символы !#$%&*+-=?@^_
is_noexceptions		= False # Исключать ли неоднозначные символы il1Lo0O

# START 
# ********************************************************************************

system('mode con cols=80 lines=25')
while True:
	buffer_string = input(f'Сколько паролей вам нужно сгенерировать? [{quantity}]')
	if len(buffer_string) > 0:
		quantity = int(buffer_string)
	buffer_string = input(f'Какой длины должен быть пароль? [{length}]')
	if len(buffer_string) > 0:
		length = int(buffer_string)
	if input(f'Включать ли в пароль цифры от 0 до 9? Да(1)/Нет(2) [{is_digits}]') == '1':
		is_digits = True
	else:
		is_digits = False
	if input(f'Включать ли в пароль прописные буквы? Да(1)/Нет(2) [{is_uppercase}]') == '1':
		is_uppercase = True
	else:
		is_uppercase = False
	if input(f'Включать ли в пароль строчные буквы? Да(1)/Нет(2) [{is_lowercase}]') == '1':
		is_lowercase = True
	else: 
		is_lowercase = False
	if input(f'Включать ли в пароль символы !#$%&*+-=?@^_? Да(1)/Нет(2) [{is_punctuation}]') =='1':
		is_punctuation = True
	else: 
		is_punctuation = False
	if input(f'Исключать ли неоднозначные символы iIl1Lo0O? Да(1)/Нет(2) [{is_noexceptions}]') =='1':
		is_noexceptions = True
	else: 
		is_punctuation = False
	if is_digits:
		chars += digits
	if is_uppercase:
		chars += uppercase_letters
	if is_lowercase:
		chars += lowercase_letters
	if is_punctuation:
		chars += punctuation
	if is_noexceptions:
		buffer_string = ''
		for idx in range(len(chars)):
			if chars[idx] not in exclusions:
				buffer_string += chars[idx]
		chars = buffer_string
	for _ in range(quantity):
		print(generate_password(length, chars))
	if (ask('Закончить работу? Да(1)/Нет(2)','1','2')):
		break

# END 
# ********************************************************************************

