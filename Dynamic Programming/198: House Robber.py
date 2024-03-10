# https://leetcode.com/problems/house-robber/description/
# difficulty: medium
# topics: array, dynamic programming

# problem:
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 2: return max(nums)
        prev3, prev2, prev1 = 0, nums[0], nums[1]
        for i in range(3, length+1):
            temp = prev1
            prev1 = nums[i-1] + max(prev2, prev3)
            prev3 = prev2
            prev2 = temp
        return max(prev1, prev2)
# space optimized bottom-up
# time complexity: O(n)
# space complexity: O(1)

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 2: return max(nums)
        dp = [0] * (length+1)
        dp[1], dp[2] = nums[0], nums[1]
        for i in range(3, length+1):
            dp[i] = nums[i-1] + max(dp[i-2], dp[i-3])
        return max(dp[-1], dp[-2])
"""
# bottom-up
# time complexity: O(n)
# space complexity: O(n)
