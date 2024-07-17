# https://leetcode.com/problems/count-the-number-of-complete-components/
# difficulty: medium
# topics: depth-first search, breadth-first search, graph

# problem:
# You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.
# Return the number of complete connected components of the graph.
# A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
# A connected component is said to be complete if there exists an edge between every pair of its vertices.

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        neighborMap = defaultdict(list)
        seen = [False for _ in range(n)]
        for node1, node2 in edges:
            neighborMap[node1].append(node2)
            neighborMap[node2].append(node1)
        
        def dfs(node, compNodes):
            seen[node] = True
            compNodes.append(node)
            for neighbor in neighborMap[node]:
                if not seen[neighbor]: v = dfs(neighbor, compNodes)
            return compNodes
        
        ans = 0
        for i in range(n):
            if seen[i]: continue
            compNodes = dfs(i, [])
            compSize = len(compNodes)
            if all(len(neighborMap[node]) == compSize-1 for node in compNodes): ans += 1
        return ans
# time complexity: O(v+e)
# space complexity: O(v+e)
#     space complexity will probably never be O(e) for any problem
#     neighborMap is always O(v) space for the keys, since each node is a key, and O(e) space for the values, as we store every edge in a neighbor array
#     callstack depth on dfs is usually O(v) too

"""
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        neighborMap = defaultdict(list)
        seen = [False for _ in range(n)]
        for node1, node2 in edges:
            neighborMap[node1].append(node2)
            neighborMap[node2].append(node1)
        
        def dfs(node, e, v):
            seen[node] = True
            v += 1
            for neighbor in neighborMap[node]:
                e += 1
                if not seen[neighbor]: e, v = dfs(neighbor, e, v)
            return e, v
        
        ans = 0
        for i in range(n):
            if seen[i]: continue
            e, v = dfs(i, 0, 0)
            e //= 2
            if v*(v-1)//2 == e: ans += 1
        return ans
"""
# common pattern is to pass in a set or array as a parameter of dfs to accumulate or keep track of things
# we don't need to deal with edges in the dfs function
# we know that if a component has k nodes, each node in that component needs to have exactly k-1 edges for that component to be perfect
# we know how many edges each node has from neighborMap
