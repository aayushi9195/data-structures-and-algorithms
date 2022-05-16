"""
The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem. The problem is to find shortest
distances between every pair of vertices in a given edge weighted directed Graph.

Time complexity: O(V^3)
"""
INF = 99999


class Graph:
    def __init__(self, vertices):
        self.V = vertices

    def floyd_warshall(self, graph):
        dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        print(dist)


def main():
    graph = Graph(4)
    g = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]]
    graph.floyd_warshall(g)


if __name__ == '__main__':
    main()