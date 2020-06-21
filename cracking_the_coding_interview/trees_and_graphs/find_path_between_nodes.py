"""
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.

Complexity Analysis:

Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph.
Space Compelxity: O(V).
There can be atmost V elements in the queue. So the space needed is O(V).
"""

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isReachable(self, s ,d):
        # using bfs approach
        visited = [False]*self.v
        # create a queue for BFS
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            node = queue.pop(0)
            if node == d:
                return True
            for i in self.graph[node]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return False


g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
print(g.graph)
u = 1
v = 3
if g.isReachable(u, v):
    print("path is found")
else:
    print("no path")