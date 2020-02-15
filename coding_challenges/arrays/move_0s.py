"""
Description : move all 0's to the left

"""


def move(nums):
    valid = 0
    for i, num in enumerate(nums):
        print("out if loop", i, num)
        if num!=0:
            print("inside loop", nums[valid], nums[i])
            nums[valid], nums[i] = nums[i], nums[valid]
            valid+=1


if __name__ == '__main__':
    a = [0,1,0,3,1,2]
    move(a)
    print(a)