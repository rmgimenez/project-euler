'''
Factorial digit sum
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
from time import time
start = time()

import funcoes

resultado_fatorial = funcoes.fatorial(100)
resposta = 0
for numero in str(resultado_fatorial):
	resposta = resposta + int(numero)

print(resposta)

print("Time: {0} secs".format(time()-start))