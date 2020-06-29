"""
The Sieve of Eratosthenes is a highly efficient way to generate a list of primes. It works by recognizing that
all non-prime numbers are divisible by a prime number.
We start with a list of all the numbers up through some value max. First, we cross off all numbers divisible by
2. Then, we look for the next prime (the next non-crossed off number) and cross off all numbers divisible by
it. By crossing off all numbers divisible by 2, 3, 5, 7, 11, and so on, we wind up with a list of prime numbers
from 2 through max.
"""
import math


def list_of_primes(no):
    limit = math.floor(math.sqrt(no))
    primes = [True] * (no + 1)
    primes[0], primes[1] = False, False
    p = 2
    while p  <= limit:
        if primes[p]:
            for i in range(p * 2, no + 1, p):
                primes[i] = False
        p += 1
    return primes
    # for i in range(len(primes)):
    #     if primes[i]:
    #         print(i)


res = list_of_primes(50)
print([i for i in range(len(res)) if res[i] is True])
