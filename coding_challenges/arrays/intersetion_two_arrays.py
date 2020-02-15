"""
Description: intersection of two arrays in python
"""


def find_intersection(a,b):
    intersect_elem = list(set(a).intersection(set(b)))
    all_intersection = list()
    for i in intersect_elem:
        res = (min(a.count(i), b.count(i)))
        for each in range(res):
            all_intersection.append(i)
    return all_intersection

if __name__ == '__main__':
    a = [1,2,1]
    b= [2,2]
    res = find_intersection(a,b)
    print(res)