# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
# difficulty: hard
# topics: array, dynamic programming, depth-first search, breadth-first search, graph, topolgical sort, memoization, matrix

# program:
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.
# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cache = [[0 for j in range(n)] for i in range(m)]
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dp(row, col):
            if cache[row][col] != 0: return cache[row][col]
            ans = 1
            for move in moves:
                newRow, newCol = row+move[0], col+move[1]
                if (newRow >= 0 and newRow < m and newCol >= 0 and newCol < n and 
                matrix[newRow][newCol] > matrix[row][col]): ans = max(ans, 1+dp(newRow, newCol))
            cache[row][col] = ans
            return ans

        ans = 0
        for row in range(m):
            for col in range(n):
                ans = max(ans, dp(row, col))
        return ans
  # top-down with memoization
  # time complexity: O(n*m)
  # space complexity: O(n*m)
