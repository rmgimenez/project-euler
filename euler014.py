'''
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

resposta: 837799
155.8 segundos
'''
def numero_par(numero):
	return numero/2

def numero_impar(numero):
	return (3 * numero) + 1

resposta = 0
maior_sequencia = 0
for x in range(1, 1000000):
	numero_processado = x
	vezes = 1

	while numero_processado != 1:
		if numero_processado % 2 == 0:
			numero_processado = numero_par(numero_processado)
		else:
			numero_processado = numero_impar(numero_processado)
		vezes += 1

		if numero_processado == 1:
			if vezes > maior_sequencia:
				maior_sequencia = vezes
				resposta = x
	#print(x,vezes)
print("Resposta =", resposta)
#print(maior_sequencia)

# resolvido