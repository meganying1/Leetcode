# https://leetcode.com/problems/greatest-sum-divisible-by-three/
# difficulty: medium
# topics: array, dynamic programming, sorting, greedy

# description:
# Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        prev = [0, -float('inf'), -float('inf')]
        for n in nums:
            curr = prev[:]
            for i in range(3):
                curr[(i + n) % 3] = max(curr[(i + n) % 3], prev[i] + n)
            prev = curr
        return curr[0]
# time complexity: O(n)
# space complexity: O(1)

"""
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][nums[0] % 3] = nums[0]
        for i in range(1, n):
            for mod in range(3):
                addSum = dp[i-1][mod] + nums[i]
                dp[i][addSum % 3] = max(dp[i][addSum % 3], addSum)
                dp[i][mod] = max(dp[i][mod], dp[i-1][mod])
        return dp[-1][0]
"""
# time complexity: O(n)
# space complexity: O(n)
