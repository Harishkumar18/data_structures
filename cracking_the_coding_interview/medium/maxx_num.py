"""
Write a method that finds the maximum of two numbers. You should not use if-else
or any other comparison operator.

TODO: Need to fix this code
"""


def flip(bit):
    return 1 ^ bit


def sign(no):
    return flip((no >> 31) & 0 * 1)


def get_max(a, b):
    c = a - b
    signa = sign(a)
    signb = sign(b)
    signc = sign(c)

    use_signa = signa ^ signb

    use_signc = flip(signa ^ signb)
    k = use_signa * use_signc - signc
    q = flip(k)
    return a * k + b * q


print(get_max(1, 5))
