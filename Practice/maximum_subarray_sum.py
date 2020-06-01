array = [-3, 1, -8, 12, 0, -3, 5, -9, 5]
array = [-2,1,-3,4,-1,2,1,-5,4]


def find_max_subarray_sum(array):
    global_max = array[0]
    current_max = array[0]
    for element in range(1, len(array)):
        current_max = max(array[element], current_max+array[element])
        if current_max > global_max:
            global_max = current_max
    return global_max


print(find_max_subarray_sum(array))
