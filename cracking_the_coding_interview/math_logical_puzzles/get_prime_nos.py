"""
Usual way to find the prime no
"""
import math


def isPrime(no):
    if no < 2:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True


"""
The /n is sufficient because, for every number a which divides n evenly, there is a complement b, where
a * b = n. If a > /n, then b < /n (since ( /n)2 = n ). We therefore don't need a to check n's
primality, since we would have already checked with b.
"""


def isPrime2(no):
    if no < 2:
        return False
    for i in range(2, math.ceil(math.sqrt(no))):
        if no % i == 0:
            return False
    return True


print(isPrime(7) == isPrime(7))
print(isPrime(10) == isPrime2(10))
