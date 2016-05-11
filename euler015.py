'''
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

A pergunta do problema é quantos caminhos existem do ponto (0,0) até o ponto (19,19) movendo apenas para
a direita e para baixo. Pesquisei sobre o problema e o que mais encontrei foram explicações matemáticas
cuja a resposta está da seguinte forma 
resposta = (40!)/(20!*20!)
Ainda não consegui entender a solução, abaixo alguns vídeos para ajudar a entender

Solução usando um script para percorrer a matriz e ir somando valores
https://www.youtube.com/watch?v=c1hfTSkOJhQ

Solução em forma matemática
https://www.youtube.com/watch?v=1-Zx8IHJT38
print(math.factorial(tamanho_matriz*2)/(math.factorial(tamanho_matriz)*math.factorial(tamanho_matriz)))
number of ways = (2*n)! / (n! * n!)

print(math.factorial(40)/(math.factorial(20)*math.factorial(20)))
Com a linha acima chega na resposta, mas não entendi a explicação

You can solve it without programming:
It is a group of 2*n members, divided in 2 subgroups of n equal members (right / down):
number of ways = (2*n)! / (n! * n!)

you must take 20 move to right and 20 move downward ... that apply to every possible rout in order to reach destination ...  
40! is total combination of 40 different object... since 2*20 of these objects is identical so 40!/(20!*20!) is answer to problem ...

resposta = 137846528820
'''
import math

tamanho_matriz = 21

matriz = []
for x in range(0,tamanho_matriz):
	linha = []
	linha.clear()
	for y in range(0,tamanho_matriz):
		linha.append(0)
	matriz.append(linha)

for row in range(0,tamanho_matriz):
	for col in range(0,tamanho_matriz):
		if row == 0 or col == 0:
			matriz[row][col] = 1
		else:
			matriz[row][col] = matriz[row-1][col] + matriz[row][col-1]
		col += 1
	row += 1
print(matriz[tamanho_matriz-1][tamanho_matriz-1])
#for x in matriz: print(x)

# resolvido