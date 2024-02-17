# https://leetcode.com/problems/search-a-2d-matrix/
# difficulty: medium
# topics: array, binary search, matrix

# problem:
# You are given an m x n integer matrix matrix with the following two properties:
#   Each row is sorted in non-decreasing order.
#   The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        lo, hi = 0, (rows*cols)-1
        while lo <= hi:
            mid = lo + ((hi-lo)//2)
            row, col = divmod(mid, cols)
            if matrix[row][col] == target: return True
            elif matrix[row][col] > target: hi = mid-1
            else: lo = mid+1
        return False
