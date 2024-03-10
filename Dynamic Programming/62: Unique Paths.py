# https://leetcode.com/problems/unique-paths/description/
# difficulty: medium
# topics: math, dynamic programming, combinatorics

# problem:
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 109.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n < m:
            prevRow = [1] * n
            for row in range(1, m):
                prevCol = 1
                for col in range(1, n):
                    prevRow[col] += prevCol
                    prevCol = prevRow[col]
            return prevRow[-1]
        else:
            prevCol = [1] * m
            for col in range (1, n):
                prevRow = 1
                for row in range(1, m):
                    prevCol[row] += prevRow
                    prevRow = prevCol[row]
            return prevCol[-1]
# space optimized bottom-up
# time complexity: O(n*m)
# space complexity: O(min(m, n))

"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [1] * n
        for row in range(1, m):
            prevCol = 1
            for col in range(1, n):
                prevRow[col] += prevCol
                prevCol = prevRow[col]
        return prevRow[-1]
"""
# space optimized bottom-up
# time complexity: O(n*m)
# space complexity: O(n)
#     can do even better by choosing to iterate in direction which allows cache to be smaller

"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] * m
        for col in range(n): dp[0][col] = 1
        for row in range(m): dp[row][0] = 1
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[m-1][n-1]
"""
# bottom-up
# time complexity: O(n*m)
# space complexity: O(n*m)
