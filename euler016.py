'''
Power digit sum
Problem 16
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''
numero = 2**1000
soma = 0
for x in str(numero):
	soma = soma + int(x) 

print(soma)