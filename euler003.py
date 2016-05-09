'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import funcoes

maior_divisor = 0
numero = 600851475143
for x in range(1, round(numero**0.5)):
	if x % 2 != 0:
		if numero % x == 0:
			if funcoes.is_prime(x):
					if x > maior_divisor:
						maior_divisor = x
						#print(x)

print('Maior divisor =', maior_divisor)
