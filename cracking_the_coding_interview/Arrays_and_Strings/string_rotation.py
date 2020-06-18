"""
String rotation
"""


def is_string_rotated(s1, s2):
    n1, n2 = len(s1), len(s2)
    if n1!=n2:
        return False
    if s2 in s1+s1:
        return True
    return False


print(is_string_rotated("harish", "rishna"))

print(is_string_rotated("harish", "rishha"))

print(is_string_rotated("harish", "rishnas"))