"""
Multiply the numbers using bitwise operator
"""


def get_product(a, b):
    res = 0

    while b > 0:
        if b & 1:
            res += a

        a = a << 1
        b = b >> 1
    return  res


ans = get_product(5, 10)
print(ans)