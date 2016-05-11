'''
Self powers
Problem 48
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''
from time import time
start = time()

total = 0
for i in range(1, 1001):
	total = total + (i**i)
print(str(total)[-10::])

print("Time: {0} secs".format(time()-start))

# resolvido