"""
Input: [('Veg Biryani', 'Biryani'), ('Chicken Biryani', 'Biryani'), ('Egg Roll', 'Rolls'), ('Paneer wrap', 'Rolls'), ('Chicken Manchow Soup', 'Soup'), ('Egg Biryani', 'Biryani')]

Output: {'Biryani': ['Veg Biryani', 'Chicken Biryani', 'Egg Biryani'], 'Rolls': ['Egg Roll', 'Paneer wrap'], 'Soup': ['Chicken Manchow Soup']}



inp_elem = [('Veg Biryani', 'Biryani'), ('Chicken Biryani', 'Biryani'), ('Egg Roll', 'Rolls'), ('Paneer wrap', 'Rolls'), ('Chicken Manchow Soup', 'Soup'), ('Egg Biryani', 'Biryani')]

items_list = {}

for each in inp_elem:
    if each[1] in items_list:
        items_list[each[1]].append(each[0])
    else:
        items_list[each[1]] = [each[0]]

print(items_list)

"""

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Output: ["((()))","(()())","(())()","()(())","()()()"]


n = 3

inp_str = "((()))"


def well_formed(n):
    if n == 1:
        return "()"
    elif n==2:
        return 
"""


def check_denom(func):
    def func(arg1, arg2):
        if arg2 == 0:
            print("Division by zero is not possible")
            exit()
        else:
            return func(arg1, arg2)
    return func

@check_denom
def divide(a, b):
    return a/b

# print(divide(5, 0))
print(divide(15, 5))


# sql query










