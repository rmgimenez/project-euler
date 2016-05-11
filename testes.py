# teste
import funcoes
import math

from time import time
start = time()

import funcoes

resultado_fatorial = funcoes.fatorial(100)
resposta = 0
for numero in str(resultado_fatorial):
	resposta = resposta + int(numero)

print(resposta)

print("Time: {0} secs".format(time()-start))

#start = time()

resultado_fatorial = math.factorial(100)
resposta = 0
for numero in str(resultado_fatorial):
	resposta = resposta + int(numero)

print(resposta)

print("Time: {0} secs".format(time()-start))