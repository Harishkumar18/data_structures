"""
Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a
method to find the location of a given string.
EXAMPLE
Input: ball, {"at",""}
Output: 4

appraoch:
If it weren't for the empty strings, we could simply use binary search. We would compare the string to be
found, s tr, with the midpoint of the array, and go from there.
With empty strings interspersed, we can implement a simple modification of binary search. All we need to
do is fix the comparison against mid, in case mid is an empty string. We simply move mid to the closest
non-empty string.

The worst-case runtime for this algorithm is O ( n). In fact, it's impossible to have an algorithm for this
problem that is better than O(n) in the worst case. After all, you could have an array of all empty strings
except for one non-empty string. There is no "smart" way to find this non-empty string. In the worst case,
you will need to look at every element in the array.
Careful consideration should be given to the situation when someone searches for t he empty string. Should
we find the location (which is an O( n) operation)? Or should we handle this as an error?
There's no correct answer here. This is an issue you should raise with your interviewer. Simply asking this
question will demonstrate that you are a careful coder.
"""


def search_element(a, first, last, x):
    if last < first:
        return -1
    mid = first+last//2
    omid = mid
    if not a[mid]:
        left = mid-1
        right = mid+1
        while True:
            if left<first and right>last:
                return -1
            elif right<=last and a[right]:
                mid = right
                break
            elif first<=left and a[left]:
                mid = left
                break
            left-=1
            right+=1
    if a[mid] == x:
        return mid
    elif a[mid]<x:
        return search_element(a, mid+1, last, x)
    else:
        return search_element(a, first, omid, x)


a = ["at", "", "", "", "", "", "", "", "bat"]
first = 0
last = len(a)
x = "bat"
print(search_element(a, first, last, x))
