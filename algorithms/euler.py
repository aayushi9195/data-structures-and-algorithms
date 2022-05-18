"""
Eulerian Path is a path in graph that visits every edge exactly once.
Eulerian Circuit is a Eulerian Path which starts and ends on the same vertex.
https://www.geeksforgeeks.org/eulerian-path-and-circuit/
Time complexity: O(V+E)

Additional resources:
https://www.geeksforgeeks.org/np-completeness-set-1/
https://www.geeksforgeeks.org/difference-between-np-hard-and-np-complete-problem/
https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/
https://www.geeksforgeeks.org/euler-circuit-directed-graph/
"""
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_util(self, v, visited):
        visited[v] = True
        for i in range(self.V):
            if not visited[i]:
                self.dfs_util(i, visited)

    def is_connected(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V

        #  Find a vertex with non-zero degree
        i = 0
        for i in range(self.V):
            if len(self.graph[i]) > 1:
                break

        # If there are no edges in the graph, return true
        if i == self.V - 1:
            return True

        # Start DFS traversal from a vertex with non-zero degree
        self.dfs_util(i, visited)

        # Check if all non-zero degree vertices are visited
        for i in range(self.V):
            if not visited[i] and len(self.graph[i]) > 0:
                return False

        return True

    def is_eulerian(self):
        if not self.is_connected():
            return 0
        else:
            odd = 0
            for i in range(self.V):
                if len(self.graph[i]) % 2 != 0:
                    odd += 1
            if odd == 0:
                return 2
            elif odd == 2:
                return 1
            elif odd > 2:
                return 0

    def test(self):
        result = self.is_eulerian()
        if result == 0:
            print("Graph is not Eulerian")
        elif result == 1:
            print("Graph has a Euler path")
        else:
            print("Graph has a Euler cycle")


def main():
    g1 = Graph(5)
    g1.add_edge(1, 0)
    g1.add_edge(0, 2)
    g1.add_edge(2, 1)
    g1.add_edge(0, 3)
    g1.add_edge(3, 4)
    g1.test()

    g2 = Graph(5)
    g2.add_edge(1, 0)
    g2.add_edge(0, 2)
    g2.add_edge(2, 1)
    g2.add_edge(0, 3)
    g2.add_edge(3, 4)
    g2.add_edge(4, 0)
    g2.test()

    g3 = Graph(5)
    g3.add_edge(1, 0)
    g3.add_edge(0, 2)
    g3.add_edge(2, 1)
    g3.add_edge(0, 3)
    g3.add_edge(3, 4)
    g3.add_edge(1, 3)
    g3.test()

    # Graph contains a cycle
    g4 = Graph(3)
    g4.add_edge(0, 1)
    g4.add_edge(1, 2)
    g4.add_edge(2, 0)
    g4.test()

    # Graph with all 0-degree vertices
    g5 = Graph(3)
    g5.test()


if __name__ == '__main__':
    main()
