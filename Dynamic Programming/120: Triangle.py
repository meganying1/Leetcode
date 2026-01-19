# https://leetcode.com/problems/triangle/
# difficulty: medium
# topic: array, dynamic programming

# description:
# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[val for val in row] for row in triangle]
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]
# time complexity: O(n^2)
# space complexity: O(n^2)
