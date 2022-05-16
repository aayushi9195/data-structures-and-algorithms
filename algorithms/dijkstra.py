"""
Dijkstra’s algorithm is similar to Prim's which finds the shortest path from a single source vertex to all other
vertices in the given graph.

Time complexity: O(V^2)

https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
"""

import sys


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def min_distance(self, dist, spt):
        min, min_index = sys.maxsize, -1
        for i in range(self.V):
            if dist[i] < min and not spt[i]:
                min = dist[i]
                min_index = i
        return min_index

    def print_result(self, dist, src):
        for v in range(self.V):
            print(src, '-->', v, '==', dist[v])

    def dijkstra(self, src):
        dist = [sys.maxsize-1] * self.V
        dist[src] = 0
        spt = [False] * self.V

        for i in range(self.V):
            u = self.min_distance(dist, spt)
            spt[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and not spt[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.print_result(dist, src)


def main():
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    g.dijkstra(0)


if __name__ == '__main__':
    main()
