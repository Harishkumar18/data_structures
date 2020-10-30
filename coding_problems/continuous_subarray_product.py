"""
Given an integer array, find the contiguous subarray within an array which has the largest product and return the largest product.

For example:-

Given [2,3,-2,4] return 6
Given [-2,-1,0,3] return 3

[2,-3,2,4] - 8

g, c =2
l1: curr_max = (-6, -3) = -3
el2: curr_max = (-3, -6) = -3
el3: curr_max = (-6, 2) = 2
el4: curr_max = (8, 4) = 8
 

[2,3,2,4]
global, curr = 2, 2
e1 : 3 : curr_max = max(6, 3) = 6 global_max = 6
e2: 2  : curr_max = max(12, 2)  =12 global_max= 12
e3: 4  : curr_max = max(48, 4) = 48 global_max =  48
48

[2,3,0,2,4]
global, curr = 2, 2
e1: 2: curr_max = (6, 3) = 3 global_max = 6
e2: 0: curr_max = (0, 0) = 0 
e3: 2: curr_max = (0, 2) =2 
e4: 4: curr_max = (2, 8) = 8 global_max = 8
"""   
  
def largest_product(arr):
  global_max, curr_max = arr[0], arr[0]
  for i in range(1, len(arr)):
    curr_max = max(curr_max*arr[i], arr[i])
    if curr_max > global_max:
      global_max = curr_max
  return global_max

Dry run:
global, curr = 2, 2
curr_max(6, 3)
