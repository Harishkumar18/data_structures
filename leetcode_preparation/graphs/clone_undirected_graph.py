"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Run Time Complexity
The Time complexity for cloning the graph is O(V+E) and thats because we shall be traversing each vertex of the graph from the Queue and then visiting each edge E atleast once.
"""

import collections


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        # copying the current node
        nodecopy = Node(node.val)
        # creating the hash map to not keep track of the node neighbors
        hash_map = {node:nodecopy}
        # add the node in the dequeue data structure
        queue = collections.deque([node])
        # do the operation till the queue contains elements
        while queue:
            # pop the first element in the queue
            node = queue.popleft()
            # iterating through the elements and process it
            for neighbor in node.neighbors:
                # if the neighbor is not visited
                if neighbor not in hash_map:
                    # copy the neighbor val
                    neighborcopy = Node(neighbor.val)
                    # add the entry to the hash map
                    hash_map[neighbor] = neighborcopy
                    # add the current neighbor to the cloned node neighbor
                    hash_map[node].neighbors.append(neighborcopy)
                    # add the neighbor in to the queue for further processing
                    queue.append(neighbor)
                else:
                    # if neighbor is not visited simply add the cloned neighbor as the current neighbor
                    hash_map[node].neighbors.append(hash_map[neighbor])
        return nodecopy