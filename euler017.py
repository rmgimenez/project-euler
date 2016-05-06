'''
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then 
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance 
with British usage.
'''
def nome_numero(numero):
	if numero == 1:
		return 'one'
	elif numero == 2:
		return 'two'
	elif numero == 3:
		return 'three'
	elif numero == 4:
		return 'four'
	elif numero == 5:
		return 'five'
	elif numero == 6:
		return 'six'
	elif numero == 7:
		return 'seven'
	elif numero == 8:
		return 'eight'
	elif numero == 9:
		return 'nine'

	elif numero == 10:
		return 'ten'