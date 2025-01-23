# https://leetcode.com/problems/count-servers-that-communicate/
# difficulty: medium
# topics: array, depth-first search, breadth-first search, union find, matrix, counting

# problem:
# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
# Return the number of servers that communicate with any other server.

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        totalServers = ans = 0
        m, n = len(grid), len(grid[0])
        rowCounts, colCounts = defaultdict(int), defaultdict(int)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0: continue
                totalServers += 1
                rowCounts[r] += 1
                colCounts[c] += 1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0: continue
                if rowCounts[r] > 1 or colCounts[c] > 1: ans += 1
        return ans

# time complexity: O(m*n)
# space complexity: O(m+n)
