'''
Consecutive prime sum
Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
import funcoes

lista_primos = []
resposta = 0
maior_quantidade = 0

for x in range(1,100):
	if funcoes.is_prime(x):
		lista_primos.append(x)

for x in lista_primos:
	lista_menor = []
	for y in lista_primos:
		if y >= x:
			break
		lista_menor.append(y)
	#print(x, lista_menor)
	soma = []
	for z in lista_menor:
		soma.append(z)
		for t in lista_menor:
			if t > z:
				soma.append(t)
				if sum(soma) == x:
					if len(soma) > maior_quantidade:
						maior_quantidade = len(soma)
						resposta = x

print(resposta, maior_quantidade, soma_resposta)
