# https://leetcode.com/problems/coin-change/description/
# difficulty: medium
# topics: array, dynamic programming, breadth-first search

# problem:
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minVal = min(coins)
        cache = {coin:1 for coin in coins}
        def dp(n):
            if n == 0: return 0
            if n in cache: return cache[n]
            res = float('inf')
            for val in coins:
                if val > n: continue
                res = min(res, dp(n-val)+1)
            cache[n] = res
            return res
        ans = dp(amount)
        return ans if ans != float('inf') else -1
# time complexity: O(amount * len(coins))
# space complexity: O(amount)
