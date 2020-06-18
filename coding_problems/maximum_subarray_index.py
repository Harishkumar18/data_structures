array = [-3, 1, -8, 12, 0,5, -3, -9, 5]
array = [-2,1,-3,4,-1,2,1,-5,4]
# TODO: Need to improve

def find_max_subarray_sum(array):
    end = []
    global_max = array[0]
    current_max = array[0]
    for element in range(1, len(array)):
        current_max = max(array[element], current_max+array[element])
        if current_max > global_max:
            global_max = current_max
            end.append(array[element])
    print(end)
    # print(array.index(max(end)),array.index(end[-1]) + 1)
    print(array[array.index(max(end)):array.index(end[-1]) + 1])
    return global_max


print(find_max_subarray_sum(array))
