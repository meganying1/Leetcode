# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/
# difficulty: easy
# topics: array, math, matrix, simulation

# description:
# You are given an m x n integer matrix mat and an integer k. The matrix rows are 0-indexed.
# The following proccess happens k times:
#   Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.
#   Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.
# Return true if the final modified matrix after k steps is identical to the original matrix, and false otherwise.

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k %= n
        for i in range(m):
            for j in range(n):
                if i % 2 == 0: newVal = (j + k) % n
                else: newVal = (j - k) % n
                if mat[i][newVal] != mat[i][j]: return False
        return True
# time complexity: O(n * m)
# space complexity: O(1)
