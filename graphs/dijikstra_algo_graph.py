"""
https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/

Dijkstra’s algorithm is an iterative algorithm that provides us with the shortest path from one particular starting
node to all other nodes in the graph. To keep track of the total cost from the start node to each destination we will
make use of a distances dictionary which we will initialize to 0 for the start vertex, and infinity for the other
vertices. Our algorithm will update these values until they represent the smallest weight path from the start to the
vertex in question, at which point we will return the distances dictionary.

Things to consider: It is important to note that Dijkstra’s algorithm works only when the weights are all positive.
You should convince yourself that if you introduced a negative weight on one of the edges to the graph that the
algorithm would never exit.

Analysis of Dijkstra’s Algorithm
We will now consider the running time of Dijkstra’s algorithm.

Building the distances dictionary takes O(V)O(V) time since we add every vertex in the graph to the dictionary.

The while loop is executed once for every entry that gets added to the priority queue. An entry can only be added
when we explore an edge, so there are at most O(E)O(E) iterations of the while loop.

The for loop is executed at most once for every vertex, since the current_distance > distances[current_vertex] check
ensures that we only process a vertex once. The for loop iterates over outgoing edges, so among all iterations of the
while loop, the body of the for loop executes at most O(E)O(E) times.

Finally, if we consider that each priority queue operation (adding or removing an entry) is O(\log E)O(logE),
we conclude that the total running time is O(V + E \log E)O(V+ElogE). """
from heapq import  heappush, heappop


def calculate_distances(graph, starting_vertex):
    # create distances map with max values initially
    distances = {vertex: float('infinity') for vertex in graph}
    # mark the starting vertex distance as 0 a->a = 0
    distances[starting_vertex] = 0

    # initialize the queue with 0 distance and the starting vertex
    queue = [(0, starting_vertex)]

    while queue:
        print("q", queue)
        # pop the smallest element from the queue
        current_distance, current_vertex = heappop(queue)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            # add the weight with the current index
            distance = current_distance+weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(queue, (distance, neighbor))

    return distances


graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
print(calculate_distances(graph, 'X'))