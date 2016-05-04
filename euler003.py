'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
#import funcoes

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

maior_divisor = 0
numero = 600851475143
for x in range(1, round(numero**0.5)):
	if x % 2 != 0:
		if numero % x == 0:
			if is_prime(x):
					if x > maior_divisor:
						maior_divisor = x
						print(x)

print('Maior divisor =', maior_divisor)
