'''
Largest palindrome product
Problem 4
Published on Friday, 16th November 2001, 06:00 pm; Solved by 296265; Difficulty rating: 5%
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import funcoes

maior = 0
for x in range(100, 1000):
	for y in range(100, 1000):
		produto = x * y
		if funcoes.is_palindrome(produto):
			if produto > maior:
				maior = produto

print(maior)

# resolvido