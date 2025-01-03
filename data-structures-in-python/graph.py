"""
Two ways of representation:
Adjacency list
Adjacency matrix
https://www.baeldung.com/cs/graphs

BFS - O(V+E) time, O(V) auxiliary space
DFS - O(V+E) time, O(V) auxiliary space
"""

from collections import deque, defaultdict


class AdjacencyListWeightedGraph:
    def __init__(self):
        self.graph = {}  # or DefaultDict

    def addVertex(self, v):
        self.graph[v] = []

    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])

    def print(self):
        for vertex in self.graph:
            for edges in self.graph[vertex]:
                print(vertex, " -> ", edges[0], " edge weight: ", edges[1])


class AdjacencyMatrixWeightedGraph:
    def __init__(self, v):
        self.graph = [[0 for x in range(v+1)] for y in range(v+1)]
        self.n = v

    def addEdge(self, u, v, w):
        self.graph[u][v] = w

    def print(self):
        for source in range(1, self.n+1):
            for destination in range(1, self.n+1):
                print(source, " -> ", destination, " edge weight: ", self.graph[source][destination])


class UnweightedGraph:
    def __init__(self, v):
        self.graph = defaultdict(list)

    def addVertex(self, v):
        self.graph[v] = []

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def print(self):
        for vertex in self.graph:
            print(vertex, " -> ", self.graph[vertex])

    def bfs_iterative(self, source):
        visited = set()
        queue = deque()
        queue.append(source)
        visited.add(source)
        ans = []
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            for neighbor in self.graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print('BFS iterative:', ans)

    def dfs_recursive(self, source):
        visited = set()
        ans = []
        self.dfs_util(source, visited, ans)
        print('DFS recursive:', ans)

    def dfs_util(self, source, visited, ans):
        visited.add(source)
        ans.append(source)
        for neighbor in self.graph[source]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited, ans)

    def bfs_recursive(self, source):
        queue = deque()
        queue.append(source)
        visited = set()
        visited.add(source)
        ans = []
        self.bfs_util(queue, visited, ans)
        print('BFS recursive:', ans)

    def bfs_util(self, queue, visited, ans):
        if not queue:
            return
        curr = queue.popleft()
        ans.append(curr)
        for neighbor in self.graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        self.bfs_util(queue, visited, ans)

    def dfs_iterative(self, source):
        visited = set()
        stack = deque()
        stack.append(source)
        ans = []
        while stack:
            curr = stack.pop()
            if curr not in visited:
                ans.append(curr)
                visited.add(curr)
            for node in self.graph[curr]:
                if node not in visited:
                    stack.append(node)
        print('DFS iterative:', ans)


def main():
    graph = AdjacencyListWeightedGraph()
    graph.addVertex(1)
    graph.addVertex(2)
    graph.addVertex(3)
    graph.addVertex(4)
    graph.addEdge(1, 2, 1)
    graph.addEdge(1, 3, 1)
    graph.addEdge(2, 3, 3)
    graph.addEdge(3, 4, 4)
    graph.addEdge(4, 1, 5)
    graph.print()

    graph = AdjacencyMatrixWeightedGraph(4)
    graph.addEdge(1, 2, 1)
    graph.addEdge(1, 3, 1)
    graph.addEdge(2, 3, 3)
    graph.addEdge(3, 4, 4)
    graph.addEdge(4, 1, 5)
    graph.print()

    graph = UnweightedGraph(5)
    graph.addVertex(1)
    graph.addVertex(2)
    graph.addVertex(3)
    graph.addVertex(4)
    graph.addVertex(5)
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.addEdge(4, 1)
    graph.addEdge(2, 5)
    graph.print()

    graph.bfs_iterative(2)
    graph.bfs_recursive(2)
    graph.dfs_iterative(2)
    graph.dfs_recursive(2)


if __name__ == "__main__":
    main()
