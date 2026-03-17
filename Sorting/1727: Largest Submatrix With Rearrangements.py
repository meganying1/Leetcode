# https://leetcode.com/problems/largest-submatrix-with-rearrangements
# difficulty: medium
# topics: array, greedy, sorting, matrix

# description:
# You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.
# Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        consecutive = [[0] * m for _ in range(n)]
        ans = 0
        for col in range(m):
            if matrix[0][col] == 1: consecutive[0][col] = 1
        for row in range(n):
            for col in range(m):
                if row > 0 and matrix[row][col] == 1: consecutive[row][col] = consecutive[row-1][col] + 1
            currRow = sorted(consecutive[row], reverse=True)
            for col in range(m):
                area = currRow[col] * (col + 1)
                ans = max(ans, area)
        return ans
# time complexity: O(n*m*logn)
# space complexity: O(n*m)
