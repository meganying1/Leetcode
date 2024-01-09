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
        start, end = 0, length-k-1
        currSum = sum(cardPoints[:end])
        total, minSum = currSum, currSum
        while end < length-1:
            start += 1
            end += 1
            total += cardPoints[end]
            currSum += cardPoints[end] - cardPoints[start-1]
            minSum = min(minSum, currSum)
        return total - minSum
