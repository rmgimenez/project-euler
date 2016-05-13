# -*- coding: utf-8 -*-
'''
Large non-Mersenne prime
Problem 97
The first known prime found to exceed one million digits was discovered in 1999, and is a 
Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently 
other Mersenne primes, of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 
digits: (28433*(2**7830457))+1.

Find the last ten digits of this prime number.

http://code.jasonbhill.com/c/project-euler-97/
Since we’re only looking for the final ten digits of the number, we can form a solution 
modulo a sufficiently large number, effectively forgetting about any larger power digits. 
We’ll do all of the powers of two first, then multiply by the constant, then add one. 
We’ll take the first ten digits of the result and that should be the answer we’re looking for. 
I’d say that this one is pretty quick and painless.

Essa é a forma para achar o resultado de um problema em módulo. Isso é utilizado em vários problemas
'''
n = 2
for i in range(7830456):
    n = (2 * n) % 10000000000
 
n *= 28433
n += 1
 
n = n % 10000000000

print("Resultado =",n)

# resolvido 8739992577