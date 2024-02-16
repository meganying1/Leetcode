# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# difficulty: medium
# topics: array, binary search

# problem:
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
#   [4,5,6,7,0,1,2] if it was rotated 4 times.
#   [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        lo, hi = 0, length-1
        while lo <= hi:
            mid = lo + ((hi-lo)//2)
            if nums[mid] < nums[mid-1] and nums[mid] < nums[(mid+1) % length]: return nums[mid]
            if nums[mid] < nums[0]: hi = mid-1
            elif nums[mid] > nums[-1]: lo = mid+1
            else: return nums[0]
