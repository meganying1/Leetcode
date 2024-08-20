# https://leetcode.com/problems/maximum-number-of-points-with-cost
# difficulty: medium
# topics: array, dynamic programming, matrix

# problem:
# You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.
# To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.
# However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.
# Return the maximum number of points you can achieve.

class Solution(object):
    def maxPoints(self, points):
        rows, cols = len(points), len(points[0])
        if rows == 1: return max(points[0])
        prevRow = [points[0][i] for i in range(cols)]
        for row in range(1, rows):
            currRow = [0] * cols
            leftMax = [0] * cols
            rightMax = [0] * cols
            leftMax[0], rightMax[-1] = prevRow[0], prevRow[-1]
            for col in range(1, cols): leftMax[col] = max(leftMax[col-1]-1, prevRow[col])
            for col in range(cols-2, -1, -1): rightMax[col] = max(rightMax[col+1]-1, prevRow[col])
            for col in range(cols):
                currRow[col] = points[row][col] + max(leftMax[col], rightMax[col])
            prevRow = currRow
        return max(currRow)
# time complexity: O(m * n)
# space complexity: O(n)
# can further improve space complexity by eliminating use of auxiliary arrays

"""
class Solution(object):
    def maxPoints(self, points):
        rows, cols = len(points), len(points[0])
        if rows == 1: return max(points[0])
        prevRow = [points[0][i] for i in range(cols)]
        for row in range(1, rows):
            currRow = [0] * cols
            for currCol in range(cols):
                for prevCol in range(cols):
                   currRow[currCol] = max(currRow[currCol], prevRow[prevCol]+points[row][currCol]-abs(currCol-prevCol))
            prevRow = currRow
        return max(currRow)
"""
# time complexity: O(m * n**2), where m is number of rows and n in number of cols
# space complexity: O(n)
# due to constraint that m * n <= 10**5, we know max time complexity must be O(m*n)
#   need to optimize how we move from one row to the next
# instead of recalculating the possible scores from every cell in prevRow for each cell in currRow, we can use two auxiliary arrays to store the maximum possible contributions from the left and right
#   we can compare these two precomputed values to determine the best score for each cell in currRow
