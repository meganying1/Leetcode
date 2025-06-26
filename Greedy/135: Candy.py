# https://leetcode.com/problems/candy/?envType=daily-question&envId=2025-06-25
# topics: array, greedy
# difficulty: hard

# problem:
# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
#   Each child must have at least one candy.
#   Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1: return 1
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i-1], candies[i] + 1)
        return sum(candies)
# time complexity: O(n)
# space complexity: O(n)
