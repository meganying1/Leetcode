# https://leetcode.com/problems/jump-game/description/
# difficulty: medium
# topics: array, dynamic programming, greedy

# problem:
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n-1
        for i in range(n-2, -1, -1):
            if i + nums[i] >= target: target = i
        return True if target == 0 else False
# time complexity: O(n)
# space complexity: O(1)

"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        cache = [None] * n
        cache[-1] = True

        def dp(i):
            if cache[i] != None: return cache[i]
            for jump in range(1, nums[i]+1):
                if dp(i+jump):
                    cache[i] = True
                    return True
            cache[i] = False
            return False

        return dp(0)
"""
# time complexity: O(n)
# space complexity: O(n)
