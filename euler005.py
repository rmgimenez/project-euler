'''
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Menor: 232792560
[Finished in 128.3s]
'''
procurar = True
i = 2
while procurar:
	is_divisivel = True
	for x in range(3, 21):
		if i % x != 0:
			is_divisivel = False
			break
	if is_divisivel:
		procurar = False
	else:	
		i = i + 2

print('Menor: %d' % i)