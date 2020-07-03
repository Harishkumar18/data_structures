def find_positiveno(arr):
    if not arr:
        return arr
    arr.append(0)
    n = len(arr)
    for i in range(n):
        if arr[i] < 0 or arr[i] > n:
            arr[i] = 0
    for i in range(n):
        print(arr[i] % n)
        arr[arr[i] % n] += n
    for i in range(1, n):
        if arr[i] // n == 0:
            return i
    return n


def find_first_postitive(arr):
    """second approach for the same problem"""
    n = len(arr)
    containsOne = False
    for i in range(n):
        if arr[i] == 1:
            containsOne = True
        elif arr[i] <= 0 or arr[i] > n:
            arr[i] = 1
    if not containsOne:
        return 1
    for i in range(n):
        index = abs(arr[i]-1)
        if arr[index] > 0:
            arr[index] = -arr[index]
    for i in range(n):
        if arr[i] > 0:
            return i+1
    return n+1


print(find_positiveno([3, 4, -1, 1, 0]))
print(find_first_postitive([3, 4, -1, 1, 0]))
print(find_positiveno([-10,-1,-2]))
