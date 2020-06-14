def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# UTILITY FUNCTIONS
# function to print an array
def printArray(arr, size):
    for i in range(size):
        print ("% d" % arr[i], end =" ")


def do_rotation(arr, k, n):
    # n = len(arr)
    sets = gcd(k, n)
    # import pdb;pdb.set_trace()
    for i in range(sets):
        j = i
        temp = arr[0]
        while 1:
            d = j + k
            if d >= n:
                d = d-n
            if d == i:
                break
            arr[j] = arr[d]
            j = d
        arr[j] = temp
    return arr


# print(do_rotation([1, 2, 3, 4, 5], 2))
# Driver program to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
k = 3
do_rotation(arr, k, n)
printArray(arr, n)
