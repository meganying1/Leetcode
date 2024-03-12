# https://leetcode.com/problems/longest-increasing-subsequence/description/
# difficulty: medium
# topics: array, binary search, dynamic programming

# problem:
# Given an integer array nums, return the length of the longest strictly increasing subsequence.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length
        for i in range(1, length):
            greatest = 0
            for j in range(i):
                if nums[i] > nums[j]: greatest = max(greatest, dp[j])
            dp[i] += greatest
        return max(dp)
