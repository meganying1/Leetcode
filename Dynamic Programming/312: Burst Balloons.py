# https://leetcode.com/problems/burst-balloons/description/
# difficulty: hard
# topics: array, dynamic programming

# problem:
# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
# Return the maximum coins you can collect by bursting the balloons wisely.

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        balloons = [1] + nums + [1]
        cache = {}

        def dp(start, end):
            if start > end: return 0
            key = (start, end)
            if key in cache: return cache[key]
            ans = 0
            for i in range(start, end+1):
                coins = (balloons[start-1] * balloons[i] * balloons[end+1])
                coins += dp(start, i-1) + dp(i+1, end)
                ans = max(ans, coins)
            cache[key] = ans
            return ans

        return dp(1, n)
