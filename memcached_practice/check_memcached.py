from memcached_practice.decorators_file import timeit
from pymemcache.client import base

client = base.Client(('localhost', 11211))

@timeit
def check_with_memcached():
  result = client.get('computation')
  if not result:
      result = normal_function()
      client.set('computation', result)
  return result


@timeit
def normal_function():
    no_list = range(0, 1000000)
    result = 0
    for element in no_list:
        result += element * element
    return result


print(normal_function())
print(check_with_memcached())
