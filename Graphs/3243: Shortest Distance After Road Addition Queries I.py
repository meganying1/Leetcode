# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/
# difficulty: medium
# topics: array, breadth-first search, graph

# problem:
# You are given an integer n and a 2D integer array queries.
# There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.
# queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.
# Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.

from collections import deque

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        def bfs():
            visited = [False] * n
            queue = deque()
            queue.append(0)
            visited[0] = True
            layers = 0
            while queue:
                layerLen = len(queue)
                for _ in range(layerLen):
                    curr = queue.popleft()
                    if curr == n-1: return layers
                    for neighbor in graph[curr]:
                        if not visited[neighbor]:
                            queue.append(neighbor)
                            visited[neighbor] = True
                layers += 1
        
        ans = []
        graph = [[] for _ in range(n)]
        for i in range(n-1): graph[i].append(i+1)
        for u, v in queries:
            graph[u].append(v)
            ans.append(bfs())
        return ans
# time complexity: O(q*(n+q)), where q represents number of queries
#   bfs contains 3 loops but takes O(n + e) time
#   first inner for loop runs a total of n times, because it processes all n nodes
#   second inner for loop runs a total of e times, because it processes all e edges
#   outer while loop does not affect total time complexity
#   each bfs after adding a new road increments edge count, so total time complexity of all q queries is O(q*(n+q))
#     after first road: O(n+n), after second road: O(n+n+1), ..., after qth road: O(n+n+q-1)
#     sum is O(qn+q(q-1)/2) = O(qn + q^2) = O(q*(n+q))
# space complexity: O(n+q)
#   graph array takes O(n+q) space
#     initially, array has n-1 elements
#     after processing all queries, array has n+q-1 elements
# visited array and queue take O(n) space
