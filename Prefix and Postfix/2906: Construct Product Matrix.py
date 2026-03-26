# https://leetcode.com/problems/construct-product-matrix/
# difficulty: medium
# topics: array, matrix, prefix sum

# description:
# Given a 0-indexed 2D integer matrix grid of size n * m, we define a 0-indexed 2D matrix p of size n * m as the product matrix of grid if the following condition is met:
#   Each element p[i][j] is calculated as the product of all elements in grid except for the element grid[i][j]. This product is then taken modulo 12345.
# Return the product matrix of grid.

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        p = [[0] * m for _ in range(n)]
        prefix, suffix = 1, 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                p[i][j] = suffix
                suffix = (suffix * grid[i][j]) % 12345
        for i in range(n):
            for j in range(m):
                p[i][j] = (p[i][j] * prefix) % 12345
                prefix = (prefix * grid[i][j]) % 12345
        return p
# time complexity: O(n * m)
# space complexity: O(n * m)

"""
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        prefix = [[1] * m for _ in range(n)]
        suffix = [[1] * m for _ in range(n)]
        p = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i > 0 and j == 0:
                    prefix[i][j] = (prefix[i-1][m-1] * grid[i-1][m-1]) % 12345
                    suffix[n-i-1][m-j-1] = (suffix[n-i][0] * grid[n-i][0]) % 12345
                elif j > 0:
                    prefix[i][j] *= (prefix[i][j-1] * grid[i][j-1]) % 12345
                    suffix[n-i-1][m-j-1] *= (suffix[n-i-1][m-j] * grid[n-i-1][m-j]) % 12345
        for i in range(n):
            for j in range(m):
                p[i][j] = (prefix[i][j] * suffix[i][j]) % 12345
        return p
"""
# we don't need to store prefix and suffix values in a matrix

# time complexity: O(n * m)
# space complexity: O(n * m)
