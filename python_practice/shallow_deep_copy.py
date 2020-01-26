"""
Decription: check the shallow and deep copy in python

"""

import copy

# shallow copy examples
a = [[1,1,1],[2,2,2],[3,3,3]]
b = copy.copy(a)
print(f"value of a is:{a}")
print(f"value of b is:{b}")
# one insertion
a.append([4,4,4])
print(f"value of a is:{a}")
print(f"value of b is:{b}")
# one modification
a[1][0] = 2.0
print(f"value of a is:{a}")
print(f"value of b is:{b}")

# deep copy examples
a = [[1,1,1],[2,2,2],[3,3,3]]
b = copy.deepcopy(a)
print(f"value of a is:{a}")
print(f"value of b is:{b}")
# one insertion
a.append([4,4,4])
print(f"value of a is:{a}")
print(f"value of b is:{b}")
# one modification
a[1][0] = 2.0
print(f"value of a is:{a}")
print(f"value of b is:{b}")