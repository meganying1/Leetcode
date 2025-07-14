# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/
# topics: array, graph, heap (priority queue), matrix, shortest path
# difficulty: medium

# problem:
# There is a dungeon with n x m rooms arranged as a grid.
# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.
# Return the minimum time to reach the room (n - 1, m - 1).
# Two rooms are adjacent if they share a common wall, either horizontally or vertically.

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        heap = [(0, 0, 0, 0)]
        visited = [[False for _ in range(m)] for _ in range(n)]
        visited[0][0] = True
        while heap:
            currTime, r, c, steps = heapq.heappop(heap)
            if r == n-1 and c == m-1: return currTime
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newR, newC = r+dr, c+dc
                if newR < 0 or newR >= n or newC < 0 or newC >= m or visited[newR][newC]: continue
                visited[newR][newC] = True
                newTime = max(currTime, moveTime[newR][newC]) + (steps % 2) + 1
                heapq.heappush(heap, (newTime, newR, newC, steps + 1))
        return time[-1][-1]
# time complexity: O(n*m*log(n*m))
#   there are n*m vertices
#   we implement dijkstra's algorithm, performing at most n*m insertions and deletions
#   each heap operation takes O(log(n*m)) time
# space complexity: O(n*m)

# dijkstra's algorithm: used to find shortest distance from a given source node to all other nodes in the graph
# we initialize distance of source node to 0 since it is the starting point, and all other distances as infinity
# we then iterate through all unvisited nodes; for each unvisited node u, we update its distance to its neighbors v using the formula: dist[v] = dist[u] + weight[u][v] if the new path is a shorter distance than the current known one
