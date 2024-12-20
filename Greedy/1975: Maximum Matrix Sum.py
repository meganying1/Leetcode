# https://leetcode.com/problems/maximum-matrix-sum/description/
# difficulty: medium
# topics: array, greedy, matrix

# problem:
# You are given an n x n integer matrix. You can do the following operation any number of times:
#   Choose any two adjacent elements of matrix and multiply each of them by -1.
#   Two elements are considered adjacent if and only if they share a border.
# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        zeroClosest = float("inf")
        negCount = 0
        ans = 0
        for row in matrix:
            for elem in row:
                ans += abs(elem)
                if elem < 0: negCount += 1
                zeroClosest = min(zeroClosest, abs(elem))
        if negCount % 2 == 0: return ans
        return ans - 2*abs(zeroClosest)
# idea: we can convert all values to positive if we have an even number of negative values
#   iterate through all elements and add absolute value to sum
#   count the number of negative numbers
#   keep track of value closest to zero
#   if final negative count is even, return sum; otherwise, subtract two times value closest to zero and return sum
# time complexity: O(n*m)
# space complexity: O(1)
