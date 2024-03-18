# https://leetcode.com/problems/coin-change-ii/description/
# difficulty: medium
# topics: array, dynamic programming

# problem:
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.
# The answer is guaranteed to fit into a signed 32-bit integer.

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        cache = {}
        
        def dp(remain, i):
            if remain == 0: return 1
            if i < 0 or remain < 0: return 0
            key = (remain, i)
            if key in cache: return cache[key]
            ans = dp(remain, i-1) + dp(remain-coins[i], i)
            cache[key] = ans
            return ans

        return dp(amount, n-1)
# top-down with memoization
# time complexity: O(len(coins) * amount)
# space complexity: O(len(coins) * amount)
