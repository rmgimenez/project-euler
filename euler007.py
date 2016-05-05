'''
10001st prime
Problem 7
Published on Friday, 28th December 2001, 04:00 pm; Solved by 265193; Difficulty rating: 5%
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

104743
[Finished in 0.3s]
'''

def is_prime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		#print('\t',f)
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True

x = 2
quantidade = 0
while quantidade != 10001:
	if is_prime(x):
		quantidade = quantidade + 1
	x = x + 1
print(x - 1)