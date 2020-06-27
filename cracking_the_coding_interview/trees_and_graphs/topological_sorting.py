"""Approach: Topological sorting only applicables to DAG(Directed acyclic graph) it won't be applicable to graphif it
contains any cycles indegree - node coming into some nodes 1->2 indegree of 1 is 0 and 2 is 1.Remove the nodes
starting from node in which indegree is 0 and delete the nodes and its links.Try to order all the nodes """

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.v = vertices

    def addEdge(self, u , v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for vertex in self.graph[v]:
            if not visited[vertex]:
                self.topological_sort_util(vertex, visited, stack)
        stack.insert(0, v)

    def topological_sort(self):
        visited = [False]*self.v
        stack = []
        for i in range(self.v):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        print(stack)


vertices = 6
g = Graph(vertices)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
print(g.graph)
print(g.topological_sort())