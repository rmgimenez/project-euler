'''
Funções de ajuda para resolver os problemas
'''

# retorna true se o número for primo
def eh_primo(numero):
	if numero % 2 == 0:
		return FALSE
	else:
		limite = round(numero / 3)
		i = 3
		outro_divisor = false
		while i <= limite:
			if numero % i == 0:
				outro_divisor = true
			i += 2
		if(outro_divisor):
			return false
		else:
			return true

print(eh_primo(8))
