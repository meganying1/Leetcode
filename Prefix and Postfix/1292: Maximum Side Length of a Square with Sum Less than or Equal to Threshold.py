# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
# difficulty: medium
# topics: array, binary search, matrix, prefix sum

# description:
# Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n, m, ans = len(mat), len(mat[0]), 0
        prefix = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                prefix[i+1][j+1] = mat[i][j] + prefix[i+1][j]
        for j in range(m):
            for i in range(n):
                prefix[i+1][j+1] += prefix[i][j+1]

        def exists(val):
            for i in range(n-val+1):
                for j in range(m-val+1):
                    upperRight = prefix[i][j+val]
                    upperLeft = prefix[i][j]
                    lowerLeft = prefix[i+val][j]
                    lowerRight = prefix[i+val][j+val]
                    currSum = lowerRight - lowerLeft - upperRight + upperLeft
                    if currSum <= threshold: return True
            return False

        lo, hi = 0, min(n, m)
        while lo <= hi:
            mid = (lo + hi) // 2
            if exists(mid): 
                ans = mid
                lo = mid+1
            else: hi = mid-1
        return ans
# time complexity: O(n*m*log(min(n, m)))
#   precomputing prefixes takes O(n*m) time
#   conducting binary search takes O(n*m*log(min(n, m))) time
#     we check log(min(n, m)) values, and it takes n*m to check each value
# space complexity: O(n*m)
