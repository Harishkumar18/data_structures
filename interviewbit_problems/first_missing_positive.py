
def find_positiveno(arr):
    if not arr:
        return arr
    arr.append(0)
    n = len(arr)
    for i in range(n):
        if arr[i]<0 or arr[i]>n:
            arr[i] = 0
    for i in range(n):
        print(arr[i] % n)
        arr[arr[i]%n]+=n
    for i in range(1, n):
        if arr[i]//n ==0:
            return i
    return n


print(find_positiveno([3, 4, -1, 1, 0]))
# print(find_positiveno([-10,-1,-2]))
