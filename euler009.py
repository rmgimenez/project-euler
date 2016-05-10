'''
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Answer: 31875000
'''
def valor_c(a, b):
	return (a**2 + b**2)**0.5

for a in range(1,1000):
	for b in range(1,1000):
		c = valor_c(a, b)
		if a + b + c == 1000:
			resposta = a * b * c
			print("a =", a)
			print("b =", a)
			print("c =", a)
			break
	else:
		continue
	break

print(resposta)

'''
Ajuda sobre os break e continue que coloquei no código
http://stackoverflow.com/questions/6346492/how-to-stop-a-for-loop
'''
