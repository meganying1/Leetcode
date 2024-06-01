# https://leetcode.com/problems/largest-rectangle-in-histogram/
# difficulty: hard
# topics: array, stack, monotonic stack

# problem:
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        stack = []
        ans = 0
        for i in range(n):
            h = heights[i]
            start = i
            while stack and stack[-1][1] > h:
                prevI, prevH = stack.pop()
                ans = max(ans, prevH * (i-prevI))
                start = prevI
            stack.append((start, h))
        return ans
# 
# time complexity: O(n)
# space complexity: O(n)

"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        ans = 0
        for i in range(n):
            h = heights[i]
            start = i
            while stack and stack[-1][1] > h:
                prevI, prevH = stack.pop()
                ans = max(ans, prevH * (i-prevI))
                start = prevI
            stack.append((start, h))
        for (i, h) in stack:
            ans = max(ans, h * (n-i))
        return ans
"""
# use a stack to store the indices and their corresponding heights
# if the previous height at the top of the stack is greater than the current one, we can calculate the area from the previous index to the current index
#      we're assuming that the current index is the right edge
# since we know that that previous height was greater, we  append the current height and say it started at that previous index
# at the end, we know that anything remaining in the stack didn’t encounter a smaller height, so we can calculate the area from that index to the end of the array
#     can append a 0 to the end of the heights array to clean up the remaining stack

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
