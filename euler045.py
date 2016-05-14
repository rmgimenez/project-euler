# -*- coding: utf-8 -*-
'''
Triangular, pentagonal, and hexagonal
Problem 45
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.

Posso alterar o problema, pois todos os número triangulares são hexagonais, não precisaria fazer esse teste, mas por enquanto o script faz esse teste
'''
import funcoes
from time import time
start = time()

achou = False
# comecei com i = 285, pois abaixo disso não interessa para o problema
i = 285
while achou == False:
	i += 1
	t = funcoes.triangulo(i)
	if funcoes.is_pentagono(t) and funcoes.is_hexagonal(t):
		achou = True
		print(t)

print("Time: {0} secs".format(time()-start))

# resolvido