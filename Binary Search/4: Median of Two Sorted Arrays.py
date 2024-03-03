# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# difficulty: hard
# topics: array, binary search, divide and conquer

# problem:
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1
        if len1 == 0:
            if len2 % 2 == 1: return nums2[len2//2]
            else: return (nums2[len2//2] + nums2[len2//2 - 1]) / 2
        lo, hi = 0, len1
        while lo <= hi:
            mid1 = (hi+lo+1) // 2
            mid2 = ((len1 + len2) // 2) - mid1
            maxLeft1 = nums1[mid1-1] if mid1 != 0 else -float("inf")
            minRight1 = nums1[mid1] if mid1 != len1 else float("inf")
            maxLeft2 = nums2[mid2-1] if mid2 != 0 else -float("inf")
            minRight2 = nums2[mid2] if mid2 != len2 else float("inf")
            if maxLeft1 > minRight2: hi = mid1-1
            elif minRight1 < maxLeft2: lo = mid1+1
            else: break
        if (len1 + len2) % 2 == 1: return min(minRight1, minRight2)
        return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2

# We have two arrays, and some amount of elements must be chosen from each array, to come on the left of the median.
# We binary search on the shorter one (faster time). If the shorter array is of length k, there are from 0 to k possible elements from this array, that appear to the left of the median.
# Our goal is to binary search on the number of elements from the smaller array, that appear to the left of the median.

# Say we start binary searching, and our first pick for the possible amount of elements that appear on the left of the median is 4.
# We can deduce how many elements from the longer array should be included from the amount of elements that go on the left among both arrays and the amount we are including from the shorter array.

# We can basically split each array into regions, like this example:
#     [] = should come on the left of the median
#     () = should come on the right of the median
#     array1 = [1, 2, 3] (5, 6, 7)
#     array2 = [20, 21, 22, 23] (24, 25, 26, 27)

# This is the correct split if all the numbers in square brackets are smaller than all the numbers in parentheses.
# We can just consider the largest square bracket numbers, and the smallest parentheses numbers- in this case, its 3 and 23 for the [], and 5 and 24 for the ().
#     3 is <= 5, because they're both from arr1 and arr1 is sorted. Similarly, 23 is <= 24, for the same reason.
#     What makes this split valid is if 3 <= 24, and 23 <= 5. The second condition fails, so we know we used too many numbers from arr2 in the left region.
# We run the binary search again, but modify the bounds. If the first condition failed, then we used too few numbers from arr2, and we modify the binary search bounds and go again.
# If both conditions succeeded, like if 3 <= 24 and pretend 23 is <= 5, then we know we have a valid split.

# We can now get the median! There are 2 cases:
#     1. The two arrays have an even total number of elements, so the median is the two middle numbers, averaged together. Consider these arrays:
#         array1 = [1, 2] (20, 40)
#         array2 = [5] (25)
#         If we write this out as one array, it is [1, 2, 5, 20, 25, 40], and the median is (5+20)/2 = 12.5.
#         Since the median is the two middle numbers averaged, and there is an equal amount of [] numbers in total and an equal amount of () numbers, the two middle numbers are the biggest [] number and the smallest () number.
#         The biggest [] number is 5, and the smallest () one is 20. So we take those two, add them, and average to get 12.5.
#     2. The total amount of elements in both arrays is odd?
#         Then we might have something like this:
#         array1 = [1, 2] (20, 40, 60)
#         array2 = [5] (25)
#         Here, the median is just the smallest number, which is 20.
#         It works because of the way we define the [] and (). For odd total elements, we define [] as the elements strictly to the left of the median, making the median the smallest () number.
#         For even total elements, we define [] as the smallest 50% of elements, making the median include exactly 1 of these in its calculation.

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
# this is the naive solution
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
