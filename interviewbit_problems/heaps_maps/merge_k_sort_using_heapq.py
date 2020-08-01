"""
Brute force apporach:
Concatenate all arrays into one large array and sort the large array.

Sorting will always expense us O(n * log(n)) at the least when sorting non-special data that we only know a total ordering property for (then we can use merge sort or quick sort).

This does not use the fact that each array is sorted already which (should) help us on time complexity.

Approach :

When building our final output array that is the sorted set of all the items we will be placing an item one by one from the original k arrays
What is are the items in each of those k arrays that interest us? The smallest items.

How can we keep track of the smallest item of the k smallest items respective to each array?

A min-heap is optimal.

Since we will hold at max k items in the min-heap we know what we will have at least O(k) time complexity where k is # of sorted arrays we need to maintain the smallest item across.

We will take the smallest item from the min-heap and remember the array it came from so that we can add the next item in that array to the min heap (if it exists).


Example Walkthrough:

Input
[ [3, 5, 7], [0, 6], [0, 6, 28] ]

Our output array will have size 8 [ _, _, _, _, _, _, _, _ ]

Let us step through this:

Initialize: Min Heap: [3, 0, 0]

[ 0, _, _, _, _, _, _, _ ]
Min Heap: [3, 0, 6] (0 came from array 2, we add the next item 6)

[ 0, 0, _, _, _, _, _, _ ]
Min Heap: [3, 6, 6] (0 came from array 3, we add the next item 6)

[ 0, 0, 3, _, _, _, _, _ ]
Min Heap: [5, 6, 6] (3 came from array 1, we add the next item 5)

[ 0, 0, 3, 5, _, _, _, _ ]
Min Heap: [7, 6, 6] (5 came from array 1, we add the next item 7)

[ 0, 0, 3, 5, 6, _, _, _ ]
Min Heap: [7, 6] (6 came from array 2, array 2 is finished)

[ 0, 0, 3, 5, 6, 6, _, _ ]
Min Heap: [7, 28] (6 came from array 3, we add the next item 28)

[ 0, 0, 3, 5, 6, 6, 7, _ ]
Min Heap: [28] (7 came from array 1, array 1 is finished)

[ 0, 0, 3, 5, 6, 6, 7, 28 ]
Min Heap: [] (28 came from array 3, array 3 is finished)

Output
[ 0, 0, 3, 5, 6, 6, 7, 28 ]


Complexities

Time: O( 2(n * log(k))) = O( n * log(k) )

Let n be the total elements across the k sorted arrays we are given.

Extracting and adding to the min heap will both take log(k) time.

For each of the n items, we will do an addition to the heap and removal from the heap (log(k) expense per heap operation).

Hence the times 2. It is dropped. We get O( n * log(k) ).

Space: O( k )

Our heap will need to hold k elements for most of this process and cannot worsen past this.

We are not counting the size of the output array which uses O(n) space since that isn't core to our algorithm.
"""
from heapq import heappush, heappop


# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = new_head = ListNode(0)
        q = []
        for list_head_id, list_head in enumerate(lists):
            if list_head:
                heappush(q, (list_head.val, list_head_id, list_head))
        while q:
            _, list_id, new_head.next = heappop(q)
            new_head = new_head.next
            if new_head.next:
                heappush(q, (new_head.next.val, list_id, new_head.next))
        return dummy.next
