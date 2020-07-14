"""
Reverse the arguments for he functions -> Animaker question
"""
from functools import wraps


def power_function(a, b):
    return a**b


def modify_argument(func):
    @wraps(func)
    def modified_power(*args):
        return func(*args[::-1])
    return modified_power


print(power_function(2, 3))
modified_power = modify_argument(power_function)
print(modified_power(2, 3))