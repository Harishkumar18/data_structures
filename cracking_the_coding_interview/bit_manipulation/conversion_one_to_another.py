"""
Given two numbers ‘a’ and b’. Write a program to count number of bits needed to be flipped to convert ‘a’ to ‘b’.

Input : a = 10, b = 20
Output : 4
Binary representation of a is 00001010
Binary representation of b is 00010100
We need to flip highlighted four bits in a
to make it b.

solution:
 1. Calculate XOR of A and B.
        a_xor_b = A ^ B
  2. Count the set bits in the above
     calculated XOR result.
        countSetBits(a_xor_b)
"""


def countsetbits(n):
    count = 0
    while n:
        count+=1
        n&=n-1
    return count


def convertbit(a, b):
    return countsetbits(a^b)


a = 10
b = 20
print(convertbit(a, b))