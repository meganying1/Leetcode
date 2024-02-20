# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# difficulty: hard
# topics: array, binary search, divide and conquer

# problem:
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        for num in nums2: nums1.insert(bisect_left(nums1, num), num)
        if length % 2 == 1: return nums1[length//2]
        return (nums1[(length//2) - 1] + nums1[length//2]) / 2
# time complexity: O(m*n)
#     loop on nums2: O(m)
#     bisect_left: O(log(n+m))
#     insert: O(log(n))
#     total: m*(log(n+m) + n) = m*log(n+m) + m*n
