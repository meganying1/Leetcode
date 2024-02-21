# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# difficulty: hard
# topics: array, binary search, divide and conquer

# problem:
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# naive solution:
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        ptr1, ptr2 = 0, 0
        length1, length2 = len(nums1), len(nums2)
        while ptr1 < length1 and ptr2 < length2:
            if nums1[ptr1] < nums2[ptr2]:
                merged.append(nums1[ptr1])
                ptr1 += 1
            else:
                merged.append(nums2[ptr2])
                ptr2 += 1
        while ptr1 < length1:
            merged.append(nums1[ptr1])
            ptr1 += 1
        while ptr2 < length2:
            merged.append(nums2[ptr2])
            ptr2 += 1
        if (length1+length2) % 2 == 1: return merged[(length1+length2)//2]
        else: return (merged[(length1+length2)//2] + merged[((length1+length2)//2)-1])/2
"""
# time complexity: O(n+m)
#     takes O(n+m) time to iterate through both lists and create merged list
#     takes O(1) time to find middle of merged list

"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        for num in nums2: nums1.insert(bisect_left(nums1, num), num)
        if length % 2 == 1: return nums1[length//2]
        return (nums1[(length//2) - 1] + nums1[length//2]) / 2
"""
# time complexity: O(m*n) <- slower than naive method
#     loop on nums2: O(m)
#     bisect_left: O(log(n+m))
#     insert: O(log(n))
#     total: m*(log(n+m) + n) = m*log(n+m) + m*n
