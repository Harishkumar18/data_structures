def contigous_max_sum(arr):
    global_sum = curr_sum = arr[0]
    for i in range(1, len(arr)):
        curr_sum = max(curr_sum+arr[i], arr[i])
        global_sum = max(curr_sum, global_sum)
    return global_sum


arr = [1, 2, -43, 20, -50, 7, 8]
res = contigous_max_sum(arr)
print(res)