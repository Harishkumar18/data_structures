
from heapq import heapify, heappop, heappush, _heappop_max, heappushpop


class MaxHeap:
    def __init__(self):
        self.heap = [0]

    def parent(self, i):
        if i>1:
            return i//2

    def insert(self, val):
        heappushpop(self.heap, val)

    def extractmax(self):
        _heappop_max(self.heap)

    def getmax(self):
        return self.heap[1]



m1 = MaxHeap()
m1.insert(1)
m1.insert(2)
m1.insert(3)
print(m1.getmax())