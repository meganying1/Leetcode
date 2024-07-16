# https://leetcode.com/problems/clone-graph/
# difficulty: medium
# topics: hash table, depth-first search, breadth-first search, graph

# problem:
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
#   class Node {
#       public int val;
#       public List<Node> neighbors;
#   }


class Solution(object):
    def cloneGraph(self, node):
        if not node: return None
        nodeMap = dict()

        def cloneNode(n):
            newNode = Node(n.val, [])
            nodeMap[n.val] = newNode
            for neighbor in n.neighbors:
                if neighbor.val not in nodeMap:
                    cloneNode(neighbor)
                newNode.neighbors.append(nodeMap[neighbor.val])
        
        cloneNode(node)
        return nodeMap[1]
# time complexity: O(v+e)
#     we visit each vertex once and each edge twice
#     since the number of edges can be large, we say v+e
# space complexity: O(v)
#     we store v nodes in nodeMap
#     the dfs callstack depth is v
#     the space used by the nodes is e, but we don't include this in the space complexity since it's part of the solutio
