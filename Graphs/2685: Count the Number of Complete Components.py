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
        
        def dfs(node, num, e, v):
            seen[node] = True
            v += 1
            for neighbor in neighborMap[node]:
                e += 1
                if not seen[neighbor]: e, v = dfs(neighbor, num, e, v)
            return e, v
        
        ans = num = 0
        for i in range(n):
            if seen[i]: continue
            e, v = dfs(i, num, 0, 0)
            e //= 2
            num += 1
            if v*(v-1)//2 == e: ans += 1
        return ans
