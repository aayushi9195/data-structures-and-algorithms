"""
https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
Time: O(V+E)
Space: O(V)

https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
Time: O(V+E)
Space: O(V)
"""
from collections import defaultdict


class DirectedGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, rec_stack, visited):
        visited[v] = True
        rec_stack[v] = True
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.is_cyclic_util(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True
        rec_stack[v] = False
        return False

    def is_cyclic(self):
        visited = [False] * (self.V + 1)
        rec_stack = [False] * (self.V + 1)
        for node in range(self.V):
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False


class UndirectedGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                if self.is_cyclic_util(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False

    def is_cyclic(self):
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                if self.is_cyclic_util(i, visited, -1):
                    return True
        return False


def main():
    g = DirectedGraph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)  # Cycle
    g.add_edge(2, 3)
    g.add_edge(3, 3)  # Cycle
    if g.is_cyclic() == 1:
        print("Directed graph has a cycle")
    else:
        print("Directed graph has no cycle")

    g = DirectedGraph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    if g.is_cyclic() == 1:
        print("Directed graph has a cycle")
    else:
        print("Directed graph has no cycle")

    g = UndirectedGraph(5)
    g.add_edge(1, 0)
    g.add_edge(1, 2)
    g.add_edge(2, 0)  # Cycle
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    if g.is_cyclic():
        print("Undirected graph has a cycle")
    else:
        print("Undirected graph has no cycle ")

    g = UndirectedGraph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    if g.is_cyclic():
        print("Undirected graph has a cycle")
    else:
        print("Undirected graph has no cycle ")


if __name__ == '__main__':
    main()