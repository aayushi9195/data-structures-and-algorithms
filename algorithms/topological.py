"""
A topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every
directed edge uv from vertex u to vertex v, u comes before v in the ordering.

https://www.geeksforgeeks.org/python-program-for-topological-sorting/
https://www.geeksforgeeks.org/topological-sorting/

Time Complexity: O(V+E), same as DFS with an extra stack.
Auxiliary space: O(V), extra space is needed for the stack.
"""
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_order(self):
        visited = [False] * self.V
        stack = []
        for u in range(self.V):
            if not visited[u]:
                self.util(visited, stack, u)
        print(stack[::-1])

    def util(self, visited, stack, u):
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                self.util(visited, stack, v)
        stack.append(u)


def main():
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.topological_order()


if __name__ == '__main__':
    main()