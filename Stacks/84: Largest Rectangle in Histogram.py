# https://leetcode.com/problems/largest-rectangle-in-histogram/
# difficulty: hard
# topics: array, stack, monotonic stack

# problem:
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        nextSmallerDict, prevSmallerDict = {}, {}
        ans = 0
        for i in range(n):
            while stack and stack[-1][0] > heights[i]:
                last = stack.pop()
                nextSmallerDict[last[1]] = i
            stack.append((heights[i], i))
        for i in range(n-1, -1, -1):
            while stack and stack[-1][0] > heights[i]:
                last = stack.pop()
                prevSmallerDict[last[1]] = i
            stack.append((heights[i], i))
        for i in range(n):
            prevSmall = prevSmallerDict[i] if i in prevSmallerDict else -1
            nextSmall = nextSmallerDict[i]-1 if i in nextSmallerDict else n-1
            ans = max(ans, heights[i] * (nextSmall-prevSmall))
        return ans
"""
