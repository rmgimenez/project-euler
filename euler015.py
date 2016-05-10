'''
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''
import math

tamanho_matriz = 20

caminhos_percorridos = ()
matriz = []
for x in range(0,tamanho_matriz):
	linha = []
	linha.clear()
	for y in range(0,tamanho_matriz):
		linha.append(0)
	matriz.append(linha)

i = 0
while i < len(matriz):
	y = 0
	while y < len(matriz):
		matriz[i][y] = 1
		y += 1
	i += 1

'''
print(math.factorial(40)/(math.factorial(20)*math.factorial(20)))
Com a linha acima chega na resposta, mas não entendi a explicação
'''
