# 3 possible forms of graphs:
#  1. graph nodes:
#     class GraphNode:
#       def __init__(self, val):
#          self.val = val
#          self.neighbors = []
#  2. matrix:
#     [[1, 2, 5],
#     [3, 6, 4],
#     [8, 9, 7]]
#  3. edge list:
#     [[1, 2], [2, 3], [3, 1]]

# graphs can have various properties:
#  1. connected vs. unconnected:
#       if a graph is connected, every node in the graph can be reached by any other node
#       if a graph is unconnected, there are multiple discrete components
#  2. bi-directional vs. directed:
#       a bidirectional graph means every edge goes both ways
#       a directed graph implies a one-way relationship
#  3. weighted vs. unweighted:
#       a weighted graph means the edges have a certain cost or weight to traverse them
#       an unweighted graph means there is no cost

# complexity is represented in terms of v (# of vertices / nodes) and e (number of edges)
# matrix graphs have interesting property in which every node (except for edges) have 4 neighbors
#   each node has at max 4 edges, for a total of 4v edges, so all complexities can be expressed as function of v
# in a normal graph of n nodes, each node can have up to n-1 edges
#   in the worst case, a graph can have up to v^2 edges (this is known as a start graph)
#   we represent complexity in terms of v and e since e can be a lot larger than v

# graphs don't have that many types of solutions: mainly BFS / DFS based solutions
# more advance algorithms may include: topological sort, prim's algorithm, max flow, dijkstra's algorithm, etc.
