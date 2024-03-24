# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# difficulty: medium
# topics: array, dynamic programming

# problem:
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holding, notHolding = -float("inf"), 0
        for price in prices:
            holding, notHolding = max(holding, notHolding-price), max(notHolding, holding+price)
        return notHolding
# "state machine" solution
#     we are either in a state of holding a stock or not holding a stock
# time complexity: O(n)
# space complexity: O(1)

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = {}

        def dp(holding, day):
            if day == n-1:
                if holding: return prices[day]
                else: return 0
            key = (holding, day)
            if key in cache: return cache[key]
            if holding:
                ans = max(dp(True, day+1), dp(False, day+1)+prices[day])
            else:
                ans = max(dp(True, day+1)-prices[day], dp(False, day+1))
            cache[key] = ans
            return ans
        
        return max(dp(True, 0)-prices[0], dp(False, 0))
"""
# using "normal" bottom-up dynamic programming solution
# time complexity: O(n)
# space complexity: O(n)
