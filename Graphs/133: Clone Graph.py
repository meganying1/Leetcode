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
