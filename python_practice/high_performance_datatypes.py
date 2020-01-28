"""
Description : example for high performance data types in python
"""
import collections

# counter examples

available_colors = ["red", "red", "blue", "blue", "green", "yellow","red"]
c = collections.Counter()
for color in available_colors:
    c[color] += 1
print(f"the count of the colors is:{c}")
print(f"most common color is:{c.most_common(2)}")

# dequeue

d = collections.deque(available_colors)
d.rotate(1)
print(f"after one rotations in d:{d}")

# defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = collections.defaultdict(list)
print(f"the value of d is:{d}")
for color, count in s:
    d[color].append(count)
print(f"the value is:{d}")

# same above approach using setdefault
d= dict()
for color, count in s:
    d.setdefault(color, []).append(count)
print(f"the value is:{d}")