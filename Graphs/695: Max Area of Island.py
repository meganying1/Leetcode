# https://leetcode.com/problems/max-area-of-island/
# difficulty: medium
# topics: array, depth-first search, breadth-first search, union find, matrix

# problem:
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        ans = 0

        def dfs(i, j):
            if (i < 0) or (i == rows) or (j < 0) or (j == cols): return 0
            if (grid[i][j] == 0) or ((i, j) in seen): return 0
            ans = 1
            seen.add((i, j))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ans += dfs(i+dx, j+dy)
            return ans

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in seen and grid[i][j] == 1: ans = max(ans, dfs(i, j))
        return ans
# time complexity: O(n*m)
# space complexity: O(n*m)
