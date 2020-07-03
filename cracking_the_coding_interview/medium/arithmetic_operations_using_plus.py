"""
Given two numbers, perform multiplication, subtraction and division operations on them, using ‘+’ arithmetic operator
only.

Subtraction :-  a - b = a + (-1)*b.
Multiplication :- a * b = a + a + a ... b times.
Division :- a / b =  continuously subtract b from a and count how many times we can do that.
"""


def flipsign(no):
    """this function will give negation of the given number"""
    neg = 0
    tmp = 1 if no < 1 else -1
    while no != 0:
        neg += tmp
        no += tmp
    return neg


def aredifferent(a, b):
    """check whether both numbers having differnt sign or not"""
    return (a < 0 and b > 0) or (a > 0 and b < 0)


def subtract(a, b):
    """The negation of the value k is implemented by adding -1 k times. Observe that this will take O ( k) time"""
    return a + flipsign(b)


def multiply(a, b):
    """Function to multiply a by b by adding a to itself b times"""
    # algo will be faster if b>a
    if b < a:
        return multiply(b, a)
    product = 0
    for _ in range(abs(b), 0, -1):
        product += a

    if b < 0:
        product = flipsign(product)

    return product


def divide(a, b):
    quotient = 0
    divisor = flipsign(abs(b))
    for dividend in range(abs(a), abs(divisor) + divisor, divisor):
        quotient += 1
    if aredifferent(a, b):
        quotient = flipsign(quotient)
    return quotient


print(subtract(6, 2))
print(multiply(5, 6))
print(multiply(-5, -6))
print(multiply(-5, 6))
print(multiply(5, -6))
print(f"ans is :{divide(15, 5)}")
print(f"ans is :{divide(5, 15)}")
print(f"ans is :{divide(-15, 5)}")
print(f"ans is :{divide(-15, -5)}")
