'''
Maximum path sum II
Problem 67
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), 
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try 
every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) 
routes every second it would take over twenty billion years to check them all. There is an 
efficient algorithm to solve it. ;o)
euler067_p067_triangle.txt
'''
from time import time
start = time()

f = open("euler067_p067_triangle.txt", "r").readlines()
triangulo = []
for line in f:
    temp = []
    for token in line.replace("\n", "").split(' '):
        temp.append(token)
    triangulo.append(temp)

triangulo = list(reversed(triangulo))

i = 1 # começa da segunda linha
while i < len(triangulo):
  linha_atual = list(triangulo[i])
  linha_anterior = list(triangulo[i-1])
  j = 0
  while j < len(linha_atual):
    soma1 = int(linha_atual[j]) + int(linha_anterior[j])
    soma2 = int(linha_atual[j]) + int(linha_anterior[j+1])
    if soma1 > soma2:
      triangulo[i][j] = soma1
    else:
      triangulo[i][j] = soma2
    j += 1
  i += 1
print("Resposta: ", triangulo[len(triangulo)-1])

print("Time: {0} secs".format(time()-start))

# resolvido