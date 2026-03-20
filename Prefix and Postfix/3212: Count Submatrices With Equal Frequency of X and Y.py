# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/
# difficulty: medium
# topics: array, matrix, prefix sum

# description:
# Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:
#   grid[0][0]
#   an equal frequency of 'X' and 'Y'.
#   at least one 'X'.

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        prefixSum = [[0] * (m+1) for _ in range(n+1)]
        xCount = [[0] * (m+1) for _ in range(n+1)]
        ans = 0
        for i in range(n):
            for j in range(m):
                char = grid[i][j]
                if char == 'X':
                    prefixSum[i+1][j+1] += 1
                    xCount[i+1][j+1] += 1
                elif char == 'Y': prefixSum[i+1][j+1] -= 1
                prefixSum[i+1][j+1] += prefixSum[i][j+1] + prefixSum[i+1][j] - prefixSum[i][j]
                xCount[i+1][j+1] += xCount[i][j+1] + xCount[i+1][j] - xCount[i][j]
                if (prefixSum[i+1][j+1] == 0) and (xCount[i+1][j+1] > 0): ans += 1
        return ans
# time complexity: O(n*m)
# space complexity: O(n*m)
