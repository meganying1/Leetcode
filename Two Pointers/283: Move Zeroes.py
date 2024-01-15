# https://leetcode.com/problems/move-zeroes/description/
# difficulty: easy
# topics: array, two pointers

# problem:
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
  
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        length = len(nums)
        i, j = 0, 1
        while j < length:
            if nums[i] == 0 and nums[j] != 0:
                nums[i] = nums[j]
                nums[j] = 0
            if nums[i] != 0:
                i += 1
            j += 1
