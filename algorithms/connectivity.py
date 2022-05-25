"""
https://www.tutorialspoint.com/Connectivity-in-a-directed-graph
Time: O(V+E)
"""
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_connected_util(self, u, visited):
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                self.is_connected_util(v, visited)

    def is_connected(self):
        visited = [False] * self.V
        components = 0
        for i in range(self.V):
            if not visited[i]:
                self.is_connected_util(i, visited)
                components += 1
        if components > 1:
            return False
        return True


def main():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    if g.is_connected():
        print("The graph is connected")
    else:
        print("The graph is not connected")

    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(4, 5)
    if g.is_connected():
        print("The graph is connected")
    else:
        print("The graph is not connected")


if __name__ == '__main__':
    main()