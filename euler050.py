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
somas_possiveis = []
resposta = 0
maior_quantidade = 0

for x in range(1,1000000):
	if funcoes.is_prime(x):
		lista_primos.append(x)

for x in lista_primos:
	sequencia = []
	for y in lista_primos:
		if y > x:
			break
		else:
			sequencia.append(y)
	if sum(sequencia) in lista_primos:
		if len(sequencia) > maior_quantidade:
			resposta = sum(sequencia)
			maior_quantidade = len(sequencia)
			somas_possiveis.append(sequencia)

#print(somas_possiveis)
print("Resposta:", resposta)
print("Tamanho:", maior_quantidade)