def BinarySearch(num):
    left = 0
    right = num

    while left <= right:
        print(left, right)
        mid = left + (right - left) // 2
        if mid ** 2 == num:
            return True
        elif mid ** 2 > num:
            right = mid - 1
        else:
            left = mid + 1
    print(left, right)
    return False

BinarySearch(49)


def Math(num):
    i = 1
    while (num > 0):
        print(num, 2)
        num -= i
        i += 2
    return num == 0

Math(49)