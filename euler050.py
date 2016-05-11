'''
Consecutive prime sum
Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

Ver algum forma de começar a verificar pelos últimos números primos da lista.
Na lista os últimos primos são: ...999931, 999953, 999959, 999961, 999979, 999983, por exemplo, se eu somar o 999931 com o 999953
já vai dar um número maior que 1000000

Resposta = 997651
[Finished in 692.9s]
'''
import funcoes

from time import time
start = time()

# lista que armazena todos os números primos até o limite desejado que no caso do problema é < 1000000
lista_primos = []

# número máximo pra verificar, no caso do problema é 1000000
limite = 1000000

# preenche a lista lista_primos com os números primos até o valor da variável limite
for x in range(1, limite):
	if funcoes.is_prime(x):
		lista_primos.append(x)

def maior_numero_soma_seq(lista):
	i = 0
	lista.reverse()
	maior_numero_lista = max(lista)
	maior_sequencia = 0
	maior_numero = 0
	soma = []
	tamanho_lista = len(lista)
	while i < len(lista):
		j = i + 1
		soma.clear()
		soma.append(lista[i])
		while j < len(lista):
			if lista[j] < lista[i]:
				soma.append(lista[j])
				# fiz isso para que se o sum da lista soma for maior que o maior numero da lista
				# ele já passa e muda o indice i do while, ou seja passa para o próximo número
				# de início
				if sum(soma) > maior_numero_lista:
					j = len(lista) + 1
				else:
					if sum(soma) in lista:
						if len(soma) > maior_sequencia:
							maior_sequencia = len(soma)
							maior_numero = sum(soma)
							#print("Maior sequencia = ",maior_sequencia)							
							#print(soma, "=" , maior_numero)
							#print("Indice i =", i,"de", tamanho_lista, "- % analisados =", (i/tamanho_lista)*100,"%")
							#print("------------------------------------")
			j += 1
		i += 1
	return maior_numero

print("Resposta =", maior_numero_soma_seq(lista_primos))
print("Time: {0} secs".format(time()-start))

# resolvido