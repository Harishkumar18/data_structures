"""
Decorator pattern
"""
import time


def timeit(func):
    def _time_calculation(*args, **kwargs):
        s = time.time()
        print("started time of the function", s)
        res = func(*args, **kwargs)
        print("end time of the function", time.time()-s)
        return res
    return _time_calculation


@timeit
def add_num(a, b):
    return a+b


res = add_num(5, 6)
print(res)