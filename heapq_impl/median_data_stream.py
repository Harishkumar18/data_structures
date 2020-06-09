from heapq import *


class MedianFinder:

    def __init__(self):
        self.small = [] #max heap
        self.large = []

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, heappushpop(self.large, num))

    def findMedian(self):
        print(self.small)
        print(self.large)
        # if len(self.small) == len(self.large):
        #     return (self.small[0]+self.large[0])//2
        # else:
        #     return self.large[0]

# for i in range(10):
# MedianFinder().addNum(2)
# MedianFinder().addNum(3)
# print(MedianFinder().findMedian())
a = [4,5]
b=[1,2,3]
heappush(a, heappushpop(b, 6))
print(a)
print(b)