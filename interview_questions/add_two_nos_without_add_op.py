"""
add two no without addition operator
"""


def add(a, b):
    while b:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


result = add(3, 5)
print(result)
