# https://leetcode.com/problems/number-of-islands/
# difficulty: medium
# topics: array, depth-first search, depth-first search, union find, matrix

# problem:
#   Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#   An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

class Solution(object):
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        seen = set()
        ans = 0

        def dfs(i, j):
            if (i < 0) or (i == rows) or (j < 0) or (j == cols): return
            if (grid[i][j] == "0") or ((i, j) in seen): return
            seen.add((i, j))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(i+dx, j+dy)

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in seen and grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        return ans
# time complexity: O(n*m)
# space complexity: O(n*m)
# using a set for seen values is more efficient here because we may not need to store information about all cells in the matrix
# using an array would be more efficient if all of the cells are equal to "1" since arrays are more performant than hashmaps
