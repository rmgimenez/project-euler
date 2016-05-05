'''
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

1(elevado ao quadrado) + 2(elevado ao quadrado) + ... + 10(elevado ao quadrado) = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)(elevado ao quadrado) = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

25164150
[Finished in 0.1s]
'''
def soma_dos_quadrados(numeros):
	total = 0
	for x in range(1, numeros + 1):
		total = total + (x ** 2)
	return total

def quadrado_da_soma(numeros):
	soma = 0
	for x in range(1, numeros + 1):
		soma = soma + x
	return soma ** 2

numero = 100
print(quadrado_da_soma(numero) - soma_dos_quadrados(numero))
