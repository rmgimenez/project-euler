'''
Highly divisible triangular number
Problem 12
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
import funcoes

'''
Método de força bruta que não deu certo, demora muito
achou = False
posicao = 1
while achou == False:
	numero = funcoes.gera_numero_triagular(posicao)
	if len(funcoes.divisores_numero(numero)) > 500:
		print(numero)
		achou = True
	posicao = posicao + 1

segui a ajuda desse site:
http://code.mikeyaworski.com/python/project_euler/problem_12
'''
posicao = 1
numeros_divisores = 0

while numeros_divisores <= 500:
	numeros_divisores = 0
	numero = funcoes.gera_numero_triagular(posicao)
	i = 1
	while i <= numero**0.5:
		if numero % i == 0:
			numeros_divisores += 1
		i += 1
	numeros_divisores *= 2
	posicao = posicao + 1

print(numero)