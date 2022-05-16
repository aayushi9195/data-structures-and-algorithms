"""
Given a graph and a source vertex src in graph, find shortest paths from src to all vertices in the given graph.
Dijkstra’s algorithm is a Greedy algorithm and time complexity is O((V+E)LogV) (with the use of Fibonacci heap).
Dijkstra doesn’t work for Graphs with negative weights, Bellman-Ford works for such graphs. Bellman-Ford is also simpler
than Dijkstra and suites well for distributed systems. But time complexity of Bellman-Ford is O(VE), which is more than
Dijkstra.
"""