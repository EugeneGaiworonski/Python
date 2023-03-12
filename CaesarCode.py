# ********************************************************************************
# Source : CaesarCode.py / Python 3.9
# Created : 12.03.2023 
# Modified : - 
# Author : Евгений Гайворонский
# Description: На вход программе подается строка текста на английском языке, 
# в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать 
# с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные 
# буквы при этом остаются строчными, а прописные – прописными. 
# ********************************************************************************

from os import system

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
	else:
		pass

def screen80():
	system('mode con cols=80 lines=25')
	print()

def code(data_string):
	coded = ''
	shift = 0
	for char in data_string:
		if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			shift += 1
	for char in data_string:
		if char in 'abcdefghijklmnopqrstuvwxyz':
			shift += 1
    # shift = len(data_string)
	for char in data_string:
		if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			if ord(chr(ord(char) + shift)) <= ord('Z'):
				coded += chr(ord(char) + shift) 
			else:
				coded += chr(ord(char) + shift - 26)
		elif char in 'abcdefghijklmnopqrstuvwxyz':
			if ord(chr(ord(char) + shift)) <= ord('z'):
				coded += chr(ord(char) + shift) 
			else:
				coded += chr(ord(char) + shift - 26)
		else:
			coded += char
	return coded


def textcode(string):
	text_coded = '' 
	text_list = string.split()
	for idx in range(len(text_list)):
		text_coded += code(text_list[idx])
		text_coded += ' '
	text_coded = text_coded.lstrip()
	return text_coded

# DATA 
# ********************************************************************************


# START 
# ********************************************************************************
screen80()
while True:
	line = input()
	print(textcode(line))
	if ask('Закончить работу? Да(1)/Нет(2)', '1', '2'):
		break
	
# END 
# ********************************************************************************
