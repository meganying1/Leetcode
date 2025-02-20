# https://leetcode.com/problems/house-robber-ii/
# difficulty: medium
# topics: array, dynamic programming

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        def maxRob(arr):
            length = len(arr)
            if length <= 2: return max(arr)
            prev3, prev2, prev1 = 0, arr[0], arr[1]
            for i in range(3, length+1):
                temp = prev1
                prev1 = arr[i-1] + max(prev2, prev3)
                prev3 = prev2
                prev2 = temp
            return max(prev1, prev2)
            
        return max(maxRob(nums[:len(nums)-1]), maxRob(nums[1:]))
# time complexity: O(n)
# space complexty: O(1)
