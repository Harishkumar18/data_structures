"""https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/"""

from collections import defaultdict
from heapq import heappush, heapify, heappop


def create_minimum_spanning_tree(graph, starting_vertex):
    # mst to store the path of the minimum spanning tree
    mst = defaultdict(set)
    # visited will track of visited nodes to avoid going to already visited node
    visited = {starting_vertex}
    # heap where we are storing the cost, from and to of all the nodes and edges
    edges = [(cost, starting_vertex, to) for to, cost in graph[starting_vertex].items()]
    # heapify the edges so that will process the minimum cost path at first
    heapify(edges)

    # looping till edges become empty
    while edges:
        # pop the path which has the smallest value in the heap and process
        cost, frm, to = heappop(edges)
        if to not in visited:
            # if the to node is not visited mark the node as visited
            visited.add(to)
            # add the node and edge to the minimum spanning tree
            mst[frm].add(to)
            # add the cost and to values of the current nodes into the heap
            for to_next, cost in graph[to].items():
                # if the next nodes of the current node is not visited then add the cost and to to the heap
                if to_next not in visited:
                    # push the to node and cost of the current node to the heap
                    heappush(edges, (cost, to, to_next))
    return mst


graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1},
    'G': {'F': 1},
}
mst = create_minimum_spanning_tree(graph, "A")
print(mst)