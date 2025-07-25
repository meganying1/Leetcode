# https://leetcode.com/problems/sort-colors/
# difficulty: medium
# topics: array, two pointers, sorting

# problem:
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# using two pointers
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        lo, mid, hi = 0, 0, len(nums)-1
        while mid <= hi:
            if nums[mid] == 0:
                nums[mid], nums[lo] = nums[lo], nums[mid]
                lo += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
            else:
                mid += 1
# time complexity: O(n)
# space complexity: O(1)

# using counting sort
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = Counter(nums)
        i = 0
        for digit in (0, 1, 2):
            for _ in range(counts[digit]):
                nums[i] = digit
                i += 1
"""
# time complexity: O(n)
# space complexity: O(1)
