import time


def timeit(method):
    def timed(*args, **kwargs):
        start_time = time.time()
        result = method(*args, **kwargs)
        end_time = time.time()
        print('%r  %2.2f ms' %(method.__name__, (end_time - start_time) * 1000))
        return result
    return timed