# https://leetcode.com/problems/partition-equal-subset-sum/
# topics: array, dynamic programming
# difficulty: medium

# problem:
# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total, n = sum(nums), len(nums)
        if total % 2 == 1: return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for n in nums:
            for possSum in range(target, n-1, -1):
                dp[possSum] = dp[possSum] or dp[possSum - n]
        return dp[-1]
# time complexity: O(n * k), where k = sum(nums) / 2
# space complexity: O(k)

"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total, n = sum(nums), len(nums)
        if total % 2 == 1: return False
        cache = {}

        def containsSubSum(i, subsetSum):
            if subsetSum == 0: return True
            if i == n: return False
            if (i, subsetSum) in cache: return cache[(i, subsetSum)]
            ans = containsSubSum(i+1, subsetSum) or containsSubSum(i+1, subsetSum - nums[i])
            cache[(i, subsetSum)] = ans
            return ans
        
        return containsSubSum(0, total // 2)
"""
# time complexity: O(n * k), where k = sum(nums) / 2
# space complexity: O(n * k)
