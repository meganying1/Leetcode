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
# top-down with memoization
# time complexity: O(n^2)
# space complexity: O(n^2)
        
# we know for sure in a given subarray, one balloon must be the last one to be popped, so we can test all of them
# we can then break the problem down into new subarrays
#     if we have balloons 1 2 3 4 5 6 7 and balloon 5 is popped last, then balloons 1 2 3 4 and balloons 6 7 form two separate subarrays, they never “connect” since the 5 balloon gets popped last
