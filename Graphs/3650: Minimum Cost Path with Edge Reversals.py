# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/
# difficulty: medium
# topics: graph theory, heap (priority queue), shortest path

# description:
# You are given a directed, weighted graph with n nodes labeled from 0 to n - 1, and an array edges where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with cost wi.
# Each node ui has a switch that can be used at most once: when you arrive at ui and have not yet used its switch, you may activate it on one of its incoming edges vi → ui reverse that edge to ui → vi and immediately traverse it.
# The reversal is only valid for that single move, and using a reversed edge costs 2 * wi.
# Return the minimum total cost to travel from node 0 to node n - 1. If it is not possible, return -1.

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graphDict = defaultdict(list)
        for u, v, w in edges:
            graphDict[u].append((v, w))
            graphDict[v].append((u, w*2))
        dist = [float("inf")] * n
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            currDist, currNode = heapq.heappop(pq)
            if currDist > dist[currNode]: continue
            for v, w in graphDict[currNode]:
                vDist = currDist + w
                if vDist < dist[v]:
                    dist[v] = vDist
                    heapq.heappush(pq, (vDist, v))
        return dist[-1] if dist[-1] != float("inf") else -1
# time complexity: O((v+e)logv), where v is number of nodes and e is number of edges
#   it takes O(e) time to build the graph since we loop over every edge
#   it takes O(v) time build the dist array
#   main dijkstra's algorithm takes O((v+e)logv) time
#     each heap pop or push takes O(logv) time
#     each vertex is processed once and each edge may require a priority queue update
# space complexity: O(v + e)
