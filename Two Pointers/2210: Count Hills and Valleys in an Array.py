# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/
# difficulty: easy
# topics: array

# problem:
# You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].
# Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.
# Return the number of hills and valleys in nums.

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        lo, mid = 0, 1
        ans = 0
        n = len(nums)
        while mid < n-1:
            hi = mid+1
            while hi < n and nums[hi] == nums[mid]:
                hi += 1
            if hi == n: break
            if ((nums[lo] > nums[mid] and nums[hi] > nums[mid]) or
                (nums[lo] < nums[mid] and nums[hi] < nums[mid])):
                ans += 1
            lo, mid = mid, hi
        return ans
# time complexity: O(n)
# space complexity: O(1)
