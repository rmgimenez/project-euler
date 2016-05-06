# coding: utf-8

'''
Se o número for primo a função retorna True, se não retorna False
'''
def is_prime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		#print('\t',f)
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True

'''
Verifica se o número é um palindromo
Se for retorna True, se não retorna False
Palindromo é quando o número é escrito da mesma forma não importa se começar de tras pra frente
'''
def is_palindrome(numero):
	str_numero = str(numero)
	if str_numero == str_numero[::-1]:
		return True
	else:
		return False

'''
Calcula o fatorial de um número de forma recursiva
'''
def fatorial( n ):
   if n <1:   # base case
       return 1
   else:
       return n * fatorial( n - 1 )  # recursive call