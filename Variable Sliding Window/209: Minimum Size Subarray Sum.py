# https://leetcode.com/problems/minimum-size-subarray-sum/
# topics: array, binary search, sliding window, prefix sum
# difficulty: medium

# problem:
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        ans = float('inf')
        n = len(nums)
        l = r = 0
        currSum = 0
        while r < n:
            currSum += nums[r]
            while currSum >= target:
                ans = min(ans, r-l+1)
                currSum -= nums[l]
                l += 1
            r += 1
        return ans
# time complexity: O(n)
# space complexity: O(1)
