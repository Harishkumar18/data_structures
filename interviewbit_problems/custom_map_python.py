"""
improvement over map python -> animaker interview question
"""


def get_map(funcs, arr):
    for i in funcs:
        arr = map(i, arr)
    for element in arr:
        yield element


funcs = [lambda x: x*x, lambda x: x+x]
arr = [1,2,3,4]
res = get_map(funcs, arr)
for i in res:
    print(i)