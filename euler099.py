'''
Largest exponential
Problem 99
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm 
that 211 = 2048 < 37 = 2187.

However, confirming that 632382**518061 > 519432**525806 would be much more difficult, as both
numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one 
thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.

log(x elevado a y) = y * log(x)
'''
import math

lista = []
arquivo = open('euler099_base_exp.txt')
linhas = arquivo.read()
linhas = linhas.splitlines();
i = 1
maior = 0
resposta = 0
for linha in linhas:
	partes = list(linha.split(','))
	base = int(partes[0])
	expoente = int(partes[1])
	valor = expoente * math.log(base)
	if valor > maior:
		maior = valor
		resposta = i
	i += 1

print(resposta)
	
# resolvido