# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
# difficulty: medium
# topics: array, design, matrix, prefix sum

# problem:
# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:
#   NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
#   int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
#You must design an algorithm where sumRegion works on O(1) time complexity.

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = [[val for val in row] for row in matrix]
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(1, cols):
                self.matrix[i][j] += self.matrix[i][j-1]
        for i in range(1, rows):
            for j in range(cols):
                self.matrix[i][j] += self.matrix[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        upperRight = self.matrix[row1-1][col2] if row1 != 0 else 0
        lowerLeft = self.matrix[row2][col1-1] if col1 != 0 else 0
        upperLeft = self.matrix[row1-1][col1-1] if (row1 != 0 and col1 != 0) else 0
        return self.matrix[row2][col2] - upperRight - lowerLeft + upperLeft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
