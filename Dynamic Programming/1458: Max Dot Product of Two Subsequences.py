# https://leetcode.com/problems/max-dot-product-of-two-subsequences/
# difficulty: hard
# topics: array, dynamic programming

# description:
# Given two arrays nums1 and nums2.
# Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.
# A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

# class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[-float("inf")] * m for _ in range(n)]
        dp[0][0] = nums1[0] * nums2[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], nums1[i] * nums2[0])
        for j in range(1, m):
            dp[0][j] = max(dp[0][j-1], nums1[0] * nums2[j])
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j-1] + nums1[i] * nums2[j], nums1[i]*nums2[j], dp[i-1][j], dp[i][j-1])
        return max(max(row) for row in dp)
# time complexity: O(n*m)
# space complexity: O(n*m)
