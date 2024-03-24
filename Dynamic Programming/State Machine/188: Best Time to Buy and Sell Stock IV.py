# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# difficulty: hard
# topics: array, dynamic programming

# problem:
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        cache = {}

        def dp(holding, actions, day):
            if day == n-1 or actions == k:
                if holding: return prices[day]
                else: return 0
            key = (holding, actions, day)
            if key in cache: return cache[key]
            if holding: ans = max(dp(True, actions, day+1), dp(False, actions+1, day+1)+prices[day])
            else: ans = max(dp(True, actions, day+1)-prices[day], dp(False, actions, day+1))
            cache[key] = ans
            return ans

        return max(dp(True, 0, 0)-prices[0], dp(False, 0, 0))
"""
# unoptimized space version
# time complexity: O(n*k)
# space complexity: O(n*k)
