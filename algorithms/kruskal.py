"""
Kruskal's algorithm finds a minimum spanning forest of an undirected edge-weighted graph. If the graph is connected,
it finds a minimum spanning tree. It is a greedy algorithm in graph theory as in each step it adds the next
lowest-weight edge that will not form a cycle to the minimum spanning forest.

Time complexity:
Sorting of edges takes O(ELogE) time. After sorting, we iterate through all edges and apply the find-union algorithm.
The find and union operations can take at most O(LogV) time. So overall complexity is O(ELogE + ELogV) time.
The value of E can be at most O(V2), so O(LogV) is O(LogE) the same.
Therefore, the overall time complexity is O(ELogE) or O(ELogV).

https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/
"""


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y (uses union by rank)
    def union(self, parent, rank, u, v):
        u_root = self.find(parent, u)
        v_root = self.find(parent, v)
        if rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        elif rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        else:
            parent[v_root] = u_root
            rank[u_root] += 1

    def print_mst(self, result):
        min_cost = 0
        for u, v, w in result:
            min_cost += w
            print(u, '-->', v, '==', w)
        print('MST cost:', min_cost)

    def kruskal_mst(self):
        result, parent, rank = [], [], []
        e = 0
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        self.graph = sorted(self.graph, key=lambda x: x[2])
        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
            u, v, w = self.graph.pop(0)
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                self.union(parent, rank, u, v)
                result.append([u, v, w])
                e += 1
        self.print_mst(result)


def main():
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
    g.kruskal_mst()


if __name__ == '__main__':
    main()

