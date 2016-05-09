# teste
import funcoes

lista_primos = []
for x in range(1,1000000):
	if funcoes.is_prime(x):
		lista_primos.append(x)
#print(len(lista_primos))