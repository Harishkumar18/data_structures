
#TODO: need to complete

def findTwoMissingNumbers(arr, n):
    xor = arr[0]
    for i in range(1, n -2):
        xor ^= arr[i]
    for i in range(1, n+1):
        xor ^= i
    print(xor)




# Driver program to test
# above function
arr = [1, 3, 5, 6]

# Range of numbers is 2
# plus size of array
n = 2 + len(arr)
findTwoMissingNumbers(arr, n)
