# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# topics: array, dynamic programming
# difficulty: medium

# problem:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = {}
        
        def dp(i, holding):
            if i >= n: return 0
            if (i, holding) in cache: return cache[(i, holding)]
            if holding:
                ans = max(dp(i+2, False)+prices[i], dp(i+1, True))
            else:
                ans = max(dp(i+1, False), dp(i+1, True)-prices[i])
            cache[(i, holding)] = ans
            return ans
        
        return max(dp(0, True)-prices[0], dp(0, False))
# time complexity: O(n)
# space complexity: O(n)
