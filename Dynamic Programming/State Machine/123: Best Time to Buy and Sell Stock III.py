# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
# difficulty: hard
# topics: array, dynamic programming

# problem:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        notHolding1 = notHolding2 = 0
        holding1 = holding2 = -float("inf")
        for price in prices:
            holding2, notHolding2 = max(holding2, notHolding1-price), max(notHolding2, holding2+price)
            holding1, notHolding1 = max(holding1, -price), max(notHolding1, holding1+price)
        return notHolding2
# time complexity: O(n)
# space complexity: O(1)
