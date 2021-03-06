# coding: utf-8
import math

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
Retorna uma lista de números primos
'''
def lista_num_primos(quantidade):
	lista = []
	if quantidade == 1:
		lista.append(2)
	else:
		total = 1
		lista.append(2)
		numero = 3
		while total != quantidade:
			if(is_prime(numero)):
				lista.append(numero)
				total = total + 1
			numero = numero + 2
	return lista

'''
retorna lista de divisores de um número
'''
def divisores_numero(numero):
	lista = []
	if is_prime(numero):
		lista.append(1)
		lista.append(numero)
	else:
		#for x in range(1, round(numero/2) + 1):
		for x in range(1, round(numero/2) + 1):
			if numero % x == 0:
				lista.append(x)
		lista.append(numero)
	return lista

'''
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
com recursão
'''
def gera_numero_triagular_rec(posicao):
	if posicao == 1:
		return 1
	else:
		return posicao + gera_numero_triagular(posicao - 1)

'''
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
sem recursão
'''
def gera_numero_triagular(posicao):
	total = 0
	for x in range(1,posicao + 1):
		total += x
	return total

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

'''
Fibonacci com recursão
'''
def fib_rec(n):
	if n==1 or n==2:
		return 1
	return fib_rec(n-1) + fib_rec(n-2)

'''
Tri fibonacci com recursão
'''
def tri_fib(n):
	if n == 1 or n == 2:
		return 1
	elif n <= 0:
		return 0
	else:
		return tri_fib(n-1) + tri_fib(n-2) + tri_fib(n-3)

'''
Exponenciação modular
Ela deve ser usada quando for fazer a exnoenciação em número gigante e eu quiser apenas a parte final dele
Ajuda: http://aditya.vaidya.info/blog/2014/06/27/modular-exponentiation-python/
'''
def expmod(a,b,c):
    return (a**b)%c

'''
Calcula pentagono de um número
'''
def pentagono(n):
	return n*(3*n-1)/2

def triangulo(n):
	return n*(n+1)/2

def hexagono(n):
	return float(n*(2*n-1))

'''
Verifica se um número é pentagonal
'''
def is_pentagono(N): return ((math.sqrt(24 * N + 1) + 1) / 6.0).is_integer()

'''
Verifica se um número é hexagonal
'''
def is_hexagonal(x):
	return ((math.sqrt((8*x) + 1) + 1)/4).is_integer()

'''
Verifica se um número é triangular
'''
def is_triangular(x):
	return ((math.sqrt((8*x) + 1) - 1)/2).is_integer()

'''
Retorna true se o ano é bissexto e false se não for
'''
def is_leap_year(ano):
	if (ano % 2 != 0):
		return False
	else:
		if (ano % 100 == 0):
			if (ano % 400 == 0):
				return True
			else:
				return False
		else:
			if (ano % 4 == 0):
				return True
			else:
				return False

