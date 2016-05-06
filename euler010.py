'''
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from time import time
start = time()

import funcoes

soma = 0
for x in range(1, 2000000):
	if funcoes.is_prime(x):
		soma = soma + x

print(soma)
print("Time: {0} secs".format(time()-start))