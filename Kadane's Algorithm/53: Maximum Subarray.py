# https://leetcode.com/problems/maximum-subarray/description/
# difficulty: medium
# topics: array, divide and conquer, dynamic programming

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = end = 0
        ans, windowSum = -float("inf"), 0
        while end < len(nums):
            windowSum += nums[end]
            ans = max(ans, windowSum)
            if windowSum < 0:
                start = end + 1
                windowSum = 0
            end += 1
        return ans

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = nums[0], nums[0]
        for i in range(1, len(nums)):
            currSum = max(nums[i], currSum + nums[i])
            maxSum = max(maxSum, currSum)
        return maxSum
"""
