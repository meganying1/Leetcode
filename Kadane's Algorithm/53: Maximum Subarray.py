# https://leetcode.com/problems/maximum-subarray/description/
# difficulty: medium
# topics: array, divide and conquer, dynamic programming

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, windowSum = nums[0], 0
        for n in nums:
            if windowSum < 0: windowSum = 0   
            windowSum += n
            ans = max(ans, windowSum)
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
