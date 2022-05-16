"""
Given a graph and a source vertex src in graph, find shortest paths from src to all vertices in the given graph.
Dijkstra’s algorithm is a Greedy algorithm and time complexity is O((V+E)LogV) (with the use of Fibonacci heap).
Dijkstra doesn’t work for Graphs with negative weights, Bellman-Ford works for such graphs. Bellman-Ford is also simpler
than Dijkstra and suites well for distributed systems. But time complexity (average/worst) of Bellman-Ford is O(VE),
which is more than Dijkstra. Best case is O(E). Space complexity is O(V).

Bellman Ford's algorithm and Dijkstra's algorithm are very similar in structure. While Dijkstra looks only to the
immediate neighbors of a vertex, Bellman goes through each edge in every iteration.

https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
https://www.programiz.com/dsa/bellman-ford-algorithm
"""


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, s, d, w):
        self.edges.append([s, d, w])

    def print_solution(self, dist):
        print("Vertex distance from source:")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Relax edges |V| - 1 times as that is the max number of times a vertex's weight can be updated
        for _ in range(self.V - 1):
            for s, d, w in self.edges:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # Detect negative cycle
        # If value changes then we have a negative cycle in the graph and we cannot find the shortest distances
        for s, d, w in self.edges:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        # No negative weight cycle found
        self.print_solution(dist)


def main():
    g = Graph(5)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 4, 3)
    g.add_edge(2, 1, 1)
    g.add_edge(2, 3, 4)
    g.add_edge(2, 4, 5)
    g.add_edge(4, 3, -5)
    g.bellman_ford(0)


if __name__ == '__main__':
    main()