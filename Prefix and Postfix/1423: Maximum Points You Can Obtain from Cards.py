# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
# difficulty: medium
# topics: array, sliding window, prefix sum

# problem:
# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints)
        for i in range(1, length): cardPoints[i] += cardPoints[i-1]
        start, end = 0, length-k-1
        minSum = cardPoints[end]
        while end < length-1:
            start += 1
            end += 1
            minSum = min(minSum, cardPoints[end]-cardPoints[start-1])
        return cardPoints[-1] - minSum
