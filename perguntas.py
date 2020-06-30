from random import *
from dicionario import * 

def pergunta():

	tipo_pergunta = randint(1, 6)
	estado, (capital, sigla) = choice(list(dicionario_estados_capitais.items()))

	if tipo_pergunta == 1:
		print(f"Qual estado brasileiro possui a sigla {sigla}?")
		palpite = input('> ').lower()
		if palpite == estado.lower():
			return True
		else:
			return False
	elif tipo_pergunta == 2:
		print(f"Qual estado brasileiro possui a capital {capital}?")
		palpite = input('> ').lower()
		if palpite == estado.lower():
			return True
		else:
			return False
	elif tipo_pergunta == 3:
		print(f"Qual a capital do estado brasileiro {estado}?")
		palpite = input('> ').lower()
		if palpite == capital.lower():
			return True
		else:
			return False
	elif tipo_pergunta == 4:
		print(f"Qual a capital do estado brasileiro cujo a sigla é {sigla}?")
		palpite = input('> ').lower()
		if palpite == capital.lower():
			return True
		else:
			return False
	elif tipo_pergunta == 5:
		print(f"Qual a sigla do estado brasileiro {estado}?")
		palpite = input('> ').lower()
		if palpite == sigla.lower():
			return True
		else:
			return False
	elif tipo_pergunta == 6:
		print(f"Qual a sigla do estado brasileiro cujo a capital é {capital}?")
		palpite = input('> ').lower()
		if palpite == sigla.lower():
			return True
		else:
			return False