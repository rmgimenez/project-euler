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
'''
import funcoes

# lista que armazena todos os números primos até o limite desejado que no caso do problema é < 1000000
lista_primos = []

# número máximo pra verificar, no caso do problema é 1000000
limite = 1000

# variável que irá armazenar o indice do registro da lista de primos que não vou precisar somar, pois se somar eles já vai dar
# mais que o limite
nao_considerar_apos_indice = 0

#usado para achar o nao_considerar_apos_indice 
achou_indice = False

# lista de todas as somas possiveis em sequencia que dá um número primo
somas_possiveis = []

# somas encontradas, o valor dessa lista será inserido na lista somas_possiveis
somas = []

# maior quantidade de numeros na soma
maior_quantidade = 0

# preenche a lista lista_primos com os números primos até o valor da variável limite
for x in range(1, limite):
	if funcoes.is_prime(x):
		lista_primos.append(x)

# retorna a maior quantidade de somas continuas cujo resultado é um número primo em uma determinada lista
# deve se passar como parâmetro um lista de números primos
def quant_somas(lista):
	i = 0
	somas_possiveis = []
	while i < len(lista):
		j = i + 1
		soma = []
		del soma[:] # apaga a lista
		soma.append(lista[i])
		while j < len(lista):
			if (sum(soma) + lista[j]) in lista:
				somas_possiveis.append(lista[j])
				j += 1
			else:
				j = 5000000000000			
		i += 1
	return len(somas_possiveis)

print(quant_somas(lista_primos))


# maior soma até um centésimo do limite
def maior_quantidade_ate_um_cent():
	primos = []
	for x in range(1, limite / 100):
		if funcoes.is_prime(x):
			primos.append(x)

'''
usado para retornar o indice onde não precisarei somar, pois a soma de qualquer número
acima da metade será maior que o limite
'''
for x in range(1, limite):
	if funcoes.is_prime(x):
		lista_primos.append(x)
		if x > (limite / 2) and achou_indice == False:
			nao_considerar_apos_indice = lista_primos.index(x) - 1
			achou_indice = True
print(nao_considerar_apos_indice, lista_primos[nao_considerar_apos_indice])



'''
41537 499979
for x in range(1, limite):
	if funcoes.is_prime(x):
		lista_primos.append(x)
		if x > (limite / 2) and achou_indice == False:
			nao_considerar_apos_indice = lista_primos.index(x) - 1
			achou_indice = True

print(nao_considerar_apos_indice, lista_primos[nao_considerar_apos_indice])
'''