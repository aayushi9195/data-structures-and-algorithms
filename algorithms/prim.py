"""
Prim's algorithm (also known as Jarník's algorithm) is a greedy algorithm that finds a minimum spanning tree for a
weighted undirected graph. This means it finds a subset of the edges that forms a tree that includes every vertex,
where the total weight of all the edges in the tree is minimized.

https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/

Time complexity:
O(V*V) for adjacency matrix
O(E*logV) for adjacency list + heap
"""
import sys


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def extract_min(self, key, mst):
        min, min_index = sys.maxsize, -1
        for v in range(self.V):
            if key[v] < min and not mst[v]:
                min = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        # Array to store constructed MST
        parent = [None] * self.V
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mst = [False] * self.V
        # 0 is the root so it has no parent
        parent[0] = -1

        for i in range(self.V):
            u = self.extract_min(key, mst)
            mst[u] = True

            for v in range(self.V):
                if 0 < self.graph[u][v] < key[v] and not mst[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)


def main():
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]
    g.prim_mst()

    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0, 0],
               [0, 0, 8, 0, 0, 0, 0, 11, 0, 0],
               [0, 0, 0, 7, 0, 4, 0, 0, 2, 0],
               [0, 0, 0, 0, 9, 14, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 10, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 6, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 7, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    g.prim_mst()


if __name__ == '__main__':
    main()
