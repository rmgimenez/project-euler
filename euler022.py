'''
Names scores
Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first 
names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply 
this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
from time import time
start = time()

def valor_letra(letra):
	if letra == 'A': return 1
	elif letra == 'B': return 2
	elif letra == 'C': return 3
	elif letra == 'D': return 4
	elif letra == 'E': return 5
	elif letra == 'F': return 6
	elif letra == 'G': return 7
	elif letra == 'H': return 8
	elif letra == 'I': return 9
	elif letra == 'J': return 10
	elif letra == 'K': return 11
	elif letra == 'L': return 12
	elif letra == 'M': return 13
	elif letra == 'N': return 14
	elif letra == 'O': return 15
	elif letra == 'P': return 16
	elif letra == 'Q': return 17
	elif letra == 'R': return 18
	elif letra == 'S': return 19
	elif letra == 'T': return 20
	elif letra == 'U': return 21
	elif letra == 'V': return 22
	elif letra == 'W': return 23
	elif letra == 'X': return 24
	elif letra == 'Y': return 25
	elif letra == 'Z': return 26


arquivo = open('euler022-nome.txt')
nomes = arquivo.read()
posicao = 1
total = 0
nomes = nomes.split(',')
nomes.sort()
for nome in nomes:
	nome = nome.replace('\"', '')
	valor_nome = 0
	for letra in nome:
		valor_nome = valor_nome + valor_letra(letra)
	total = total + (valor_nome * posicao)

	posicao = posicao + 1

print(total)
print("Time: {0} secs".format(time()-start))
