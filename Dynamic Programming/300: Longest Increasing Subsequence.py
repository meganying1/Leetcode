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
# bottom-up
# time complexity: O(n^2)
# space complexity: O(n)

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        cache = {}
        
        def dp(i, prevHighest):
            if i == length: return 0
            if (i, prevHighest) in cache != None: cache[(i, prevHighest)]
            if nums[i] <= prevHighest: 
                ans = dp(i+1, prevHighest)
                cache[(i, prevHighest)] = ans
                return ans
            ans = max(dp(i+1, nums[i])+1, dp(i+1, prevHighest))
            cache[(i, prevHighest)] = ans
            return ans
        
        return dp(0, -float("inf"))
"""
# top-down with memoization (just for practice)
# time complexity: O(n^2)
#     input parameters to dp function represent state space, so our state space is a function of i and prevHighest
#     we have n*n states
# space complexity: O(n^2)

# can't define cache using just index i because there are different scenarios for the same index
#     in practice, cache needs to line up with parameters to dp function
