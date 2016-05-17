# teste
import math

from time import time
start = time()

import funcoes

a,b,c = 1,1,2
lista = [1,1,2]
for x in range(4, 15):
	#print(x," -",a,b,c)
	a,b,c = b,c,a+b+c
	lista.append(c)
print(lista)

def tri_fib(n):
	if n == 1 or n == 2:
		return 1
	elif n <= 0:
		return 0
	elif n == 3: # coloquei aqui só para teste, quando solicitar tri_fib(3) vai retornar 2, não precisa dessa linha
		return 2 # [1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705]
	else:
		return tri_fib(n-1) + tri_fib(n-2) + tri_fib(n-3)

print(tri_fib(8))


print("Time: {0} secs".format(time()-start))