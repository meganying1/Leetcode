# https://leetcode.com/problems/trapping-rain-water/description/
# difficulty: hard
# topics: array, two pointers, dynamic programming, stack, monotonic stack

# problem:
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        ans = 0
        left, right = [0] * length, [0] * length
        leftMax, rightMax = 0, 0
        for i in range(1, length):
            leftMax, rightMax = max(leftMax, height[i-1]), max(rightMax, height[length-i])
            left[i], right[length-i-1] = leftMax, rightMax
        for i in range(1, length-1):
            val = min(left[i], right[i])
            if val < height[i]: continue
            ans += val - height[i]
        return ans

# time complexity: O(n)
# space complexity: O(n)
