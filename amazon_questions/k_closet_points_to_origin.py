"""
K Closest Points to Origin
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
"""

import math
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        Its a naive approach
        intuition: we can sort the list by adding the square of the each value and take only top K elements
        TC: O(nlogn)
        """
        if not points:
            return []
        mapping = {}
        # store the mapping for index and its addition of square values
        for index, each in enumerate(points):
            mapping[index] = (math.pow(each[0], 2) + math.pow(each[1], 2))
        # sort the dictionary by values in ascending order
        sorted_mapping = {k: v for k, v in sorted(mapping.items(), key=lambda item: item[1])}
        result = []
        # based on the index add the values in the list
        for each in sorted_mapping:
            result.append(points[each])
        # provide only top k elements
        return result[:K]

    def kcloset(self, points, K):
        """
        optimal approach
        We keep a min heap of size K.
        For each item, we insert an item to our heap.
        If inserting an item makes heap size larger than k, then we immediately pop an item after inserting ( heappushpop ).
        TC: O(n logk)
        """
        heap = []
        for (x, y) in points:
            # be default heap will pop only the smallest element in the heap but here we need to keep the smallest
            # element and pop the largest one for that reson we are storing as negtive numbers in the heap
            dist = -(x * x + y * y)
            # We are going to store only k elements in the heap
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        return [(x,y) for (dist, x, y) in heap]


points = [[1, 3], [-2, 2]]
points2 = [[3, 3], [5, -1], [-2, 4]]
K = 1
soln_obj = Solution()
print(soln_obj.kClosest(points, K))
print(soln_obj.kcloset(points2, 2))
