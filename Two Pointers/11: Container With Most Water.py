# https://leetcode.com/problems/container-with-most-water/description/
# difficulty: medium
# topics: array, two pointers, greedy

# problem:
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, = 0, len(height)-1
        ans = 0
        while left < right:
            leftHeight, rightHeight, = height[left], height[right]
            if leftHeight < rightHeight:
                ans = max(ans, leftHeight*(right-left))
                left += 1
            else:
                ans = max(ans, rightHeight*(right-left))
                right -= 1
        return ans
