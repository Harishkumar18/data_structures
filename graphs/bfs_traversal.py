from graphs.basic_graph_using_adj_list import Graph


class BFS:
    def bfs_traversal(self, graph, start):
        visited = {i: False for i in graph}
        queue = []
        queue.append(start)
        visited[start] = True
        while queue:
            start = queue.pop(0)
            for node in graph[start]:
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)
            print(start)

        return queue


g = Graph()
g.add_edge("1", "2")
g.add_edge("1", "3")
g.add_edge("2", "1")
g.add_edge("2", "3")
g.add_edge("3", "4")
g.add_edge("4", "3")
g.add_edge("3", "1")
g.add_edge("3", "2")
bfs = BFS().bfs_traversal(g.graph, "2")
print(bfs)