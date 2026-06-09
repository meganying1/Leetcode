# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount
# difficulty: easy
# topics: array, greedy, sorting

# description: 
# A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.
# The customer can choose any candy to take away for free as long as the cost of the chosen candy is less than or equal to the minimum cost of the two candies bought.
#   For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3, they can take the candy with cost 1 for free, but not the candy with cost 4.
# Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the minimum cost of buying all the candies.

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n, ans = len(cost), 0
        cost.sort()
        for i in range(n):
            if i % 3 == 2: continue
            ans += cost[n-i-1]
        return ans
# time complexity: O(nlogn)
# space complexity: O(n)
